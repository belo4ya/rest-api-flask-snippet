from flask_smorest import Blueprint
from flask.views import MethodView

from app.blueprints.auth import has_access, ROLES, PERMISSIONS
from app.core.database import db
from app.core.schema import FOR_READ, FOR_CREATE

from .. import schemas
from .. import models

bp = Blueprint(
    'raccoons',
    __name__,
    url_prefix='/raccoons',
    description='Raccoons service.'
)


@bp.route('/meow', methods=['GET', 'POST'])
@bp.response(200, schemas.MeowSchema)
def raccoon_meow_view():
    return {'meow': models.Raccoon.MEOW}


@bp.route('/')
class RaccoonListView(MethodView):

    @bp.response(200, schemas.RaccoonSchema(many=True, **FOR_READ))
    @has_access(permissions=[PERMISSIONS.CAN_READ])
    def get(self):
        return models.Raccoon.all()

    @bp.arguments(schemas.RaccoonSchema(**FOR_CREATE))
    @bp.response(201, schemas.RaccoonSchema(**FOR_READ))
    @has_access(roles=[ROLES.USER])
    def post(self, raccoon_data):
        raccoon = models.Raccoon.create(**raccoon_data)
        db.session.commit()

        return raccoon


@bp.route('/<int:raccoon_id>')
class RaccoonView(MethodView):

    @has_access(permissions=[PERMISSIONS.CAN_READ])
    def get(self, raccoon_id):
        pass

    @has_access(roles=[ROLES.USER])
    def put(self, raccoon_id):
        pass

    @has_access(roles=[ROLES.USER])
    def delete(self, raccoon_id):
        pass


@bp.route('/batch')
class RaccoonBatchView(MethodView):
    decorators = [
        has_access(roles=[ROLES.ADMIN])
    ]

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
