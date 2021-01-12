from django.shortcuts import render

# Create your views here.
from product.models import *


def product_detail(request, product_name):
    product = Product.objects.get(product_name=product_name)
    image = ProductImage.objects.get(product=product)
    products = ProductImage.objects.all()
    context = {
        "product": product,
        "image": image,
        "products": products
    }
    return render(request, "shop-detail.html", context)


def gallery(request):
    images = ProductImage.objects.all()
    context = {
        "images": images,
    }
    return render(request, "gallery.html", context)
