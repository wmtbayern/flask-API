from flask_restful import Api

from app.apis.GoodsApi import GoodsApi
from app.apis.LoginApi import LoginApi
from app.apis.LunboApi import LunboApi
from app.apis.RegisterApi import Register

api=Api()

def init_apis(app):
    #这里是api的初始化
    api.init_app(app)



api.add_resource(Register, '/api/v1/register/',endpoint='register')
api.add_resource(LoginApi, '/api/v1/login/',endpoint='login')
api.add_resource(GoodsApi,'/api/v1/goods/',endpoint='goods')
api.add_resource(LunboApi,'/api/v1/banners/',endpoint='banners')
