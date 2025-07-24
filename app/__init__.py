from flask import Flask
from flask_cors import CORS
from app.core.exceptions import ExceptionBase
from app.core.models.base_model import db, migrate
from app.router.router import register_routes


def create_app():
    app = Flask(__name__)

    # Configurações do CORS
    CORS(
        app,
        supports_credentials=True,
        resources={
            r"/*": {
                "origins": [
                    "http://frontend:3000",
                ]
            }
        },
    )

    # Carrega as configurações do app
    app.config.from_object("app.config.Config")

    # Desabilita o strict_slashes para evitar problemas com URLs
    app.url_map.strict_slashes = False

    # Inicializa o banco de dados e a migração
    db.init_app(app)
    migrate.init_app(app, db)

    # Registra as rotas
    register_routes(app)

    # Registra o manipulador de exceções
    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, (ExceptionBase)):
            return e.return_exception()

        return ExceptionBase(object=e).return_exception()

    return app
