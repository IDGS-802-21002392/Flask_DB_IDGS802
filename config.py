import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY='CLAVE_SECRETA'
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:1234@127.0.0.1/bdidgs802'
