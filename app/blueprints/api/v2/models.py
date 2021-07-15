from app.core.database import Model, db
from datetime import datetime


class Raccoon(Model):
    __tablename__ = 'raccoons'
    __repr_attrs__ = ['name', 'birthdate']

    name = db.Column(db.String(255), nullable=True)
    birthdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    MEOW = 'uuu-UU-rrr-RRR-rr!'
