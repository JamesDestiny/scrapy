import tkinter as tk
import  pymysql
import tkinter.messagebox
from tkinter import  ttk

win = tk.Tk()
win.title('通讯录')
win.geometry('600x400')



menubar = tk.Menu(win)#新建菜单条
win.config(menu =menubar)
menu1 = tk.Menu(menubar,tearoff = False)#创建一个菜单选项新建
menu2 = tk.Menu(menubar,tearoff = False)#删除选项菜单
menu3 = tk.Menu(menubar,tearoff = False)#查找选项菜单
menu4 = tk.Menu(menubar,tearoff = False)#显示所有选项菜单

tree = ttk.Treeview(win)
#定义列
tree["columns"]=("name","number","address")
#设置列,和元组内容一致
tree.column("name",width=100)
tree.column("number",width=100)
tree.column("address",width=200)

#设置表头,和元组内容也要保持一致
tree.heading("name",text= "name")
tree.heading("number",text= "number")
tree.heading("address",text= "address")

name = tk.StringVar(value='')  # 键盘输入菜单获得姓名,设置默认内容为空
number = tk.StringVar(value='')  # 输入获得电话号码
address = tk.StringVar(value='')  # 输入获得地址
l1 = tk.Label(win,text = '新建联系人',font = ('微软雅黑',20),anchor = 'center')#创建新建联系人标签
l2 = tk.Label(win,text = '姓名:',font = ('微软雅黑',12),anchor = 'center')#创建姓名标签
l3 = tk.Label(win,text = '号码:',font = ('微软雅黑',12),anchor = 'center')#创建号码标签
l4 = tk.Label(win,text = '地址:',font = ('微软雅黑',12),anchor = 'center')#创建地址标签
l5 = tk.Label(win,font =('微软雅黑,12'),anchor ='center')#创建可变标签待用
entry_name = tk.Entry(win, textvariable=name)#创建输入框，传值给name对象
entry_number = tk.Entry(win, textvariable=number)#创建输入框，传值给number对象
entry_address = tk.Entry(win, textvariable=address)#创建输入框，传值给number对象
button1 = tk.Button(win, text='确认')
cv = tk.Canvas(win,bg='white',height=400,width=600)#创建画布
cv.pack()
mytext = cv.create_text(280,190,text ='简易通讯录v1.0\n',font=('微软雅黑','38'),fill ='black')
text =cv.create_text(280,380,text='温馨提示：第一次使用需先建表',font=('微软雅黑','16'),fill='red')
host = tk.StringVar()
user =tk.StringVar()
password =tk.StringVar()
databases =tk.StringVar()

def crate_toplevel(host=host,user=user,password =password,databases=databases):#创建顶级窗口来显示连接数据库界面
    toplevel = tk.Toplevel()
    toplevel.title('连接数据库')
    toplevel.geometry('300x260')
    L1=tk.Label(toplevel,text='连接数据库',font=('微软雅黑',16),anchor = 'center').pack(side=tk.TOP)
    L2=tk.Label(toplevel,text='host:').place(x=30,y=50)
    L3=tk.Label(toplevel,text='user:').place(x=30,y=90)
    L4=tk.Label(toplevel,text='password:').place(x=30,y=130)
    L5=tk.Label(toplevel,text='databases:').place(x=30,y=170)
    E1=tk.Entry(toplevel,textvariable=host).place(x=100,y=50)
    E2=tk.Entry(toplevel,textvariable=user).place(x=100,y=90)
    E3=tk.Entry(toplevel,textvariable=password,show='*').place(x=100,y=130)
    E4=tk.Entry(toplevel,textvariable=databases).place(x=100,y=170)
    toplevel.pack_slaves()
    toplevel.wm_attributes('-topmost',1)#将toplevel窗口置于顶层
    def destory_toplevel():#将toplevel窗口销毁，并且返回数据库连接成功的消息
        toplevel.destroy()
        tk.messagebox.showinfo(title='成功', message='连接成功！')
    button = tk.Button(toplevel,text='确认',command=destory_toplevel)
    button.pack(side=tk.BOTTOM)

def creat_table():
    if (host.get()!='')&(user.get()!='')&(password.get()!='')&(databases.get()!=''):
        try:
            sql = "create table if not exists Person(" \
                  "Person_id INT unsigned auto_increment," \
                  "Person_name VARCHAR(255) NOT NULL ," \
                  "Person_phonenumber VARCHAR(255) NOT NULL ," \
                  "Person_address VARCHAR(255) NOT NULL ," \
                  "PRIMARY KEY (Person_id))" \
                  "engine = Innodb DEFAULT  charset = utf8;"  # 创建新表Person来存储通讯录里的联系人数据
            # 在表中存储中文时应该添加  CHARACTER SET utf8 COLLATE utf8_unicode_ci 否则编码不正确
            db = pymysql.connect(host=host.get(), user=user.get(), passwd=password.get(),
                                 db=databases.get())  # 打开数据库连接设置charset为utf8编码
            cursor = db.cursor()  # 使用cursor方法创建一个游标对象 cursor
            cursor.execute(sql)
            db.commit()  # 提交到数据库执行
            cursor.close()
            db.close()
            tk.messagebox.showinfo(title='成功',message='建表成功')
        except:
            tk.messagebox.showerror(title='error',message='建表失败')
    else:
        tk.messagebox.showerror(title='error',message='请先连接数据库')
        delete_wdights()
        cv.pack()
        crate_toplevel()
