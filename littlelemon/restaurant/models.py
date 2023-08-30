from django.db import models

# Create your models here.
class MenuCategory(models.Model):
     name=models.CharField(max_length=200)
     def __str__(self)->str:
        return self.name
     

class Menu(models.Model):
    title=models.CharField(max_length=200)
    price=models.DecimalField(null=False, max_digits=5, decimal_places=2)
    category=models.ForeignKey(MenuCategory, on_delete=models.PROTECT,default=None)
    description=models.CharField(max_length=1000, default="")
    inventory=models.IntegerField(null=False, default=100)
    def __str__(self)->str:
        return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=200)
    guests= models.SmallIntegerField(default=1)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.first_name