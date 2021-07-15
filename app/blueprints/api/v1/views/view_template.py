from flask_smorest import Blueprint

bp = Blueprint(
    'view_template',
    __name__,
    url_prefix='/view-template',
    description='Template service.'
)
