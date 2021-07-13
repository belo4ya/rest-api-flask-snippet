from flask_smorest import Blueprint

bp = Blueprint(
    'cats',
    __name__,
    url_prefix='/cats',
    description='Cats service.'
)
