from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404

def shop_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    paginator = Paginator(products, 9)  # 9 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'products': page_obj.object_list,
        'total_products': paginator.count,
    }
    return render(request, 'products/shop.html', context)


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    similar_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    return render(request, 'products/product_detail.html', {
        'product': product,
        'similar_products': similar_products,
    })
