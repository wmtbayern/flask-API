
class BaseConfig(object):
    SECRET_KEY = 'CNKSAJHF%$##@#$%^&*()ncak213iu43247@#$%%E#%&^'
    DEBUG = False
    TESTING = False
    SESSION_TYPE = 'redis'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@127.0.0.1:3306/flaskdemo2'
 #邮箱配置(要先在邮箱那边设置客户端授权码为开启)
    MAIL_SERVER='smtp.163.com'
    #邮箱名字
    MAIL_USERNAME='wmt_bayern19@163.com'
    #这个是授权的密码,不是邮箱的登陆密码
    MAIL_PASSWORD='wangmt260112789'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@127.0.0.1:3306/flaskdemo2'


class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@127.0.0.1:3306/flaskdemo2'


class ProductConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@127.0.0.1:3306/flaskdemo2'


config={

    'develop':DevelopConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'product':ProductConfig,
    'default':DevelopConfig,

}


def init_app(app,env_name):
    app.config.from_object(config.get(env_name))