from tkinter import *
from tkinter import ttk
import subprocess
import time


class Application(Frame):
    date = time.strftime('%Y/%m/%d  ')
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """设置所有窗体小部件"""
        self.lb1 = Label(self, text='Python体验课').grid(row=0, column=0, sticky=W)
        self.lb2 = Label(self, text='时间：').grid(row=1, column=0, sticky=W)
        self.entry1 = Entry(self, borderwidth=2)
        self.entry1.insert(END, self.date)
        self.entry1.grid(row=1, column=1, columnspan=2, sticky=W, pady=2)

        self.lb3 = Label(self, text='人数：').grid(row=2, column=0, sticky=W)
        self.cmb1 = ttk.Combobox(self, value=('1', '2', '3', '4', '5', '6', '7', '8'))
        self.cmb1.grid(row=2, column=1, sticky=W, pady=2)

        self.lb4 = Label(self, text='【1】姓名：').grid(row=3, column=0, sticky=W)
        self.entry2 = Entry(self, borderwidth=2)
        self.entry2.grid(row=3, column=1, sticky=W, pady=2)

        self.lb5 = Label(self, text='【2】年龄：').grid(row=4, column=0, sticky=W)
        self.cmb2 = ttk.Combobox(self, value=('7岁','8岁','9岁','10岁','11岁','12岁','13岁','14岁','15岁'))
        self.cmb2.grid(row=4,column=1, sticky=W, pady=2)
        self.cmb3 = ttk.Combobox(self, value=('二年级', '三年级', '四年级', '五年级', '六年级','初一', '初二', '初三', '高一'))
        self.cmb3.grid(row=4,column=2, sticky=W, pady=2)

        self.lb6 = Label(self, text='【3】编程基础：').grid(row=5, column=0, sticky=W)
        self.cmb4 = ttk.Combobox(self, value=('无','计算机入门', 'c/c++', 'scratch', 'java', 'python', 'web', '其他语言'))
        self.cmb4.grid(row=5,column=1, sticky=W, pady=2)
        self.cmb5 = ttk.Combobox(self, value=('小于半年', '一年', '两年', '三年','大于三年'))
        self.cmb5.grid(row=5,column=2, sticky=W, pady=2)

        self.lb7 = Label(self,text='【4】爱好：').grid(row=6, column=0, sticky=W)
        self.entry3 = Entry(self, borderwidth=2)
        self.entry3.grid(row=6, column=1, sticky=W, pady=2)

        self.lb8 = Label(self, text='【5】电脑操作：').grid(row=7, column=0, sticky=W)
        self.cmb6 = ttk.Combobox(self, value=('超级烂', '很慢，错误较多', '很慢，但是没什么错误', '一般速度', '非常熟练'))
        self.cmb6.grid(row=7, column=1, sticky=W, pady=2)

        self.lb9 = Label(self,text='【6】课上表现：').grid(row=8, column=0, sticky=W)
        self.txt1 = Text(self, width=50, height=4, wrap=WORD, borderwidth=2)
        self.txt1.grid(row=8, column=1, columnspan=2, sticky=W, pady=2)

        self.lb10 = Label(self,text='【7】家庭背景：').grid(row=9, column=0, sticky=W)
        self.txt2 = Text(self, width=50, height=3, wrap=WORD, borderwidth=2)
        self.txt2.grid(row=9, column=1, columnspan=2, sticky=W, pady=2)

        self.lb11 = Label(self,text='【8】备注：').grid(row=10, column=0, sticky=W)
        self.txt3 = Text(self,width=50,height=4,wrap=WORD, borderwidth=2)
        self.txt3.grid(row=10,column=1,columnspan=2,sticky=W, pady=2)

        self.btn1 = Button(self,text='添加', command=self.update_stu_info)
        self.btn1.grid(row=11, column=0, sticky=W+E+N+S, pady=2)
        self.btn2 = Button(self,text='清除all', command=self.clear_all_stu_info).grid(row=11, column=1,sticky=W+E+N+S, pady=2)
        self.btn3 = Button(self, text='显示内容', command=self.show_txt).grid(row=11, column=2, sticky=W+E+N+S, pady=2)

    def clear_all_stu_info(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.txt1.delete(0.0, END)
        self.txt2.delete(0.0, END)
        self.txt3.delete(0.0, END)
        self.cmb1.delete(0, END)
        self.cmb2.delete(0, END)
        self.cmb3.delete(0, END)
        self.cmb4.delete(0, END)
        self.cmb5.delete(0, END)
        self.cmb6.delete(0, END)

    def update_stu_info(self):
        """添加学员信息函数"""
        all_stu_info = self.get_stu_info()
        with open('d:\\test.txt','a',encoding='utf-8') as f:
            # for i in f.readlines():
            #     print(i.encode('utf-8').decode('utf-8'),end='')
            for line in all_stu_info:
                f.write(line)

    def show_txt(self):
        """显示文件"""
        # f = os.system('d:\\test.txt')
        #subprocess.run('d:\\test.txt',shell=True)
        subprocess.Popen('d:\\test.txt',shell=True)

    def get_stu_info(self):
        """获取学生信息，返回一个列表"""
        info_list = []
        num = self.cmb1.get()
        if num:
            info_list.append('\nPython体验课')
            info_list.append('\n时间：'+self.entry1.get())
            info_list.append('\n人数：'+self.cmb1.get())
            info_list.append('\n【1】姓名：'+self.entry2.get())
            info_list.append('\n【2】年龄：'+self.cmb2.get()+self.cmb3.get())
            info_list.append('\n【3】编程基础：'+self.cmb4.get()+self.cmb5.get())
            info_list.append('\n【4】爱好：'+self.entry3.get())
            info_list.append('\n【5】电脑操作：'+self.cmb6.get())
            info_list.append('\n【6】课上表现：'+self.txt1.get(0.0, END))
            info_list.append('【7】家庭背景：'+self.txt2.get(0.0, END))
            info_list.append('【8】备注：'+self.txt3.get(0.0, END))
        else:
            info_list.append('\n【1】姓名：'+self.entry2.get())
            info_list.append('\n【2】年龄：'+self.cmb2.get()+self.cmb3.get())
            info_list.append('\n【3】编程基础：'+self.cmb4.get()+self.cmb5.get())
            info_list.append('\n【4】爱好：'+self.entry3.get())
            info_list.append('\n【5】电脑操作：'+self.cmb6.get())
            info_list.append('\n【6】课上表现：'+self.txt1.get(0.0, END))
            info_list.append('【7】家庭背景：'+self.txt2.get(0.0, END))
            info_list.append('【8】备注：'+self.txt3.get(0.0, END))
        return info_list


root= Tk()
root.title('学员信息输入小程序^_^')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry('460x420+%d+%d'%(screen_width/2-230,screen_height/2-280))
root.resizable(0,0)

app = Application(root)
root.mainloop()
