import argparse
import os
from multiprocessing.pool import Pool
import subprocess
import socket


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


def ip2num(ip):
    ips = [int(x) for x in ip.split('.')]
    return ips[0] << 24 | ips[1] << 16 | ips[2] << 8 | ips[3]


def num2ip(num):
    return '%s.%s.%s.%s' % ((num >> 24) & 0xff, (num >> 16) & 0xff, (num >> 8) & 0xff, (num & 0xff))
    # return '%s.%s.%s.%s' % ((num & 0xff000000)>>24,(num & 0x00ff0000)>>16,(num & 0x00000ff00)>>8,num & 0x000000ff)


def gen_ip(ip):
    start, end = [ip2num(x) for x in ip.split('-')]
    return [num2ip(num) for num in range(start, end+1) if num & 0xff]


# 参数处理
parser = argparse.ArgumentParser(description='主机扫描器')
parser.add_argument(
    '-f', choices=['ping', 'tcp'], help='扫描 ip 范围 or 对应 ip 的端口', required=True)
parser.add_argument(
    '-n', type=int, help='并发数量', default=1)

parser.add_argument(
    '-m', choices=['proc', 'thread'], help='模式: proc|thread', default='thread')

parser.add_argument(
    '-w', help='保存结果到文件')

# TODO IP 校验
parser.add_argument(
    '-ip', help='目标ip 或 ip范围', required=True)

args = parser.parse_args()

ips = args.ip.split('-')

if len(ips) == 1:
    pass
else:
    # 将 ips 换成数组  192.168.0.1-192.168.0.100
    ips = gen_ip(args.ip)


def runPing(ip,):
    command = ['ping', '-c', '1', ip]
    print(f'start ping {ip} .....')
    res = subprocess.call(command, stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL) == 0
    print(f'end ping {ip} : {res}')
    return f'ping {ip} : {res}'


def runTelnet(ip, port):
    print(f'start check {ip}:{port} .....')
    res = isOpen(ip, port)
    print(f'end check {ip}:{port} : {res}')
    return f'telnet {ip}:{port} : {res}'


if __name__ == "__main__":
    p = Pool(args.n)
    if args.f == 'ping':
        results = []
        for ip in ips:
            results.append(p.apply_async(runPing, args=(ip,)))
        p.close()
        p.join()
        for res in results:
            if args.w:
                with open(args.w, 'a+', encoding='utf-8') as article:
                    article.write(f'{res.get()} \n')
                    article.close()
            else:
                print(res.get())
        p.terminate()
    else:
        results = []
        for ip in ips:
            for port in range(65535):
                results.append(p.apply_async(runTelnet, args=(ip, port)))
        p.close()
        p.join()
        for res in results:
            if args.w:
                with open(args.w, 'a+', encoding='utf-8') as article:
                    article.write(f'{res.get()} \n')
                    article.close()
            else:
                print(res.get())
        p.terminate()

# python3 pmap.py -n 100 -f ping -ip 192.168.10.100-192.168.10.200 -w pingRes.txt
# python3 pmap.py -n 10000 -f tcp -ip 192.168.10.157 -w tcpRes.txt
