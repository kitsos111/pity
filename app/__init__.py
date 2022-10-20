from flask import Flask
from app.Config import Config

pity=Flask(__name__)
pity.config.from_object(Config)


