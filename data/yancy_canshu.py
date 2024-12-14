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


url3 = f'https://proxy.ip3366.net/free/?action=china&page={suijishu}'

url4='https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1'
url4_thead=['图标', 'IP 地址', '端口',	'类型',	'国家',	'谷歌',	'Https']

url5_http='https://openproxy.space/list/http'
url5_socks4='https://openproxy.space/list/socks4'
url5_socks5='https://openproxy.space/list/socks5'

url5_headers = {
    "Sec-Ch-Ua": '"Chromium";v="123", "Not:A-Brand";v="8"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Linux",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.122 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Priority": "u=0, i",
    "Connection": "close"
}
url6 = 'https://www.proxy-list.download/HTTP'
url6_thead=['IP地址','端口号','匿名程度','国家','延迟']

