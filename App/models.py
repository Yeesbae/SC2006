from django.db import models

# Create your models here.
class Default(models.Model):
    # This is the model for the default database.
    # - Default ID
    # - Default Field
    default_id = models.AutoField(primary_key=True)
    default_field = models.CharField(max_length=50)

    class Meta:
        app_label = 'App'
        db_table = 'default'

class Account(models.Model):
    # This is the model for the account database.
    # - Account ID
    # - Username
    # - Password
    # - Email
    # - First Name
    # - Last Name
    # - Date of Birth
    account_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    class Meta:
        app_label = 'App'
        db_table = 'account'


class Property(models.Model):
    # This is the model for the property database.
    # - Property ID
    # - Address
    # - City
    # - State
    # - Zip Code
    # - Price
    # - Bedrooms
    # - Bathrooms
    # - Square Feet
    property_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.IntegerField()

    class Meta:
        app_label = 'App'
        db_table = 'property'

class ButtonClick(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)