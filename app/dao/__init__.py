from app.models.user import User
from app.models import db
from app import pity

with pity.app_context():
    db.create_all()