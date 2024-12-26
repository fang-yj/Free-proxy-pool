from tkinter import messagebox
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests
import os
from function.qu_can_shu import proxy_list_table


# http1 = 'https://openproxy.space/list/http'
http2 = 'https://www.proxy-list.download/HTTP'

def anniu(canshu,update_pro_bar):
    print('计算数据中....')
    if canshu == 'http(https)':

        update_pro_bar(0)
        response = requests.get(http2, headers=headers, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        response.encoding = response.apparent_encoding  # 设置编码
        # time.sleep(3)
        update_pro_bar(30)
        soup = BeautifulSoup(response.text, "html.parser")
        to = proxy_list_table(soup)

        update_pro_bar(90)
        print(to)
        lines = []
        for item in to:
            if len(item) >= 2:  # 确保每组数据至少有两个元素可提取
                combined_info = f"{item[0]}:{item[1]}"
                lines.append(combined_info)
        # 检查output目录是否存在，不存在则创建
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 将处理后的数据逐行写入到http_or_https.txt文件中
        file_path = os.path.join(output_dir, "http_or_https.txt")
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
        messagebox.showwarning("ok~", "信息存放在了output/http_or_https.txt文件了！")
        update_pro_bar(100)

    elif canshu == 'socks4':
        print(canshu)
    elif canshu =='socks5':
        print(canshu)
    else:
        print('你确定有这个代理池?')
        messagebox.showerror('错误','恩?你确定有这个代理池?')


headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}