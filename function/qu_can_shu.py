
def proxy_list_table(table):
        # print(table)
        # 获取 tbody 标签
        tbody = table.find("tbody")

        # 解析表格数据
        tbody_rows = []
        for row in tbody.find_all("tr"):
            cols = row.find_all("td")
            # 如果一行包含7列数据
            if len(cols) == 5:
                ip = cols[0].text.strip().replace("IP", "")
                port = cols[1].text.strip().replace("PORT", "")
                anonymity = cols[2].text.strip().replace("匿名度", "")
                proxy_type = cols[3].text.strip().replace("国家", "")
                location = cols[4].text.strip().replace("相应速度", "")
                # response_speed = cols[5].text.strip().replace("响应速度", "")
                # last_verified = cols[6].text.strip().replace("录取时间", "")

                # 添加到 tbody_rows 列表中
                tbody_rows.append([ip, port, anonymity, proxy_type, location])

        # 打印表头
        # print("信息:",yancy_canshu.url6_thead)

        # 打印每一行数据
        for row in tbody_rows:
            print("内容:", row)

        return tbody_rows
