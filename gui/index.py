import tkinter
from tkinter import ttk
from tkinter import *
from function import tools

def index1():
    #创建窗口
    rt = Tk()
    rt.title('代理池   --作者:杨CC')
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
    lab2 = Label(rt,text='这里是一个简单的说明\n注意:此工具界面方便,简洁,\n但是相对而言因为是可视化的初步代码,\n所以可能会有一些卡顿或bug,请各位及时提醒\n还有!先下载curl!先下载curl!先下载curl!\nWIndows打开浏览器访问:https://curl.se/download.html\nLinux自带\nMacos自行寻找下载')
    lab2.pack(pady=30)

    # 弄个进度条
    progress_bar = ttk.Progressbar(rt, orient=tkinter.HORIZONTAL, length=450, mode='determinate')
    progress_bar.pack()

    mainloop()

    return ''