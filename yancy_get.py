import requests
from bs4 import BeautifulSoup
import data.yancy_canshu
from data import yancy_canshu
from tools.yancy_qubiaoqian1 import parse_table,ihuan_table,proxylistplu_table,ip3366_table,proxy_list_table
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import subprocess
import os
import tempfile

def yancy_zdaye():

    try:
        # 发起 GET 请求
        response = requests.get(data.yancy_canshu.url1, headers=data.yancy_canshu.url1_headers, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        response.encoding = response.apparent_encoding

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, "html.parser")

        # 获取 tbody 标签
        tbody = soup.find("tbody")

        # 使用 parse_table 函数解析表格
        tbody_rows = parse_table(tbody)

        # 打印表头和内容
        print("信息:", data.yancy_canshu.url1_thead)
        for row in tbody_rows:
            print("内容:", row)

        return tbody_rows

    except requests.exceptions.RequestException as e:
        print(f"出现了错误 {e}\n请更换ip或过段时间再重新获取")
        return []

def yancy_ihuan():

    try:

        # 设置Chrome选项
        chrome_options = Options()
        # chrome_options.binary_location = yancy_canshu.chrome_path
        chrome_options.add_argument('--headless')

        # 使用Service指定chromedriver路径
        service = Service(yancy_canshu.driver_path)

        # 创建webdriver实例
        driver = webdriver.Chrome(service=service, options=chrome_options)
        # 打开页面
        driver.get(yancy_canshu.url2)

        # 等待页面加载完成
        driver.implicitly_wait(10)  # 最多等待10秒

        # 获取网页内容
        html = driver.page_source

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(html, 'html.parser')

        # 找到表格
        table = soup.find('table', {'class': 'table table-hover table-bordered'})

        if table:
            # 提取表格中的每一行数据
            rows = table.find_all('tr')[1:]  # 跳过表头

            data = []
            for row in rows:
                cols = row.find_all('td')
                ip_address = cols[0].get_text(strip=True)  # IP地址
                port = cols[1].get_text(strip=True)  # 端口
                location = cols[2].get_text(strip=True)  # 地理位置
                isp = cols[3].get_text(strip=True)  # 运营商
                https = cols[4].get_text(strip=True)  # HTTPS
                post = cols[5].get_text(strip=True)  # POST
                anonymity = cols[6].get_text(strip=True)  # 匿名度
                speed = cols[7].get_text(strip=True)  # 访问速度
                entry_time = cols[8].get_text(strip=True)  # 入库时间
                last_check = cols[9].get_text(strip=True)  # 最后检测

                # 将每一行的数据保存为一个字典
                data.append({
                    'IP地址': ip_address,
                    '端口': port,
                    '位置': location,
                    # '运营商': isp,
                    'HTTPS': https,
                    'POST': post,
                    # '匿名度': anonymity,
                    '访问速度': speed,
                    '入库时间': entry_time,
                    '最后在线时间': last_check
                })

            # 输出提取的结果
            for entry in data:
                print(entry)
            #解决、并保存
            result_lines = []
            for entry in data:
                ip = entry['IP地址']
                port = entry['端口']
                result_lines.append(f"{ip}:{port}")

            #保存
            with open('output/out.txt', 'a') as f:
                for line in result_lines:
                    f.write(line + '\n')

    except requests.exceptions.RequestException as e:
        print(f"出现了错误 {e}\n请更换ip或过段时间再重新获取")
        return []

def yancy_ip3366():
    try:
        # 发起 GET 请求
        response = requests.get(data.yancy_canshu.url3, headers=data.yancy_canshu.url1_headers, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        response.encoding = response.apparent_encoding  # 设置编码

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, "html.parser")

        tables = ip3366_table(soup)

        return tables

    except requests.exceptions.RequestException as e:
        print(f"出现了错误 {e}\n请更换ip或过段时间再重新获取")
        return []

def yancy_proxylistplu():
    try:
        # 发起 GET 请求
        response = requests.get(data.yancy_canshu.url4, headers=data.yancy_canshu.url1_headers, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        response.encoding = response.apparent_encoding  # 设置编码

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, "html.parser")

        tables = proxylistplu_table(soup)
        # print(tables)

        return tables

    except requests.exceptions.RequestException as e:
        print(f"出现了错误 {e}\n请更换ip或过段时间再重新获取")
        return []

# def yancy_openproxy():
#     try:
#         print('\nhttp代理如下：')
#         tables0 = openproxy_table(data.yancy_canshu.url5_http)
#         print('\nsocks4代理如下：')
#         tables1 = openproxy_table(data.yancy_canshu.url5_socks4)
#         print('\nsocks5代理如下：')
#         tables2 = openproxy_table(data.yancy_canshu.url5_socks5)
#         return tables0,tables1,tables2

#     except requests.exceptions.RequestException as e:
#         print(f"出现了错误 {e}\n请更换ip或过段时间再重新获取")
#         return []

#获取proxy_list代理源
def yancy_proxy_list():
    try:
        response = requests.get(data.yancy_canshu.url6, headers=data.yancy_canshu.url1_headers, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        response.encoding = response.apparent_encoding  # 设置编码

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, "html.parser")

        # tables = proxylistplu_table(soup)
        print('获取http代理如下:')
        tables0 = proxy_list_table(soup)
        # print(tables0)
        return tables0

    except requests.exceptions.RequestException as e:
        print(f"出现了错误 {e}\n请更换ip或过段时间再重新获取")
        return []

#更新
def yancy_update():
    try:
        # 先改变工作目录到上级目录（跨平台兼容写法）
        os.chdir(os.path.pardir)
        # 判断操作系统类型，构建对应的删除文件夹命令和克隆命令
        if os.name == 'nt':  # Windows系统
            remove_cmd = ['rd', '/S', '/Q', 'yancy-dai-li_chi']
            clone_cmd = ['git', 'clone', 'https://github.com/Sgyling/Free-proxy-pool']
        else:  # Linux和macOS系统
            remove_cmd = ['rm', '-rf', 'yancy-dai-li_chi']
            clone_cmd = ['git', 'clone', 'https://github.com/Sgyling/Free-proxy-pool']

        # 使用git clone命令克隆仓库，如果文件夹已存在，git clone会报错，然后后续删除再重新克隆来模拟覆盖
        try:
            subprocess.check_call(clone_cmd)
        except subprocess.CalledProcessError:
            # 如果文件夹已存在导致git clone失败，先删除已存在的文件夹
            subprocess.check_call(remove_cmd)
            # 再重新尝试克隆
            subprocess.check_call(clone_cmd)
    except subprocess.CalledProcessError as e:
        print(f"更新出错 {e}")

