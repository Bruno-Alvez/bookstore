from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        required=True
    )

    category_detail = CategorySerializer(
        many=True,
        read_only=True,
        source='category'
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'active',
            'category',         # Para escrita (envia ID)
            'category_detail'   # Para leitura (recebe os detalhes)
        ]
