from flask import request
from app.cadastros.models import Usuario
from app.cadastros.schemas import UserSchema
from app.core.views.base_view import BaseView


class UserView(BaseView):
    schema_class = UserSchema

    def get_records_query(self):
        user_id = request.args.get("id", type=int)
        if user_id:
            return Usuario.query.filter_by(id=user_id).all()
        return Usuario.query.all()
