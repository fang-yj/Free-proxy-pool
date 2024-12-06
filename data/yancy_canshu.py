import random

suijishu = random.randint(1, 20)
url1 = f'https://www.zdaye.com/Free/{suijishu}/'
url1_headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
url1_thead = ['IP地址',	'端口',	'类型',	'地理位置',	'上次验证',	'https',	'post',	'响应时间',	'已存活时间']

url2 = 'https://ip.ihuan.me/?page=b97827cc'
url2_headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Cookie":"20930a62a242c92e3e695ca20f367f66=14a8b5e1824bebcc1385ef439b1498c6; Hm_lvt_8ccd0ef22095c2eebfe4cd6187dea829=1733463333; HMACCOUNT=52725196F4D2DF9F; 426769e6a15025e510124cd10ad8a2a5=6fe966fdde87e60eb9cbc0c4dc0e60a4; Hm_lpvt_8ccd0ef22095c2eebfe4cd6187dea829=1733466412"
}
url2_thead = ['IP地址',	'端口',	'地理位置',	'运营商',	'HTTPS',	'POST',	'匿名度',	'访问速度',	'入库时间',	'最后检测时间']

driver_path = fr'chromedriver-win64\chromedriver.exe'
chrome_path = fr'Application\chrome.exe'
