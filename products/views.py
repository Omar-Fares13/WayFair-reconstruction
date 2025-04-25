from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

def shop_view(request):

    query = request.GET.get('q')
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    products = products.order_by('-created_at')
    paginator = Paginator(products, 9)  # 9 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'total_products': paginator.count,
        'query': query,
    }
    return render(request, 'products/shop.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'similar_products': similar_products,
    })

def shop_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, is_available=True).order_by('-created_at')
    categories = Category.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'total_products': products.count(),
        'selected_category': category,
    }
    return render(request, 'products/shop.html', context)