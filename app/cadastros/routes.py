from flask import Blueprint

from app.cadastros.views import UserView

cadastros_bp = Blueprint("cadastros", __name__, url_prefix="/cadastros")

cadastros_bp.add_url_rule("/users", view_func=UserView.as_view("user_api"))
