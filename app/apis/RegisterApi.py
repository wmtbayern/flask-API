import uuid
from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash
from app.exts import db, cache, mail
from app.models import User


parser=reqparse.RequestParser()
parser.add_argument('phone',type=str,required=True,help='输入合法的手机号')
parser.add_argument('password',type=str,required=True,help='输入4-20位的密码')
parser.add_argument('email',type=str,required=True,help='输入合法的邮箱')

""""
响应的格式
'msg':'注册成功',
'status':'200',
'user':{
    'phone':XXXX,
    'email':'XXXX',
}
'token':'token',
"""
user_fields={
    'phone':fields.String,
    'email':fields.String,
}

result_field={
'msg':fields.String,
'status':fields.Integer,
'user':fields.Nested(user_fields,default={}),
'token':fields.String,
}

class Register(Resource):
    @marshal_with(result_field)  #字段的限制约束
    def post(self):
        parse=parser.parse_args()
        user=User()
        #拿到相应的值存入数据库
        user.phone=parse.get('phone')
        user.password=generate_password_hash(parse.get('password'))
        user.email=parse.get('email')

        #每个返回信息都有的部分,写在外面
        response_data={}

        # 分情况处理返回的数据
        #需要验证手机和邮箱,提示是否被占用
        response_data['status']=406
        response_data['user']=''
        users=User.query.filter(User.phone==user.phone)
        if users.count(): #用户存在的情况
            # #设置返回的信息
            response_data['msg']='该手机号已被注册'
            #没有设置token 返回的时候会是Null
            return response_data

        users=User.query.filter(User.email==user.email)
        if users.count():
            response_data['msg']='该邮箱已被注册'
            return response_data

        #都没有被注册才存入数据库
        db.session.add(user)
        db.session.commit()

        token=uuid.uuid5(uuid.uuid4(),'register').hex
        #设置token
        cache.set(token,user.id,timeout=60*60*7)

        #返回数据
        response_data['msg']='注册成功'
        response_data['status']=200
        response_data['token']=token
        response_data['user']=user

        return response_data