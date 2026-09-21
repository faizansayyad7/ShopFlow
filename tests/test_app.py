import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200


def test_products_page(client):
    response = client.get("/products")

    assert response.status_code == 200


def test_product_details(client):
    response = client.get("/product/1")

    assert response.status_code == 200


def test_invalid_product(client):
    response = client.get("/product/999")

    assert response.status_code == 404


def test_add_to_cart(client):
    response = client.get("/add-to-cart/1")

    assert response.status_code == 302


def test_cart_page(client):
    response = client.get("/cart")

    assert response.status_code == 200


def test_checkout_page(client):
    response = client.get("/checkout")

    assert response.status_code == 200