import sqlite3
import os
from flask import current_app


def get_db():
    db_path = os.path.join(
        current_app.instance_path,
        "shopflow.db"
    )

    os.makedirs(current_app.instance_path, exist_ok=True)

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    return connection


def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            description TEXT NOT NULL
        )
    """)

    cursor = db.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:
        products = [
            (
                "Wireless Headphones",
                1999,
                "Comfortable wireless headphones for everyday use."
            ),
            (
                "Mechanical Keyboard",
                2999,
                "Mechanical keyboard for work and gaming."
            ),
            (
                "Smart Watch",
                2499,
                "Smart watch with fitness and notification features."
            ),
            (
                "USB-C Hub",
                1299,
                "Multi-port USB-C hub for laptops and desktops."
            )
        ]

        db.executemany("""
            INSERT INTO products (name, price, description)
            VALUES (?, ?, ?)
        """, products)

    db.commit()
    db.close()


def get_all_products():
    db = get_db()

    products = db.execute("""
        SELECT * FROM products
    """).fetchall()

    db.close()

    return products


def get_product(product_id):
    db = get_db()

    product = db.execute("""
        SELECT * FROM products
        WHERE id = ?
    """, (product_id,)).fetchone()

    db.close()

    return product