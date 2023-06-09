from django.db import models


# Create your models here.
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=50)
    admin_email = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=8)

    def __str__(self):
        return self.admin_name


class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    menu_name = models.CharField(max_length=50)

    def __str__(self):
        return self.menu_name


class Foodbuyer(models.Model):
    buyer_id = models.AutoField(primary_key=True)
    buyer_name = models.CharField(max_length=50)
    buyer_location = models.CharField(max_length=50)
    buyer_address = models.CharField(max_length=50)
    buyer_contact = models.CharField(max_length=13)
    buyer_password = models.CharField(max_length=8)

    def __str__(self):
        return self.buyer_name


class Foodvendor(models.Model):
    vendor_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    vendor_location = models.CharField(max_length=50)
    vendor_contact = models.CharField(max_length=50)
    vendor_password = models.CharField(max_length=8)
    admin_id = models.ForeignKey('Admin', on_delete=models.CASCADE)
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.vendor_name


class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=50)
    image_file = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.image_name


class Dishes(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=50)
    dish_price = models.IntegerField(default=0)
    menu_id = models.ForeignKey('Menu', on_delete=models.CASCADE)
    image_id = models.ForeignKey('Image', on_delete=models.CASCADE)

    def __str__(self):
        return self.dish_name


class Shoppingcart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    dish_id = models.ForeignKey('Dishes', on_delete=models.CASCADE)
    cart_quantity = models.IntegerField(default=0)
    cart_date_added = models.DateField(null=True)

    def __str__(self):
        return str(self.cart_id)


class Orderfood(models.Model):
    order_id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey('FoodVendor', on_delete=models.CASCADE)
    buyer_id = models.ForeignKey('Foodbuyer', on_delete=models.CASCADE)
    dish_id = models.ForeignKey('Dishes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.order_id)