from flask_smorest import Blueprint

from .views import view_bps

bp = Blueprint(
    'v2',
    __name__,
    url_prefix='/v2',
    description='API version 2.'
)

for bp_ in view_bps:
    bp.register_blueprint(bp_)
