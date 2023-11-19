from django.db import models


# Create your models here.


class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    no_of_table = models.IntegerField()
    bookingDate = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return self.name


class SingleMenuItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self) -> str:
        return self.first_name
