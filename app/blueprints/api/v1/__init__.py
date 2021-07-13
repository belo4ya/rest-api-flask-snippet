from flask_smorest import Blueprint

from .views import view_bps

bp = Blueprint(
    'v1',
    __name__,
    url_prefix='/v1',
    description='API version 1.'
)

for bp_ in view_bps:
    bp.register_blueprint(bp_)
