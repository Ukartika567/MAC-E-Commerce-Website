from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models. CharField(max_length=250)
    category= models.CharField(max_length=250, default="")
    subcategory=models.CharField(max_length=250, default="")
    price=models.IntegerField(default=0)
    desc = models.TextField(max_length=5000, default="")
    pub_date = models.DateField()
    image=CloudinaryField('image')
    
    def __str__(self):
        return self.product_name

# Exercise-
# How many type of model can we add in the shop app give the name and create that in this models.py file.
# Solution- ProductDetails, Customer, CustmerDetails, OrderDetails, searchproduct etc.    

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=70, default='')
    phone=models.CharField(max_length=70, default='')
    desc=models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=50000)
    amount=models.IntegerField(default=0)
    name = models.CharField(max_length= 80)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."