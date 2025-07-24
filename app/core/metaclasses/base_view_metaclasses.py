from app.core.models.base_model import BaseModel
from app.core.schemas.base_schema import BaseSchema
from app.core.schemas.schema_builder import build_dynamic_schema


class BaseViewMetaclass(type):
    def __call__(cls, *args, **kwargs):
        if getattr(cls, "schema_class", None):
            if not issubclass(cls.schema_class, BaseSchema):
                raise TypeError(
                    f"schema_class deve ser um modelo Pydantic, obtido {type(cls.schema_class)}"
                )

            model = getattr(cls.schema_class, "__model__", None)

            if model is None:
                raise ValueError(
                    f"{cls.schema_class.__name__} deve ter um atributo '__model__' definido na classe schema_class"
                )

            if not issubclass(model, BaseModel):
                raise TypeError(f"model deve ser um modelo ORM, obtido {type(model)}")

            instance = super().__call__(*args, **kwargs)

            instance.schema = build_dynamic_schema(cls.schema_class, model)

        return instance
