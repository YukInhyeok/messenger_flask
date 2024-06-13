import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'chat.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False