from flask import Flask
from app.cadastros.routes import cadastros_bp


def register_routes(app: Flask):
    app.register_blueprint(cadastros_bp)