def delete_wdights(l1=l1,l2=l2,l3=l3,name =name,number=number,address=address,tree=tree,button1=button1,cv=cv):#消除所有控件，对窗口实现刷新功能
    l1.place_forget()
    l2.place_forget()
    l3.place_forget()
    l4.place_forget()
    entry_number.place_forget()
    entry_address.place_forget()
    entry_name.place_forget()
    button1.place_forget()
    tree.pack_forget()
    cv.pack_forget()


def insert_person(l1=l1,l2=l2,l3=l3,name =name,number=number,address=address,tree=tree,button1=button1,cv=cv,host=host,user=user,password=password,databases=databases):
    delete_wdights()
    l1.config(text='新建联系人')
    l1.place(x=240,y=20)#将标签布局到窗口顶部
    l2.place(x=180,y=100)#对3个标签进行布局
    l3.place(x=180,y=150)
    l4.place(x=180,y=200)
    entry_name.place(x=230,y=100)#对3个输入框进行布局
    entry_number.place(x=230,y=150)
    entry_address.place(x=230,y=200)
    name.set('')
    number.set('')
    address.set('')
    def play_1():#设置操作函数，来使点击button后可以来执行函数
        if (host.get()!='')&(user.get()!='')&(password.get()!='')&(databases.get()!=''):
            if (name.get()!='')&(number.get()!='')&(address.get()!=''):
                try:
                    sql = "insert into Person(Person_name,Person_phonenumber,Person_address) " \
                          "VALUES ('%s','%s','%s');" % (name.get(), number.get(), address.get())
                    db = pymysql.connect(host=host.get(), user=user.get(), passwd=password.get(),
                                         db=databases.get())  # 打开数据库连接设置charset为utf8编码
                    cursor = db.cursor()  # 使用cursor方法创建一个游标对象 cursor
                    cursor.execute(sql)
                    db.commit()  # 提交到数据库执行
                    cursor.close()
                    db.close()
                    tk.messagebox.showinfo(title='成功',message='新建联系人成功！')
                    delete_wdights()  # 对窗口实现刷新效果
                    cv.pack()
                except  Exception as e:
                    tk.messagebox.showinfo(title='失败',message='失败类型'+str(e))
                    delete_wdights()  # 对窗口实现刷新效果
                    cv.pack()
            else:
                tk.messagebox.showerror(title='error',message='请输入有效信息！')
                delete_wdights()  # 对窗口实现刷新效果
                cv.pack()
        else:
            tk.messagebox.showerror(title='error',message='请先连接数据库')
            delete_wdights()
            cv.pack()
            crate_toplevel()
    button1.config(command =play_1)
    button1.place(x=280,y=260)#对按钮button进行布局




def delete_person(l1=l1,l2=l2,l3=l3,l4=l4,name=name,number =number,address=address,tree=tree,button1=button1,cv=cv,host=host,user=user,password=password,databases=databases):
    delete_wdights()
    l1.config(text='删除联系人')  # 创建新建联系人标签
    l1.place(x=240, y=20)  # 将标签布局到窗口顶部
    l2.place(x=180, y=100)  # 对姓名标签进行布局
    entry_name.place(x=230, y=100)
    def play_2():
        if (host.get() != '') & (user.get() != '') & (password.get() != '') & (databases.get() != ''):
            if name.get()!='':
                try:
                    sql = '''delete from Person
                          where Person_name = "%s";'''%(name.get())
                    db = pymysql.connect(host=host.get(), user=user.get(), passwd=password.get(),
                                         db=databases.get())  # 打开数据库连接设置charset为utf8编码
                    cursor = db.cursor()  # 使用cursor方法创建一个游标对象 cursor
                    cursor.execute(sql)
                    db.commit()  # 提交到数据库执行
                    cursor.close()
                    db.close()
                    tk.messagebox.showinfo(title='成功',message='删除联系人成功！')
                    delete_wdights()
                    cv.pack()
                except Exception as e:
                    tk.messagebox.showinfo(title='失败', message='失败类型' + str(e))
                    delete_wdights()  # 对窗口实现刷新效果
                    cv.pack()
            else:
                tk.messagebox.showerror(title='error',message='请输入有效的姓名！')
                delete_wdights()  # 对窗口实现刷新效果
                cv.pack()
        else:
            tk.messagebox.showerror(title='error', message='请先连接数据库')
            delete_wdights()
            cv.pack()
            crate_toplevel()
    button1.config(command = play_2)
    button1.place(x=280, y=260)  # 对按钮button进行布局



