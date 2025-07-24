from app.cadastros.models import Usuario
from app.core.schemas.base_schema import BaseSchema


class UserSchema(BaseSchema):
    __model__ = Usuario
