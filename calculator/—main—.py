#calculater简易计算器
from tkinter import  *

#以定义适合的函数来创建框架和更简洁的按钮为开始，用一些只读函数来代替一些常用代码。
def frame(root,side):
    w = Frame(root)
    w.pack(side=side,expand = YES,fill = BOTH)
    return  w


def button(root,side,text,command=None):
    w = Button(root,text = text , command = command)
    w.pack(side = side, expand = YES, fill = BOTH)
    return  w


class Calculator(Frame):#
    def __init__(self):#调用父类Frame的构造方法
        Frame.__init__(self)
        self.pack(expand = YES ,fill = BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calcl")

        display = StringVar()
        Entry(self,relief = SUNKEN,textvariable = display).pack(side = TOP ,expand = YES, fill = BOTH)

        for key in ("123", "456","789", "-0."):
            keyF =frame(self,TOP)
            for char in key:
                button(keyF,LEFT,char, lambda  w = display, s ='%s'%char: w.set(w.get()+s))


        opsF = frame(self,TOP)
        for char in  "+-*/=":
            if char == '=':
                btn = button(opsF,LEFT,char)
                btn.bind('<ButtonRelease-1>',lambda  e, s=self, w=display : s.calc(w), '+')
            else:
                btn = button(opsF,LEFT,char,lambda  w = display, c=char: w.set(w.get()+''+c+''))

        clearF = frame(self,BOTTOM)
        button(clearF, LEFT, 'Clr',lambda  w =display: w.set(''))

    def calc(self,display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    Calculator().mainloop()

