from rest_framework.serializers import ModelSerializer
from .models import Product, Manufacturer, Category


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
