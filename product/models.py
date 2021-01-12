from django.db import models


# Create your models here.
class Status(models.Model):
    status_name = models.CharField(max_length=20, null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.status_name}"

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class TypeOfProduct(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Product(models.Model):
    product_name = models.CharField(max_length=120, null=True, blank=True, default=None)
    product_description = models.TextField(null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.ForeignKey(Status, null=True, blank=True, default=None, on_delete=models.CASCADE)
    type = models.ForeignKey(TypeOfProduct, null=True, blank=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Image {self.id}"

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
