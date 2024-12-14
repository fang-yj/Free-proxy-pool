# Free-proxy-pool-杨CC

​	作为一位红队人员,ip池几乎是必备的,但是从各种搜索引擎找了一下,发现很多ip池打着免费的名号,点进去之后又要让你充值,心里总感觉收到了欺骗.总让人心里起起落落落落落...



## Free-proxy-pool简介:

​	这款工具名称顾名思义,是一款免费代理池的获取工具,通过手动收集免费的代理池网站,通过代码进行汇总,最终形成了免费的代理池工具.



​	不过有一点可能需要注意一下,因为这款工具本质上为爬取互联网上所公开的代理池,安全性本人并不能完全保证.请各位自行掂量



## 更新内容

### V0.5-甲辰年  丙子月 壬子日更新 

- 更改项目名称为:Free-proxy-pool
- 添加功能:自动更新
- 添加了proxy_list源
- 优化了openproxy代理池的获取
- 对多个部分进行了不同程度的优化

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

## 使用教程:

```
git clone https://github.com/Sgyling/yancy-dai-li_chi.git#
cd yancy-dai-li_chi
python3 -m pip install -r requirements.txt
python3 run.py -h 
```





![image](https://github.com/user-attachments/assets/cbb8ee9e-eb96-4bfe-8ebd-0e068b45ef9a)

# QQ交流群:660264846  B站：疯狂的杨CC 

![image](https://github.com/user-attachments/assets/aa6099f8-d09d-4a93-b781-30ce705499cd)
