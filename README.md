# Free-proxy-pool-杨CC

​	这款工具名称顾名思义,是一款免费代理池的获取工具,通过手动收集免费的代理池网站,通过代码进行汇总,最终形成了免费的代理池工具.而且作为一位红队人员,ip池几乎是必备的,但是从各种搜索引擎找了一下,发现很多ip池打着免费的名号,点进去之后又要让你充值,心里总感觉收到了欺骗.总让人心里起起落落落落落...


## 免责声明
  此工具仅用于学习交流,此工具禁止任何形式的非法操作,此工具开发者不承担任何法律风险责任等.

-- 
-- 
-- 

# Free-proxy-pool简介:

  这款工具是专门为了经常用到'爆破'/'扫描'/'抢票'/'撸空投'...等多ip使用场景,进行的开发,毕竟谁也不想扫描一半ip被封了,对吧?





## 新版协议支持

|  协议  | 是否支持 |
| :----: | :------: |
|  http  |    √     |
| https  |    √     |
| socks4 |    ×     |
| socks5 |    ×     |


## 新版更新内容

### V1.0-发布-甲辰年 丙子月 甲子日(24年阳历12月26)
- [维护]重构整体代码
- [维护]取消掉了命令行
- [更新]使用了图形化界面
- [优化]简单化图形界面
- [优化]将输出一致更改为一行一个.
- [优化]将输出内容更改为:xxx.xxx.xxx.xxx:xxx格式
- [维护]暂时取消掉了socks4和socks5的代理池获取
- [优化]pyhton3.8以上版本,均可使用
- [优化]将整体代码优化到34kb(未来可能会逐步增加)
- [维护]需要在本机安装curl命令,并且添加到环境变量
- [优化]输出文件支持多种爆破/扫描工具直接使用
- [优化]取消掉了臃肿的chromedriver
- [优化]支持跨平台使用(包括但不限于:WIndows/Linux/MacOS/Android/模拟终端等)
- [更新]添加了进度条,让其效果更直接
- [更新]当发生错误后,该软件会自动对错误位置进行定位
- [更新]在终端中添加了运行日志

## 新版使用教程
  ```
    curl -v #如果没有请下载设置环境变量,不懂请百度
    python --version #查看当前python版本是否为3.8以上
    python -m pip install -r requirements.txt #安装支持库
    python yancy_run_gui.py #运行
  ```
