
from flask_restful import Resource, fields, marshal_with
from app.models import Goods


"""
需要返回的数据的示例
{
    'msg':'获取商品信息成功'
    'count':1,
    'data':{
        'id':1,
        'img':'/static/images2/2-1.jpg'
        'detail':'XXX',
        'price':'111',
    }
}
这个是客户端要返回的数据格式
"""
class ImgFormat(fields.Raw):
    def Format(self,value):
        return '/static/images2/' + value

goods_fields={
    'id':fields.Integer,
    'img': ImgFormat(attribute='img'),
    'detail':fields.String,
    'price':fields.Integer,
}
result_fields={
    'msg':fields.String,
    'total':fields.Integer,
    'data':fields.Nested(goods_fields),
}

class GoodsApi(Resource):
    # 要格式化输出,就要用到这个装饰器,参数是上面定制的格式
    @marshal_with(result_fields)
    def get(self):
        goods=Goods.query.all()
        response_data={
            'msg':'获取商品列表成功',
            'total':len(goods),
            'data':goods,
        }
        return response_data
