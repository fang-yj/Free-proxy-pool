# yancy_qubiaoqian1.py
from bs4 import BeautifulSoup
from data import yancy_canshu
import requests
import re

def clean_tag(tag):
    
    
    return tag.get_text(strip=True)

# def parse_table(thead, tbody):
def parse_table(tbody):


    if tbody:
        tbody_rows = [[clean_tag(td) for td in row.find_all("td")] for row in tbody.find_all("tr")]
    else:
        tbody_rows = []

    return tbody_rows

def ihuan_table(tbody):

    if tbody:
        tbody_rows = [[clean_tag(td) for td in row.find_all("td")] for row in tbody.find_all("tr")]
    else:
        tbody_rows = []

    return tbody_rows


def proxylistplu_table(table): 
    result_data = []
    tr_tags = table.find_all('tr')
    print(yancy_canshu.url4_thead)
    for tr_tag in tr_tags:
        #寻找所有的td标签
        td_tags = tr_tag.find_all('td')
        tbody_rows = [td_tag.text.strip() for td_tag in td_tags]
        if len(tbody_rows) == 8 and tbody_rows[0] == '' and isinstance(tbody_rows[2], str) and tbody_rows[2].isdigit():
            result_data.append(tbody_rows)
            print(tbody_rows)


    return result_data

def ip3366_table(table):

        # 获取 tbody 标签
        tbody = table.find("tbody")

        # 解析表格数据
        tbody_rows = []
        for row in tbody.find_all("tr"):
            cols = row.find_all("td")
            
            # 如果一行包含7列数据
            if len(cols) == 7:
                ip = cols[0].text.strip().replace("IP", "")
                port = cols[1].text.strip().replace("PORT", "")
                anonymity = cols[2].text.strip().replace("匿名度", "")
                proxy_type = cols[3].text.strip().replace("类型", "")
                location = cols[4].text.strip().replace("位置", "")
                response_speed = cols[5].text.strip().replace("响应速度", "")
                last_verified = cols[6].text.strip().replace("录取时间", "")

                # 添加到 tbody_rows 列表中
                tbody_rows.append([ip, port, anonymity, proxy_type, location, response_speed, last_verified])

            # 打印表头
            print("信息:",yancy_canshu.url1_thead)

            # 打印每一行数据
            for row in tbody_rows:
                print("内容:", row)

        return tbody_rows
def openproxy_table(url):
    # data = table.text

    response = requests.get(url, headers=yancy_canshu.url5_headers,timeout=10)

    if response.status_code == 200:
        # soup = BeautifulSoup(response.text,'html.parser')
        data = response.text
        pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b'
        ip_port_matches = re.findall(pattern,data)
        for match in ip_port_matches:
            print(match)

    else:
        print('出现异常，状态码：{response.status_code}')
    return []




