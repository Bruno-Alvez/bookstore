import pytest
from django.contrib.auth.models import User
from order.models.order import Order
from product.models.product import Product
from product.models.category import Category
from order.serializers.order_serializer import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_total():
    # Cria usuário fake
    user = User.objects.create_user(username="testuser", password="testpassword")

    # Cria categoria
    category = Category.objects.create(
        title="Games", slug="games", description="Jogos", active=True
    )

    # Cria produtos
    product1 = Product.objects.create(
        title="Playstation 5", description="Console", price=5000, active=True
    )
    product1.category.add(category)

    product2 = Product.objects.create(
        title="Xbox Series X", description="Console", price=4500, active=True
    )
    product2.category.add(category)

    # Dados para criar pedido
    data = {"product": [product1.id, product2.id]}

    # Valida e salva
    serializer = OrderSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    order = serializer.save(user=user)

    # Verifica se o total está correto
    assert order.product.count() == 2
    assert order.product.first().title == "Playstation 5"
    assert order.product.last().title == "Xbox Series X"

    response_data = OrderSerializer(order).data
    assert response_data["total"] == 9500
