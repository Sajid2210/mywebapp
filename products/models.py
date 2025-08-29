from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from django.utils import timezone

def unique_slugify(instance, value, slug_field_name='slug', within_qs=None):
    base = slugify(value) or "item"
    unique_slug = base
    num = 1
    if within_qs is None:
        ModelClass = instance.__class__
        while ModelClass.objects.filter(**{slug_field_name: unique_slug}).exclude(pk=instance.pk).exists():
            unique_slug = f"{base}-{num}"
            num += 1
        return unique_slug
    while within_qs.filter(**{slug_field_name: unique_slug}).exclude(pk=instance.pk).exists():
        unique_slug = f"{base}-{num}"
        num += 1
    return unique_slug

class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=180)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    brand = models.CharField(max_length=120, blank=True)
    sku = models.CharField(max_length=80, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    mrp = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    short_description = models.CharField(max_length=240, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='products/cover/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    color = models.CharField(max_length=60, blank=True)
    size = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.sku})"

    @property
    def selling_price(self):
        return self.price

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/gallery/')
    alt_text = models.CharField(max_length=160, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"Image for {self.product.name}"

# ================= Variations (minimal diffs only) =================

class Variation(models.Model):
    """
    Only different fields from Product:
    - name (display name for this variation)
    - slug (unique per product)
    - sku
    - color
    - size
    All other details (price/mrp/description/brand etc.) come from Product.
    """
    product = models.ForeignKey(Product, related_name='variations', on_delete=models.CASCADE)
    name = models.CharField(max_length=160, help_text="e.g., Red / 26-inch")
    slug = models.SlugField(max_length=220, blank=True, help_text="Unique per product")
    sku = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=60, blank=True)
    size = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('product', 'slug'),)
        ordering = ['product', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            qs = Variation.objects.filter(product=self.product)
            # Auto name if not given but color/size set
            base_name = self.name or " ".join(x for x in [self.color, self.size] if x).strip() or "variant"
            self.slug = unique_slugify(self, base_name, within_qs=qs)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} — {self.name or (self.color + ' ' + self.size).strip()}"

class VariationImage(models.Model):
    variation = models.ForeignKey(Variation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/variation/')
    alt_text = models.CharField(max_length=160, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"Image for {self.variation}"
