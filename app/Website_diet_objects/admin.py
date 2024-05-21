from django.contrib import admin
from .models import Product, NutritionalInfo, ProductConsumption
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "description", "image"]
    list_filter = ("product_name",)
    search_fields = ("description",)

@admin.register(NutritionalInfo)
class NutritionalInfoAdmin(admin.ModelAdmin):

    list_display = ["product", "calories", "carbohydrates", "protein", "fats", "fiber", "salt", "vitamin_A",
                    "vitamin_B1", "vitamin_B2", "vitamin_B6", "vitamin_C", "vitamin_E", "calcium", "iron",
                    "potassium", "magnesium", "sodium"]
    list_filter = ("calories",)
    search_fields = ("product",)

@admin.register(ProductConsumption)
class ProductConsumptionAdmin(admin.ModelAdmin):
    list_display = ["profile", "product", "consumption_date", "quantity"]
    list_filter = ("consumption_date",)
    search_fields = ("consumption_date",)
