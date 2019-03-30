
import uuid

from flask_restful import Resource, reqparse,fields,marshal_with
from werkzeug.security import check_password_hash

from app.exts import cache
from app.models import User

parser=reqparse.RequestParser()

parser.add_argument('phone',type=int,required=True,help='请输入手机号')
parser.add_argument('password',type=str,required=True,help='请输入密码')
"""
请求信息的定制
'msg':'登陆成功',
'status':200,
'user':user,
'token':token,

"""

user_fields={
    'phone':fields.Integer,
    'email':fields.String

}
result_fields={
         #这里的 key 就是返回给客户端的  key 可以自定义
        'msg':fields.String,
        'status':fields.Integer,
        'user':fields.Nested(user_fields,default={}),
        'token':fields.String,
}

class LoginApi(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse=parser.parse_args()
        phone=parse.get('phone')
        password=parse.get('password')
        #各个情况下都要显示的字段,可以放到外面
        response_data={
            'status':406,
            'user':''
        }
        users=User.query.filter(User.phone==phone)
        if users.count():#存在
            user=users.first()
            if check_password_hash(user.password,password):

                token=uuid.uuid5(uuid.uuid4(),'login').hex
                cache.set(token,user.id,timeout=60*60*7)

                response_data['msg']='登陆成功'
                response_data['status']=200
                response_data['user']=user
                response_data['token']=token
                return response_data

            else:
                response_data['msg']='登陆失败,密码错误'
                return response_data
        else:  #用户不存在
            response_data['msg']='登陆失败,用户不存在'
            return response_data
