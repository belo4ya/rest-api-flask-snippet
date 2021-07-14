from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    data = {
        'message': None,
        'errors': None,
        'headers': None
    }

    def __init__(self, description=None, response=None, errors=None, headers=None):
        super(APIException, self).__init__(description, response)
        self.data['message'] = description
        self.data['errors'] = errors
        self.data['headers'] = headers


class BadRequest(APIException):
    code = 400


class NotFound(APIException):
    code = 404


class BadCredentials(BadRequest):
    pass


class ResourceNotFound(NotFound):
    pass


class AccessDenied(APIException):
    code = 403
