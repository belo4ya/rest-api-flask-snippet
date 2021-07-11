from flask import Blueprint
from flask_restx import Api

from .resources import cats

__version__ = 2

bp = Blueprint(f'api_v{__version__}', __name__, url_prefix=f'/api/v{__version__}')
api = Api(
    bp,
    title='My API',
    version=f'{__version__}.0',
    description='Simple description for my API',
)

api.add_namespace(cats)
