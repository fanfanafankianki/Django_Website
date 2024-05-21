from django.db import models

# Create your models here.
class Testing(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)    
    imagePath = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    products = models.ManyToManyField('FoodProduct', related_name='testings')

    def __str__(self):
        return f"Name: {self.name}, image {self.imagePath}, description: {self.description}"
    

class FoodProduct(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)  
    calories = models.IntegerField()

    def __str__(self):
        return self.name
