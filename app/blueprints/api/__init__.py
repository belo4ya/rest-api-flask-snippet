from flask_smorest import Blueprint

from .v1 import bp as v1_bp
from .v2 import bp as v2_bp

bp = Blueprint(
    'api',
    __name__,
    url_prefix='/api',
    description='Main API service.'
)

bp.register_blueprint(v1_bp)
bp.register_blueprint(v2_bp)
