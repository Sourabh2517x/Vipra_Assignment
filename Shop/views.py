from django.shortcuts import render
from .models import ProductModel,Order
import stripe
from django.conf import settings
from django.shortcuts import redirect,redirect, get_object_or_404
# Create your views here.
def index(request):
    product_objects = ProductModel.objects.all()
        
    return render(request,'Shop/index.html',{'product_objects':product_objects})



stripe.api_key = settings.STRIPE_SECRET_KEY


# views.py
def create_checkout_session(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)

    if request.method == "POST":
        # Get quantity from the form
        quantity = int(request.POST.get("quantity", 1))
    else:
        quantity = 1

    # Create Stripe session with the correct quantity
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "inr",
                "unit_amount": int(product.price * 100),
                "product_data": {"name": product.title},
            },
            "quantity": quantity,  # now from user input
        }],
        mode="payment",
        success_url="http://127.0.0.1:8000/myorders/",
        cancel_url="http://127.0.0.1:8000/",
    )

    # Save the order in DB
    Order.objects.create(
        product_name=product.title,
        product_image=product.image,
        amount=product.price * quantity,
        quantity=quantity,
        status="PENDING",
        stripe_session_id=session.id
    )

    return redirect(session.url)


def my_orders(request):
    orders = Order.objects.filter(status="PENDING")

    for order in orders:
        try:
            session = stripe.checkout.Session.retrieve(order.stripe_session_id)
            if session.payment_status == "paid":
                order.status = "PAID"
                order.save()
        except stripe.error.StripeError:
            pass  # handle errors if needed

    # Only show paid orders
    paid_orders = Order.objects.filter(status="PAID")
    return render(request, 'Shop/myorders.html', {'orders': paid_orders})