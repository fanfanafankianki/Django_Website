from rest_framework import serializers
from .models import Testing, FoodProduct


class FoodProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodProduct
        fields = ['id', 'name', 'calories'] 

class TestingSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=FoodProduct.objects.all())

    class Meta:
        model = Testing
        fields = ['description', 'products', 'imagePath', 'name']