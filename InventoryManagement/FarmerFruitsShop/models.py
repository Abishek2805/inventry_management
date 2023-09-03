from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Location(models.Model):
    l_name = models.CharField(max_length=70)
    def __str__(self):
        return self.l_name

class Product_Movement(models.Model):
    f_name = models.ForeignKey(Product,related_name="from_location", on_delete=models.CASCADE,null=True,blank=True)
    from_location = models.ForeignKey(Location,related_name="from_location", on_delete=models.CASCADE,null=True,blank=True)
    to_location = models.ForeignKey(Location,related_name="to_location", on_delete=models.CASCADE,null=True,blank=True)
    p_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    time_stamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)

