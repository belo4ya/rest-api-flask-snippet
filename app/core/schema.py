from app.extensions import ma


class ServiceFieldsMixin(ma.Schema):
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    created_by = ma.auto_field()
    updated_by = ma.auto_field()


SERVICE_FIELDS = [
    'created_at',
    'updated_at',
    'created_by',
    'updated_by',
]


FOR_CREATE = {
    'exclude': ['id', *SERVICE_FIELDS]
}

FOR_READ = {
    'exclude': SERVICE_FIELDS
}
