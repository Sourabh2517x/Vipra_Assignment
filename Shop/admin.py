from django.contrib import admin
from .models import ProductModel,Order

admin.site.register(ProductModel),
admin.site.register(Order)