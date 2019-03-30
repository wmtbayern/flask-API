
from flask_restful import Resource, fields, marshal_with
from app.models import Banner

"""
需要返回的数据的示例
{
    'msg':'获取商品信息成功'
    'data':{
        'id':1,
        'img':'/static/images/2-1.jpg'
    }
}
这个是客户端要返回的数据格式
"""
class ImgFormat(fields.Raw):
    def Format(self,value):
        return '/static/images/' + value

goods_fields={
    'id':fields.Integer,
    'img': ImgFormat(attribute='img'),

}
result_fields={
    'msg':fields.String,
    'status':fields.Integer,
    'total':fields.Integer,
    'data':fields.Nested(goods_fields),
}

class LunboApi(Resource):
    # 要格式化输出,就要用到这个装饰器,参数是上面定制的格式
    @marshal_with(result_fields)
    def get(self):
        banners=Banner.query.all()
        response_data={
            'msg':'获取轮播图成功',
            'status':200,
            'total':len(banners),
            'data':banners,
        }
        return response_data
