from tkinter import messagebox
from tkinter import filedialog
from bs4 import BeautifulSoup
import requests
import os
from.can_shu import zhan_da_ye_ip,headers,zhan_da_ye_ip2,zhan_da_ye_ip3
from.yancy_qubiaoqian1 import zhan_daye_table

import requests
from bs4 import BeautifulSoup
import os
import tkinter.messagebox as messagebox


def anniu(canshu, update_pro_bar):
    print('计算数据中....')
    if canshu == 'http(https)':
        update_pro_bar(0)
        # 先获取第一个IP对应的内容并处理
        response = requests.get(zhan_da_ye_ip, headers=headers, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        response.encoding = response.apparent_encoding  # 设置编码
        update_pro_bar(10)
        soup = BeautifulSoup(response.text, "html.parser")
        print(soup)

        print('数据在进行处理')
        to = zhan_daye_table(soup)
        update_pro_bar(30)
        print("\n输出处理后的数据\n", to)
        update_pro_bar(40)

        # 再获取第二个IP对应的内容并处理
        response2 = requests.get(zhan_da_ye_ip2, headers=headers, timeout=10)
        response2.raise_for_status()  # 检查 HTTP 状态码
        response2.encoding = response2.apparent_encoding  # 设置编码
        soup2 = BeautifulSoup(response2.text, "html.parser")
        print(soup2)
        print('数据在进行处理')
        to2 = zhan_daye_table(soup2)
        print("\n输出处理后的数据\n", to2)
        update_pro_bar(50)
        # 接着获取第三个IP对应的内容并处理
        response3 = requests.get(zhan_da_ye_ip3, headers=headers, timeout=10)
        response3.raise_for_status()  # 检查 HTTP 状态码
        response3.encoding = response3.apparent_encoding  # 设置编码
        soup3 = BeautifulSoup(response3.text, "html.parser")
        print(soup3)
        print('数据在进行处理')
        to3 = zhan_daye_table(soup3)
        print("\n输出处理后的数据\n", to3)
        update_pro_bar(60)
        # 合并三个结果
        combined_to = to + to2 + to3

        print('合并信息,并且准备输出,本次获取代理共计60条')
        update_pro_bar(70)
        lines = []

        for item in combined_to:
            if len(item) >= 2:  # 确保每组数据至少有两个元素可提取
                combined_info = f"{item[0]}:{item[1]}"
                lines.append(combined_info)
        update_pro_bar(80)
        # 检查output目录是否存在，不存在则创建
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        update_pro_bar(90)
        print('准备输出到文件...')
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



