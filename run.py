import argparse
from yancy_get import yancy_zdaye, yancy_ihuan, yancy_ip3366, yancy_proxylistplu, yancy_openproxy
import sys
from io import StringIO

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description="杨CC-获取代理池ip\nVersion：0.4",
        usage="python run.py [-h] [-z] [-i] [-a] [-pr] [-op] [-O]"
    )
    # 添加各个参数，这里补充上 -O 参数的定义
    parser.add_argument("-z", "--run-zdaye", action="store_true", dest="run_zdaye",
                        help="使用 zdaye 获取代理池ip(高质量/支持全系统/容易被封ip))")
    parser.add_argument("-i", "--run-ihuan", action="store_true", dest="run_ihuan",
                        help="使用 ihuan 获取代理池ip(高质量/仅支持Windows)")
    parser.add_argument("-ip36", "--run-ip3366", action="store_true", dest="run_ip3366",
                        help="使用ip3366获取代理持池（中质量/支持全系统）")
    parser.add_argument("-pr", "--run-proxylistplus", action="store_true", dest="run_proxylistplus",
                        help="使用 proxylistpus 获取代理池ip（中质量/支持全系统）")
    parser.add_argument("-a", "--run-all", action="store_true", dest="run_all",
                        help="运行所有参数（默认不使用-i参数，如果你是Widnows系统，请手动添加-i参数）")
    parser.add_argument("-op", "--run-openproxy", action="store_true", dest="run_openproxy",
                        help="使用 openproxy 源获取socks4代理池（中质量/当前全系统可用）")
    parser.add_argument("-O", "--save-output", action="store_true", dest="save_output",
                        help="将获取到的ip池存放在output目录中的svae.txt文件中")

    args = parser.parse_args()

    # 用于记录是否执行了有效参数对应的函数
    func_executed = False
    # 用于捕获终端输出内容的对象
    redirected_output = None
    if args.save_output:
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output

    if args.run_all:
        func_executed = True
        print('运行所有参数(默认不运行-i，如果你是Windows用户请自行添加-i参数)')
        yancy_zdaye()
        if args.run_ihuan:
            yancy_ihuan()
        yancy_ip3366()
        yancy_proxylistplu()
        yancy_openproxy()
    if args.run_zdaye:
        func_executed = True
        print("使用 zdaye 获取代理池ip中...（此参数及其容易被封IP，少用！）")
        yancy_zdaye()
    if args.run_ihuan:
        func_executed = True
        print("使用 ihuan 获取代理池ip中...")
        yancy_ihuan()
    if args.run_ip3366:
        func_executed = True
        print('使用ip3366获取代理池中...')
        yancy_ip3366()
    if args.run_proxylistplus:
        func_executed = True
        print('使用 proxylistplu 获取代理池中...')
        yancy_proxylistplu()
    if args.run_openproxy:
        func_executed = True
        print("使用 openproxy 获取代理池中...")
        yancy_openproxy()

    if not func_executed:
        parser.print_help()

    if args.save_output:
        # 恢复标准输出
        sys.stdout = old_stdout
        with open('output/Save file.txt', 'w') as f:
            f.write(redirected_output.getvalue())

if __name__ == "__main__":
    main()