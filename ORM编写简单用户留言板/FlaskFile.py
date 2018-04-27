from flask import Flask
from flask import request
from flask import  render_template
from  flask import  redirect
app = Flask(__name__)
#from db import *#导入db.py中的方法，即使用函数
from model import *#导入模块中的方法
import wtforms#引用flask表单的附加类

'''
使用了如下概念：
1，ORM的概念:对象关系映射（数据库进阶）
2，使用Flask-SQLAlchemy扩展
3，flask表单扩展，即wtforms类方法
4，flask中的redirect方法
5，flask中的render_template方法
6，flask中的request方法来获取前端页面的表单
'''

class LoginForm(wtforms.Form):#继承From的函数，为登录的表单
    username =wtforms.StringField('username',[wtforms.validators.DataRequired()])#文本框类型
    password = wtforms.PasswordField('password',[wtforms.validators.DataRequired()])#密码框类型

class PublishForm(wtforms.Form):#继承From的函数,为留言板的表单
    content =wtforms.StringField('content',[wtforms.validators.DataRequired()])#文本框类型
    sender = wtforms.StringField('sender',[wtforms.validators.DataRequired()])#文本框类型

@app.route('/',methods=['GET','POST'])

def login():
    myForm = LoginForm(request.form)
    if request.method=='POST':#确定表单提交方式为POST
        u = User(myForm.username.data,myForm.password.data)
        if u.isExisted():#导入model中的isExisted方法判断数据库中是否含有此用户
                    #确定表单提交的用户名字以及密码存储在了数据库中
                print('登录成功！正在跳转留言板页面')
                return  redirect('http://127.0.0.1:8000/show')#返回一个网页，即url页面
            #else:
                #message='who are you?'
                #return render_template('index.html',message=message,form=myForm)#返回message信息，注意要在html文件中修改相应html代码
        else:
            print('该用户未注册或者账号密码错误!')
            return redirect('http://127.0.0.1:8000/register')
    return  render_template('index.html',form=myForm)#引用templates文件夹的html文件

@app.route('/register',methods=['GET','POST'])

def register():
    myForm = LoginForm(request.form)
    if request.method=='POST':
        u = User(myForm.username.data,myForm.password.data)
        if u.isExisted()!=1:
            u.add()
            print( '注册成功！')
            return redirect('http://127.0.0.1:8000/')
        else:
            print('该用户已经注册！')
            return redirect('http://127.0.0.1:8000/')
    return render_template('register.html',form=myForm)

@app.route("/show",methods=['POST','GET'])

def show():
    myEntryForm = PublishForm(request.form)#request获取表单
    l = getAllEntry()
    if request.method=='POST':
        e = Entry(myEntryForm.content.data,myEntryForm.sender.data)
        e.add()
        return render_template('content.html',entries=l,form = myEntryForm)#将L和表单作为参数，传入到两个页面中
    return render_template('content.html',entries = l,form = myEntryForm)

if __name__ == '__main__':
    app.run(port=8000,debug=True,threaded=True)#python自带的服务器，设置端口号为8000
    #debug代表打开了调试模式，在生产中不推荐使用
    #threaded代表打开了flask的多线程模式