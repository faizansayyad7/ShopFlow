from flask import Flask


def create_app():
    app = Flask(__name__)

    app.secret_key = "shopflow-dev-secret-key"

    from app.routes import main
    app.register_blueprint(main)

    from app.models import init_db

    with app.app_context():
        init_db()

    return app