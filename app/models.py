from app.exts import db


class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img= db.Column(db.String(255))


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img= db.Column(db.String(255))
    detail = db.Column(db.String(255))
    price = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(500))
    email = db.Column(db.String(80), unique=True)