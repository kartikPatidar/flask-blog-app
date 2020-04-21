import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # to prevent CSRF attack we create SECRET_KEY(flask-wtf extension uses it to implement hidden_tag())
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # sqlalchemy extension uses database location from line below
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' +os.path.join(basedir, 'app.db')
    # so that flask-sqlalchemy do not send signal when changes are about to be made in database.
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    