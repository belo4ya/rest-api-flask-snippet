from flask_restx import abort
from http import HTTPStatus

status = HTTPStatus


def abort_if_not_exist(model, pk: int):
    abort(status.NOT_FOUND, f"{model.__class__.__name__} {pk} doesn't exist")