def find_person(l1=l1,l2=l2,l3=l3,l4=l4,name=name,number=number,address=address,tree=tree,button1=button1,cv=cv,host=host,user=user,password=password,databases=databases):
    delete_wdights()
    l1.config(text='查找联系人')# 创建新建联系人标签
    l1.place(x=240, y=20)  # 将标签布局到窗口顶部
    l2.place(x=180, y=100)  # 对姓名标签进行布局
    entry_name.place(x=230, y=100)
    def play_3():
        if (host.get() != '') & (user.get() != '') & (password.get() != '') & (databases.get() != ''):
            if name.get()!='':
                try:
                    db = pymysql.connect(host=host.get(), user=user.get(), passwd=password.get(), db=databases.get())  # 打开数据库连接设置charset为utf8编码
                    cursor = db.cursor()  # 使用cursor方法创建一个游标对象 cursor
                    cursor.execute('''select * from Person
                                where Person_name = "%s";''' % (name.get()))  # 使用execute方法执行sql查询
                    db.commit()  # 提交到数据库执行
                    rs = cursor.fetchall()
                    for row in rs:
                        phone = row[2]
                        add = row[3]
                        tk.messagebox.showinfo(title='成功',message='姓名:'+name.get()+' 号码：'+phone+' 地址：'+add)
                    cursor.close()
                    db.close()
                    delete_wdights()
                    cv.pack()
                except Exception as e:
                    tk.messagebox.showinfo(title='失败', message='查无此人！')
                    delete_wdights()
                    cv.pack()
            else:
                tk.messagebox.showerror(title='error',message='请输入有效的姓名！')
                delete_wdights()
                cv.pack()
        else:
            tk.messagebox.showerror(title='error', message='请先连接数据库')
            delete_wdights()
            cv.pack()
            crate_toplevel()
    button1.config(command=play_3)
    button1.place(x=280, y=260)  # 对按钮button进行布局

def find_all_person(tree = tree,l1=l1,l2=l2,l3=l3,l4=l4,name=name,number=number,address=address,button1=button1,cv=cv,host=host,user=user,password=password,databases=databases):
        delete_wdights()
        if (host.get() != '') & (user.get() != '') & (password.get() != '') & (databases.get() != ''):
            try:
                db = pymysql.connect(host=host.get(), user=user.get(), passwd=password.get(), db=databases.get())  # 打开数据库连接设置charset为utf8编码
                cursor = db.cursor()  # 使用cursor方法创建一个游标对象 cursor
                cursor.execute("select * from Person;" )  # 使用execute方法执行sql查询
                db.commit()  # 提交到数据库执行
                rs = cursor.fetchall()
                conter =0
                if tree.get_children()==():
                    for row in rs:
                        name = row[1]
                        phone = row[2]
                        add = row[3]
                        # 添加数据,第二个参数为添加行数的下标，text参数为待插入行的开头
                        tree.insert("", 0, text="line"+str(conter), values=(name,phone,add))
                        conter+=1
                    tree.pack()
                else:
                    tree.pack()
                cursor.close()
                db.close()
            except:
                tk.messagebox.showinfo(title='error',message='失败')
                cv.pack()
        else:
            tk.messagebox.showerror(title='error', message='请先连接数据库')
            delete_wdights()
            cv.pack()
            crate_toplevel()
        def func():
            tree.pack_forget()
            cv.pack()
        button1.config(command =func)#确认按钮进行清屏
        button1.place(x=280,y=260)

def menu(char,menup):
    for item in [char]:#给菜单增加选项内容
        if item == '新建联系人':
            menup.add_command(label = item,command = insert_person)
        elif item == '删除联系人':
            menup.add_command(label=item, command = delete_person)
        elif item == '查找联系人':
            menup.add_command(label=item, command = find_person)
        elif item == '显示所有联系人':
            menup.add_command(label=item, command = find_all_person)

menu('新建联系人',menu1)
menu('删除联系人',menu2)
menu('查找联系人',menu3)
menu('显示所有联系人',menu4)
def funct():
    tk.messagebox.showinfo(title='关于:',message='from：James/简易通讯录v1.0')

menubar.add_cascade(label = '新建',menu = menu1)
menubar.add_cascade(label = '删除',menu = menu2)
menubar.add_cascade(label = '查找',menu = menu3)
menubar.add_cascade(label = '显示',menu = menu4)
menubar.add_command(label = '退出',command = win.quit)
menubar.add_command(label='建表',command=creat_table)
menubar.add_command(label = '关于',command = funct)

if __name__=='__main__':
    crate_toplevel()
    win.mainloop()
