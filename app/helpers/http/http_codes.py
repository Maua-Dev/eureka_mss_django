from typing import Any
from app.helpers.enum.http_status_code_enum import HttpStatusCodeEnum
from app.helpers.http.http_models import HttpResponseModel


class OK(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.OK.value,
            message=message,
            body=body
        )


class Created(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.CREATED.value,
            message=message,
            body=body
        )

class NoContent(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.NO_CONTENT.value,
            message=message,
            body=body
        )


class BadRequest(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.BAD_REQUEST.value,
            message=message,
            body=body
        )


class InternalServerError(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.INTERNAL_SERVER_ERROR.value,
            message=message,
            body=body
        )


class NotFound(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.NOT_FOUND.value,
            message=message,
            body=body
        )


class Conflict(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.CONFLICT.value,
            message=message,
            body=body
        )


class RedirectResponse(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.REDIRECT.value,
            message=message,
            body=body
        )


class Forbidden(HttpResponseModel):
    def __init__(self, body: dict = None, message: str = None) -> None:
        super().__init__(
            status_code=HttpStatusCodeEnum.FORBIDDEN.value,
            message=message,
            body=body
        )
