from flask import Flask
from app.config import Config
from app.database import db
from app import models

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

from app import routes
