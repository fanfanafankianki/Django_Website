from django.forms import ModelForm
from .models import Product, ProductConsumption, NutritionalInfo

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image']

class NutritionalInfoForm(ModelForm):
    class Meta:
        model = NutritionalInfo
        fields = ['calories', 'carbohydrates', 'protein', 'fats', 'fiber', 'salt', 'vitamin_A', 'vitamin_B1', 'vitamin_B2',
                  'vitamin_B6', 'vitamin_C', 'vitamin_E', 'calcium', 'iron', 'potassium', 'magnesium', 'sodium']

class ProductConsumptionForm(ModelForm):
    class Meta:
        model = ProductConsumption
        fields = ['profile', 'product', 'quantity']
