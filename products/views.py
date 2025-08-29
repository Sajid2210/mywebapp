from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Min, Max
from .models import Product, Category, Variation

def product_list(request):
    qs = Product.objects.filter(is_active=True)

    q = request.GET.get('q')
    cat = request.GET.get('category')
    brand = request.GET.get('brand')
    minp = request.GET.get('min')
    maxp = request.GET.get('max')
    sort = request.GET.get('sort')

    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(brand__icontains=q) | Q(short_description__icontains=q))
    if cat:
        qs = qs.filter(category__slug=cat)
    if brand:
        qs = qs.filter(brand__iexact=brand)
    if minp:
        qs = qs.filter(price__gte=minp)
    if maxp:
        qs = qs.filter(price__lte=maxp)
    if sort == 'price_asc':
        qs = qs.order_by('price')
    elif sort == 'price_desc':
        qs = qs.order_by('-price')
    elif sort == 'featured':
        qs = qs.order_by('-is_featured', '-created_at')
    else:
        qs = qs.order_by('-created_at')

    paginator = Paginator(qs, 12)
    page_obj = paginator.get_page(request.GET.get('page'))

    price_range = Product.objects.filter(is_active=True).aggregate(min_price=Min('price'), max_price=Max('price'))
    categories = Category.objects.filter(is_active=True).order_by('name').select_related('parent')

    ctx = {
        'page_obj': page_obj,
        'categories': categories,
        'price_range': price_range,
        'active_filters': {'q': q, 'category': cat, 'brand': brand, 'min': minp, 'max': maxp, 'sort': sort},
    }
    return render(request, 'products/shop_list.html', ctx)

def product_detail(request, product_slug, variation_slug=None):
    product = get_object_or_404(Product.objects.select_related('category'), slug=product_slug, is_active=True)

    # Select variation (optional)
    variations_qs = product.variations.all().order_by('name')
    selected_variation = None
    if variation_slug:
        selected_variation = get_object_or_404(variations_qs, slug=variation_slug)
    elif variations_qs.exists():
        selected_variation = variations_qs.first()

    related = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:8]

    ctx = {
        'product': product,
        'selected_variation': selected_variation,
        'variations': variations_qs,
        'related': related,
    }
    return render(request, 'products/product_detail.html', ctx)
