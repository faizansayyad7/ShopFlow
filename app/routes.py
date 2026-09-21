from flask import Blueprint, render_template, redirect, url_for, session

from app.models import get_all_products, get_product


main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/products")
def product_list():
    products = get_all_products()

    return render_template(
        "products.html",
        products=products
    )


@main.route("/product/<int:product_id>")
def product_detail(product_id):
    product = get_product(product_id)

    if product is None:
        return "Product not found", 404

    return render_template(
        "product.html",
        product=product
    )


@main.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    product = get_product(product_id)

    if product is None:
        return "Product not found", 404

    # Get existing cart
    cart = session.get("cart", {})

    # Convert old cart format (list) into new format (dictionary)
    if isinstance(cart, list):
        cart = {
            str(item_id): 1
            for item_id in cart
        }

    # Convert product ID to string because Flask session
    # stores dictionary keys as strings
    product_id = str(product_id)

    # Increase quantity if product already exists
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    # Save updated cart in session
    session["cart"] = cart

    return redirect(url_for("main.cart"))


@main.route("/cart")
def cart():
    cart = session.get("cart", {})

    # Safety check for old cart format
    if isinstance(cart, list):
        cart = {
            str(item_id): 1
            for item_id in cart
        }

    cart_products = []
    total = 0

    # Get every product from database
    for product_id, quantity in cart.items():

        product = get_product(int(product_id))

        if product:
            subtotal = product["price"] * quantity

            cart_products.append({
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal
            })

            total += subtotal

    return render_template(
        "cart.html",
        cart_products=cart_products,
        total=total
    )


@main.route("/checkout")
def checkout():
    return render_template("checkout.html")