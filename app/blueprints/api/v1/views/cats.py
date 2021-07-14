from flask_smorest import Blueprint

from app.blueprints.auth import services
from app.blueprints.auth import security

bp = Blueprint(
    'cats',
    __name__,
    url_prefix='/cats',
    description='Cats service.'
)


@bp.get('/get')
@services.has_access(permissions=[
    security.PERMISSIONS.CAN_READ
])
def get_cats_view():
    return {'cats': 'wow!'}
