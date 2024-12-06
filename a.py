from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 设置chromedriver路径
driver_path = fr'chromedriver-win64\chromedriver.exe'  # 请替换为你本地的chromedriver路径
chrome_path = fr'Application\chrome.exe'  # 请替换为你本地的chrome浏览器路径

# 设置Chrome选项
chrome_options = Options()
chrome_options.binary_location = chrome_path  # 指定Chrome浏览器的路径

# 使用Service指定chromedriver路径
service = Service(driver_path)

# 创建webdriver实例
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开页面
driver.get('https://ip.ihuan.me/')

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
            '地理位置': location,
            '运营商': isp,
            'HTTPS': https,
            'POST': post,
            '匿名度': anonymity,
            '访问速度': speed,
            '入库时间': entry_time,
            '最后检测': last_check
        })

    # 输出提取的结果
    for entry in data:
        print(entry)

else:
    print("未找到目标表格。")

# 关闭浏览器
driver.quit()
