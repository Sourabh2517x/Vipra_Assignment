from django.contrib import admin
from django.urls import path
from Shop import views
from Shop.views import create_checkout_session,my_orders

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('checkout/<int:product_id>/', create_checkout_session, name='checkout'),
    path('myorders/', my_orders, name='myorder'),
    
]
