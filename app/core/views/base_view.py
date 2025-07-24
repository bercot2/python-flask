from http import HTTPStatus
from flask import request
from flask.views import MethodView
from pydantic import ValidationError
from app.core.metaclasses.base_view_metaclasses import BaseViewMetaclass


class BaseView(MethodView, metaclass=BaseViewMetaclass):
    schema_class = None

    def get_records_query(self):
        if hasattr(self, "schema"):
            raise ValueError(
                f"get_records_query não implementada para a view {self.__class__.__name__}. Certifique-se de implementar a função 'get_records_query'."
            )

    def get_schema(self):
        if hasattr(self, "schema"):
            return self.schema

    def get_schema_serialize(self):
        if hasattr(self, "schema"):
            paginate: bool = request.args.get(
                "page", None
            ) is not None and request.args.get("per_page", None)

            model_instances = self.get_records_query()

            if isinstance(model_instances, list):
                if paginate:
                    page = int(request.args.get("page", 1))
                    per_page = int(request.args.get("per_page", 10))

                    total = len(model_instances)
                    start = (page - 1) * per_page
                    end = start + per_page
                    paginated = model_instances[start:end]

                    result = [
                        self.schema.model_validate(record).model_dump()
                        for record in paginated
                    ]

                    return {
                        "results": result,
                        "total": total,
                        "page": page,
                        "pages": (total + per_page - 1) // per_page,
                        "per_page": per_page,
                    }
                else:
                    return [
                        self.schema.model_validate(model_instance).model_dump()
                        for model_instance in model_instances
                    ]

            return self.schema.model_validate(model_instances).model_dump()

    def get(self):
        try:
            if hasattr(self, "schema"):
                data = self.get_schema_serialize()
                return data, HTTPStatus.OK
        except ValidationError as e:
            return {"error": e.errors()}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

        raise ValueError("Schema não definida para a view")

    def post(self):
        try:
            data = request.get_json()

            if hasattr(self, "schema"):
                if isinstance(data, list):
                    validated_data = [self.schema.model_validate(item) for item in data]
                    datas = [
                        self.schema.__model__(**item.model_dump(exclude_none=True))
                        for item in validated_data
                    ]

                    new_instances = self.schema.__model__.bulk_save(datas)

                    data = [
                        self.schema.model_validate(instance).model_dump()
                        for instance in new_instances
                    ]
                else:
                    validated_data = self.schema.model_validate(data)

                    data = validated_data.model_dump(exclude_none=True)

                    new_instance = self.schema.__model__(**data).save()

                    data["id"] = new_instance.id

                return data, HTTPStatus.CREATED
        except ValidationError as e:
            return {"error": e.errors()}, HTTPStatus.BAD_REQUEST
        except Exception as e:
            return {"error": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR

        raise ValueError("Schema não definida para a view")
