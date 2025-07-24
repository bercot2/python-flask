from http import HTTPStatus

from flask import jsonify


class ExceptionBase(Exception):
    def __init__(
        self,
        message="Erro interno no servidor",
        status_code: HTTPStatus = HTTPStatus.INTERNAL_SERVER_ERROR,
        object: Exception = None,
        *args: object
    ) -> None:
        self.message = message if object is None else str(object)

        _status_code = getattr(object, "code", None)
        _status_code_valid = (
            isinstance(_status_code, int) and 100 <= _status_code <= 599
        )

        self.status_code = (
            status_code if object is None or not _status_code_valid else _status_code
        )

        super().__init__(*args)

    def return_exception(self):
        return jsonify({"error": self.message}), self.status_code


class ExceptionNoDataFound(ExceptionBase):
    """Exceção levantada quando nenhum dado é encontrado na consulta."""

    def __init__(
        self,
        message="Dados não encontrados",
        status_code: HTTPStatus = HTTPStatus.NOT_FOUND,
        *args: object
    ):
        super().__init__(message, status_code, *args)


class ExceptionBadRequest(ExceptionBase):
    """Exceção levantada quando ocorre um erro no request da transação."""

    def __init__(
        self,
        message="Erro na requisição",
        status_code: HTTPStatus = HTTPStatus.BAD_REQUEST,
        *args: object
    ):
        super().__init__(message, status_code, *args)
