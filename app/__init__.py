from flask import Flask
from .config import Config
from .database import db
from .models import User, Appointment

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

from app import routes
