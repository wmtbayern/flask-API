from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()
migrate=Migrate()
sess=Session()
#减少数据库或者文件的IO操作,提高性能,减少耗时
# 配置   传入两个参数,第一个是app 另一个是config
cache=Cache(config={
    'CACHE_TYPE': 'redis'
})
mail=Mail()
#cache.cached(timeout=80)
# cache.set(key,value,timeout)
#value=cache.get(key)
api = Api()


def init_ext(app):
    db.init_app(app)
    sess.init_app(app)
    migrate.init_app(app=app,db=db)
    Bootstrap(app)
    cache.init_app(app)
    #toolbar = DebugToolbarExtension(app)  DEBUG=True才可以用
    api.init_app(app)
    mail.init_app(app)