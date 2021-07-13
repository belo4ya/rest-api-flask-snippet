from flask_smorest import Blueprint

bp = Blueprint(
    'dogs',
    __name__,
    url_prefix='/dogs',
    description='Dogs service.'
)
