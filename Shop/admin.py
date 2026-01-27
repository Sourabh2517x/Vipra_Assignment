from django.contrib import admin
from .models import ProductModel,Order
# Register your models here.
admin.site.register(ProductModel),
admin.site.register(Order)