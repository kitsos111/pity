from flask import Flask
from Config import Config
from app.controller.auth.user import auth
pity=Flask(__name__)
pity.config.from_object(Config)
pity.register_blueprint(auth)
