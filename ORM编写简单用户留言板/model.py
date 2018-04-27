# model.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#定义数据库连接协议，输入数据库的user和password，然后选择主机号和数据库,注意这是python3的连接方式，加上了’+pymysql‘语句
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:919398@localhost:3306/test?charset=utf8mb4"
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = True


db = SQLAlchemy(app)#利用SQLAlchemy为我们提供好的app封装对象

#定义一个user类，继承了Model类
class User(db.Model):
    #第一个成员变量id，是数据库中的一个字段，整形变量，并且为主键
    id = db.Column(db.Integer,primary_key=True)
    #第二个变量为username，unique代表该变量不能重复，即该用户名不能重复
    username= db.Column(db.String(32),unique=True)
    #第三个变量为password
    password = db.Column(db.String(32))

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def add(self):#将用户数据插入到数据库中
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

    def isExisted(self):#query为查询，返回第一个结果，如果为空返回0，如果为非空，返回1
        temUser = User.query.filter_by(username = self.username,password=self.password).first()#判断用户名和密码是否在数据库中存在
        if temUser is None:
            return 0
        else:
            return 1

#定义一个Entry类，代表用户输入的留言信息，继承Mode类
class Entry(db.Model):
    #第一个成员变量为id，是数据库中的一个字段，为整型变量，为主键
    id = db.Column(db.Integer,primary_key=True)
    #第二个成员变量为content，为text类型，代表用户输入的留言内容
    content = db.Column(db.Text)
    #第三个成员变量为sender,为字符串类型，代表留言的用户的username
    sender = db.Column(db.String(32))

    #编写类的构造函数,传入content和sender内容
    def __init__(self,content,sender):
        self.content = content
        self.sender = sender

    #编写添加函数add（），即添加用户留言板的内容函数
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            db.session.rollback()
            return e
        finally:
            return 0

#编写方法getAllEntry()，输出所有的Entry
def getAllEntry():
    Enlist = []#定义一个数组来保存所有entry内容
    Enlist = Entry.query.filter_by().all()#query.filter_by().all()为查询所有的功能
    return Enlist#返回数组entry