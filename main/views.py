from django.shortcuts import render
from product.models import *
# Create your views here.


def main(request):
    products = Product.objects.all()
    products_images = ProductImage.objects.all()
    context = {
        "products": products,
        "images": products_images
    }

    return render(request, "index.html", context)


