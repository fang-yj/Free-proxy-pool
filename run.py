import argparse
from yancy_get import yancy_zdaye,yancy_ihuan,yancy_ip3366,yancy_proxylistplu

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(
        description="杨CC-获取代理池ip\nVersion：0.3",
        usage="python run.py [-h] [-z] [-i] [-a] [-pr]"
    )

    # 添加参数
    parser.add_argument(
        "-z", "--run-zdaye",
        action="store_true",
        dest="run_zdaye",
        help="使用 zdaye 获取代理池ip(高质量/支持全系统)"
    )
    parser.add_argument(
        "-i","--run-ihuan",
        action="store_true",
        dest="run_ihuan",
        help="使用 ihuan 获取代理池ip(高质量/仅支持Windows)"
    )
    parser.add_argument(
        "-ip36","--run-ip3366",
        action="store_true",
        dest="run_ip3366",
        help="使用ip3366获取代理持池（中质量/支持全系统）"

    )
    parser.add_argument(
        "-pr","--run-proxylistplus",
        action="store_true",
        dest="run_proxylistplus",
        help="使用 proxylistpus 获取代理池ip（中质量/支持全系统）"
    )
    parser.add_argument(
        "-a","--run-all",
        action="store_true",
        dest="run_all",
        help="运行所有参数（默认不使用-i参数，如果你是Widnows系统，请手动添加-i参数）"
    )

    # 解析命令行参数
    import sys
    if len(sys.argv) == 1:  # 如果没有传入参数，显示帮助信息
        parser.print_help()
        return

    args = parser.parse_args()

    # 参数逻辑
    if args.run_all:
        print('运行所有参数(默认不运行-i，如果你是Windows用户请自行添加-i参数)')
        yancy_zdaye()
        # yancy_ihuan()
        yancy_ip3366()
        yancy_proxylistplu()
    if args.run_zdaye:
        print("使用 zdaye 获取代理池ip中...")
        yancy_zdaye()
    if args.run_ihuan:
        print("使用 ihuan 获取代理池ip中...")
        yancy_ihuan()
    if args.run_ip3366:
        print('使用ip3366获取代理池中...')
        yancy_ip3366()
    if args.run_proxylistplus:
        print('使用 proxylistplu 获取代理池中...')
        yancy_proxylistplu()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
