import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-or-would-you?'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///predictive_analytics.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
