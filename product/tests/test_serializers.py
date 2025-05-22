import pytest
from product.serializers.category_serializer import CategorySerializer
from product.serializers.product_serializer import ProductSerializer
from product.models.category import Category
from product.models.product import Product


@pytest.mark.django_db
def test_category_serializer_valid():
    data = {
        "title": "Eletrônicos",
        "slug": "eletronicos",
        "description": "Produtos da categoria eletrônicos",
        "active": True
    }

    serializer = CategorySerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["title"] == "Eletrônicos"
    assert serializer.validated_data["slug"] == "eletronicos"


@pytest.mark.django_db
def test_category_serializer_invalid_missing_title():
    data = {
        "slug": "sem-titulo",
        "description": "Categoria sem título",
        "active": True
    }

    serializer = CategorySerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors


@pytest.mark.django_db
def test_product_serializer_valid():
    category = Category.objects.create(
        title="Games",
        slug="games",
        description="Produtos de games",
        active=True
    )

    data = {
        "title": "Playstation 5",
        "description": "Console de última geração",
        "price": 5000,
        "active": True,
        "category": [category.id]
    }

    serializer = ProductSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["title"] == "Playstation 5"
    assert serializer.validated_data["price"] == 5000
    assert serializer.validated_data["active"] is True


@pytest.mark.django_db
def test_product_serializer_invalid_missing_title():
    category = Category.objects.create(
        title="Games",
        slug="games",
        description="Produtos de games",
        active=True
    )

    data = {
        "description": "Console de última geração",
        "price": 5000,
        "active": True,
        "category": [category.id]
    }

    serializer = ProductSerializer(data=data)
    assert not serializer.is_valid()
    assert "title" in serializer.errors
