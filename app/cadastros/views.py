from app.cadastros.models import Usuario
from app.cadastros.schemas import UserSchema
from app.core.views.base_view import BaseView


class UserView(BaseView):
    schema_class = UserSchema
    records_query = lambda _: Usuario.query.all()

    def get(self):
        return super().get()

    def post(self):
        return super().post()
