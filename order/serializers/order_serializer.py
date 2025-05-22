from rest_framework import serializers
from product.models.product import Product
from order.models.order import Order
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
        required=True
    )

    product_detail = ProductSerializer(
        many=True,
        read_only=True,
        source='product'
    )

    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = [
            'product',          # Envia os IDs dos produtos
            'product_detail',   # Recebe detalhes dos produtos na resposta
            'total'
        ]
