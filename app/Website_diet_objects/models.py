from django.db import models
from Website_training_objects.models import UserProfile
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="product_images", null=True, blank=True)


    def __str__(self):
        return f"Product: {self.product_name} and description: {self.description}"


class NutritionalInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    # Basic Nutrition Info
    calories = models.FloatField()
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    fiber = models.FloatField(blank=True, null=True)
    salt = models.FloatField(blank=True, null=True)

    # Vitamins
    vitamin_A = models.FloatField(blank=True, null=True)
    vitamin_B1 = models.FloatField(blank=True, null=True)
    vitamin_B2 = models.FloatField(blank=True, null=True)
    vitamin_B6 = models.FloatField(blank=True, null=True)
    vitamin_C = models.FloatField(blank=True, null=True)
    vitamin_E = models.FloatField(blank=True, null=True)

    # Minerals
    calcium = models.FloatField(blank=True, null=True)
    iron = models.FloatField(blank=True, null=True)
    potassium = models.FloatField(blank=True, null=True)
    magnesium = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)

    def __str__(self):
        return (f"Product: {self.product.product_name}, "
                f"Kcal: {self.calories}, "
                f"Węglowodany: {self.carbohydrates} g, "
                f"Białko: {self.protein} g, "
                f"Tłuszcze: {self.fats} g, "
                f"Błonnik: {self.fiber} g, "
                f"Sól: {self.salt} g, "
                f"Witamina A: {self.vitamin_A} µg, "
                f"Witamina B1: {self.vitamin_B1} mg, "
                f"Witamina B2: {self.vitamin_B2} mg, "
                f"Witamina B6: {self.vitamin_B6} mg, "
                f"Witamina C: {self.vitamin_C} mg, "
                f"Witamina E: {self.vitamin_E} mg, "
                f"Wapń: {self.calcium} mg, "
                f"Żelazo: {self.iron} mg, "
                f"Potas: {self.potassium} mg, "
                f"Magnez: {self.magnesium} mg, "
                f"Sód: {self.sodium} mg")

class ProductConsumption(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    consumption_date = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField()

    def __str__(self):
        return f"Consumption of {self.product.product_name} on {self.consumption_date} by {self.profile}"
