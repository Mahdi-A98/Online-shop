from rest_framework.serializers import Serializer, ModelSerializer
from .models import Product, Category

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description','category','image','stock']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description','parent_category']