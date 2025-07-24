from typing import get_args, get_origin, Optional
from pydantic import Field
from app.core.schemas.base_schema import BaseSchema
from app.core.models.base_model import BaseModel


def build_dynamic_schema(
    schema_class: type[BaseSchema], model_class: type[BaseModel]
) -> type[BaseSchema]:
    annotations = getattr(schema_class, "__annotations__", {})
    fields_defaults = {}

    for attr_name, mapped_type in model_class.__annotations__.items():
        origin = get_origin(mapped_type)
        if origin and origin.__name__ == "Mapped":
            field_type = get_args(mapped_type)[0]
            column = getattr(model_class, attr_name)

            is_nullable = getattr(column, "nullable", False)
            if is_nullable:
                field_type = Optional[field_type]

            if attr_name.lower() == "id":
                annotations[attr_name] = Optional[field_type]
                fields_defaults[attr_name] = Field(
                    default=None,
                    required=False,
                )
            else:
                annotations[attr_name] = field_type
                fields_defaults[attr_name] = Field(default=None if is_nullable else ...)

    for key, field in schema_class.model_fields.items():
        fields_defaults[key] = field

    namespace = {
        "__annotations__": annotations,
        **fields_defaults,
    }

    return type(f"{schema_class.__name__}Generated", (schema_class,), namespace)