## 新版截图
![image](https://github.com/user-attachments/assets/80abdcdf-59be-4395-a126-61c89d13bc9a)
## -- 
![image](https://github.com/user-attachments/assets/92f92cd2-03f5-4f4e-b29c-b11f470c3e64)
## --
![image](https://github.com/user-attachments/assets/2e7e00c1-c0dc-431a-90d7-35401d527165)
## --
![image](https://github.com/user-attachments/assets/def7aba1-bd70-4e87-9d8d-d0fe0cafde29)




## 旧版协议支持

|  协议  | 是否支持 |
| :----: | :------: |
|  http  |    √     |
| https  |    √     |
| socks4 |    √     |
| socks5 |    √     |

## 老版本更新内容
### V0.5.2-甲辰年 丙子月 丙辰日

- 修复偶尔‘-up’参数不能使用的bug
- 修复使用‘-up’参数后，会导致当前目录为空的bug


### V0.5.1-甲辰年  丙子月 甲寅日更新 

- 修复'-op'参数,乱码,以及偶尔无法输出的bug
- 修复'-pr'参数,输出信息乱码的bug.
- 修复'-a'参数,调用信息不全的bug.
- 修复Windows下'-i'参数无法输出的问题.
- 优化'-pr'参数的代码.
- 重写了'-op'参数的运行代码,使其更加稳定.
![image](https://github.com/user-attachments/assets/fbb868d5-8001-44d0-a006-c7ab42f96ebe)


### V0.5-甲辰年  丙子月 壬子日更新 

- 更改项目名称为:Free-proxy-pool
- 添加功能:自动更新
- 添加了proxy_list源
- 优化了openproxy代理池的获取
- 对多个部分进行了不同程度的优化
  ```
    -h, --help            show this help message and exit
    -z, --run-zdaye       使用 zdaye 获取代理池ip(高质量/支持全系统/容易被封ip))
    -i, --run-ihuan       使用 ihuan 获取代理池ip(高质量/仅支持Windows)
    -ip36, --run-ip3366   使用ip3366获取代理持池（中质量/支持全系统）
    -pr, --run-proxylistplus
                          使用 proxylistpus 获取代理池ip（中质量/支持全系统）
    -op, --run-openproxy  使用 openproxy 源获取代理池（中质量/当前全系统可用）
    -pl, --run-proxy_list
                          使用 proxy_list 源获取代理池（中质量/当前全系统可用）
    -O, --save-output     将获取到的ip池存放在output目录中的Save file.txt文件中
    -up, --run-update     获取最新版本的,代理池工具(需要有git和rm命令)
    -a, --run-all         运行所有参数（默认不使用-i参数，如果你是Widnows系统，请手动添加-i参数）
  ```

当前总参数如下图:

![image](https://github.com/user-attachments/assets/df43dfda-a043-4e6e-abda-ccf2ef34ad12)








### V0.4-甲辰年 丙子月 戊申日 更新

- 添加功能:输出文件保存
- 添加open proxy代理源
- 添加两个参数,分别为: -op 和 -O
- 修复IP3366源时不时获取信息到一半不能获取信息的问题
- 修复了部分已知bug
- 优化了部分代码
- 如果有人觉得使用工具麻烦，请你直接查看data目录下的yancy_canshu.py文件，谢谢！请不要跟智障一样去我B站评论区瞎评论！

![image](https://github.com/user-attachments/assets/a2cf492a-ecf2-44f3-9a41-5ef91f51ffd6)



```
usage: python run.py [-h] [-z] [-i] [-a] [-pr] [-op] [-O]

杨CC-获取代理池ip Version：0.4

options:
  -h, --help            show this help message and exit
  -z, --run-zdaye       使用 zdaye 获取代理池ip(高质量/支持全系统/容易被封ip))
  -i, --run-ihuan       使用 ihuan 获取代理池ip(高质量/仅支持Windows)
  -ip36, --run-ip3366   使用ip3366获取代理持池（中质量/支持全系统）  
  
  -pr, --run-proxylistplus
                        使用 proxylistpus 获取代理池ip（中质量/支持全系统）  
  -a, --run-all         运行所有参数（默认不使用-i参数，如果你是Widnows系统，请手动添加-i参数）
  -op, --run-openproxy  使用 openproxy 源获取socks4代理池（中质量/当前全系统可用）
  -O, --save-output     将获取到的ip池存放在output目录中的svae.txt文件中

```


###  V0.3-甲辰年 丙子月 丙午日更新

-  添加-a参数 可以同时运行全部参数


-  添加-pr参数 -使用proxylistpus源进行获取


-  更新-ip36 参数代码逻辑，使其运行更快，信息更明确


-  优化整体代码逻辑


-  优化python支持，当前支持python3.12/3.11/3.10,其他python版本暂未测试，预计3.7以上版本均可使用



```
usage: python run.py [-h] [-z] [-i] [-a] [-pr]

杨CC-获取代理池ip Version：0.3

options:
  -h, --help            show this help message and exit
  -z, --run-zdaye       使用 zdaye 获取代理池ip(高质量/支持全系统)
  -i, --run-ihuan       使用 ihuan 获取代理池ip(高质量/仅支持Windows)
  -ip36, --run-ip3366   使用ip3366获取代理持池（中质量/支持全系统）
  -pr, --run-proxylistplus
                        使用 proxylistpus 获取代理池ip（中质量/支持全系统）
  -a, --run-all         运行所有参数（默认不使用-i参数，如果你是Widnows系统，请手动添加-i参数）


```


### V0.2-甲辰年 丙子月 丙午日
- 新添加了一个源，足以获取对应代理池ip.

- 添加版本号。

- 添加参数 -ip36

```
  -h, --help           show this help message and exit
  -z, --run-zdaye      使用 zdaye 获取代理池ip(高质量/支持全系统)
  -i, --run-ihuan      使用 ihuan 获取代理池ip(高质量/仅支持Windows)
  -ip36, --run-ip3366  使用ip3366获取代理持池（中质量/支持全系统）

```

### 24年12月6号-免费代理池工具发布!
免费的代理池-完全开源,可以提意见,后续会持续更新.

python版本:3.12 其他版本请自测  

## 旧版使用教程:

```
git clone https://github.com/Sgyling/Free-proxy-pool
cd Free-proxy-pool
python3 -m pip install -r requirements.txt
python3 run.py -h 
```

  ## 请开发者喝杯咖啡?
  ## 手机关机了,嗯哼,找不到收款码了~呜呜呜





![image](https://github.com/user-attachments/assets/cbb8ee9e-eb96-4bfe-8ebd-0e068b45ef9a)

# QQ交流群:660264846  B站：疯狂的杨CC 

![image](https://github.com/user-attachments/assets/aa6099f8-d09d-4a93-b781-30ce705499cd)
