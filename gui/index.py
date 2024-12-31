import tkinter
from tkinter import ttk
from tkinter import *
from function import tools
from tkinter import messagebox

def index1():
    #创建窗口
    rt = Tk()
    rt.title('代理池   V1.0.1 --作者:杨CC')
    rt.iconbitmap('img/icon.ico')
    rt.geometry('350x425')
    # rt.resizable(False,False)

    #整个标签提示
    lab = Label(rt,text='请在下方选择你需要的代理池')
    lab.pack(pady=10)

    #设置一些参数
    opt = ['http(https)','socks4(暂不可用)','socks5(暂不可用)']
    #下拉菜单
    com_box = ttk.Combobox(rt)
    com_box['values'] = opt
    #设置下拉的第一个参数
    com_box.current(0)
    com_box.pack(pady=50)

    #整个按钮
    yes_anniu = Button(rt,text='获取信息')
    def update_pro_bar(progress_value):
        progress_bar['value'] = progress_value
        rt.update_idletasks()

    yes_anniu['command'] = lambda: tools.anniu(com_box.get(),update_pro_bar)
    yes_anniu.pack()

    #添加个说明!1
    lab2 = Label(rt,text='这里是一个简单的说明\n先下载curl!先下载curl!先下载curl!\nWIndows打开浏览器访问:https://curl.se/download.html\nLinux自带\nMacos自行寻找下载\n因为最近比较忙,所以更新比较慢\n初步只支持获取60个(后续逐步增加)')
    lab2.pack(pady=30)

    # 弄个进度条
    progress_bar = ttk.Progressbar(rt, orient=tkinter.HORIZONTAL, length=450, mode='determinate')
    progress_bar.pack()

    #整个提示
    messagebox.showinfo("紧急通知!", "当前版本:V1.0.1\n更新内容:\n1.更换了http和https协议的接口\n2.因为接口会限制速率,所以请各位获取信息以后,间隔五分钟后再获取!\n3.因为软件为初步版本,所以暂时我只写了获取60个IP池,如需要更多请更待后续更新!\n4.请夸一夸作者~如果可以的话,请给作者买杯咖啡~")
    mainloop()

    return ''