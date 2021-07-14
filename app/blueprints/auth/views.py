from flask_smorest import Blueprint

from . import schemas
from . import services

bp = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth',
    description='Simple authentication service based on a JWT token.'
)


@bp.post('/sign_up')
@bp.arguments(schemas.Credentials, as_kwargs=True)
@bp.response(200, schemas.AccessToken)
def sign_up_view(username, password):
    access_token = services.sign_up(username, password)
    return {'access_token': access_token}


@bp.post('/sign_in')
@bp.arguments(schemas.Credentials, as_kwargs=True)
@bp.response(200, schemas.AccessToken)
def sign_in_view(username, password):
    access_token = services.sign_in(username, password)
    return {'access_token': access_token}
