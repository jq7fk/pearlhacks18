import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or 'you-will-never-guess'