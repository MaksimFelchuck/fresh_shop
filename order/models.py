from django.db import models

# Create your models here.
from django.db.models.signals import post_save

from product.models import Product


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=120, null=True, blank=True, default=None)
    customer_email = models.EmailField(null=True, blank=True, default=None)
    customer_phone = models.CharField(max_length=50, null=True, blank=True, default=None)
    comments = models.TextField(null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Order {self.id} ({self.status.status_name}) - {self.total_price}$"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, default=None, on_delete=models.CASCADE)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    numb = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Product in order ({self.numb}: {self.product.product_name}) - {self.total_price}$"

    class Meta:
        verbose_name = "Product in order"
        verbose_name_plural = "Products in order"

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.numb * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products = ProductInOrder.objects.filter(order=order)
    order_total_price = 0
    for product in all_products:
        order_total_price += product.total_price
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
