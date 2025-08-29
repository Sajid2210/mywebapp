from django.contrib import admin
from .models import Category, Product, ProductImage, Variation, VariationImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0
    fields = ('name', 'slug', 'sku', 'color', 'size')
    readonly_fields = ('slug',)

@admin.action(description="Duplicate selected products (with gallery)")
def duplicate_products(modeladmin, request, queryset):
    for obj in queryset:
        images = list(obj.images.all())
        obj.pk = None
        obj.slug = ''
        obj.sku = f"{obj.sku}-COPY"
        obj.name = f"{obj.name} (Copy)"
        obj.save()
        for img in images:
            ProductImage.objects.create(product=obj, image=img.image, alt_text=img.alt_text, sort_order=img.sort_order)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'brand', 'category', 'price', 'stock', 'is_active', 'is_featured')
    list_filter = ('is_active', 'is_featured', 'category', 'brand')
    search_fields = ('name', 'sku', 'brand')
    inlines = [ProductImageInline, VariationInline]
    prepopulated_fields = {"slug": ("name",)}
    actions = [duplicate_products]

class VariationImageInline(admin.TabularInline):
    model = VariationImage
    extra = 1

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'sku', 'color', 'size')
    list_filter = ('product__category', 'color', 'size')
    search_fields = ('name', 'sku', 'product__name')
    readonly_fields = ('slug',)
    inlines = [VariationImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
