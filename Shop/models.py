from django.db import models

# Create your models here.
class ProductModel(models.Model):
    
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()               # we are using text field for description because description can be a lot longer for a product
    image = models.CharField(max_length=300)
      
    
class Order(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.CharField(max_length=300)
    amount = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1) # <-- track quantity
    stripe_session_id = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=[("PENDING", "Pending"), ("PAID", "Paid")],
        default="PENDING"
    )
    created_at = models.DateTimeField(auto_now_add=True)