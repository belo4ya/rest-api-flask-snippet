from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    pass


class BadRequest(APIException):
    code = 400


class NotFound(APIException):
    code = 404


class BadCredentials(BadRequest):
    pass


class ResourceNotFound(NotFound):
    pass
