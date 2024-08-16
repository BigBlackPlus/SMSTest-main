import requests
from multiprocessing.dummy import Pool
"""
url = "http://httpbin.org/ip"
headers = {
       'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko)Version/5.1 Safari/534.50'
}
for proxy in proxies:
    print(proxy)
    try:
        resp = requests.get(url,headers=headers,proxies=proxy,timeout=10)
        print(resp.text)
    except Exception as e:
        print(f"请求失败，代理IP无效！{e}")
"""

# 下面这些代码来验证哪些动态ip是可用的，哪些是不可用的，可用的就保存到txt里。
# 因为我们本身用来请求的时候就是使用requests这个库来进行使用的， 不如直接用它来做验证哈哈
def http_proxies_test(all_ip):
    #print("开始测试\n")
    try:
        # 设置timeout
        response = requests.get('https://cloud.tencent.com/', proxies={'http': 'http://'+all_ip}, timeout=10)
        print("使用的Ip地址为：{}".format(all_ip))
    except Exception as e:
        print('nothing')
    else:
        if response.status_code == 200:
            print("请求成功一次！")
            greatAPI.append(all_ip)

def s4_proxies_test(all_ip):
    #print("开始测试\n")
    try:
        # 设置timeout
        response = requests.get('https://cloud.tencent.com/', proxies={'all://': 'scos4://'+all_ip}, timeout=10)
        print("使用的Ip地址为：{}".format(all_ip))
    except Exception as e:
        print('nothing')
    else:
        if response.status_code == 200:
            print("请求成功一次！")
            greatAPI.append(all_ip)

def s5_proxies_test(all_ip):
    #print("开始测试\n")
    try:
        # 设置timeout
        response = requests.get('https://cupfox.love/', proxies={'all://': 'scos5://'+all_ip}, timeout=10)
        print("使用的Ip地址为：{}".format(all_ip))
    except Exception as e:
        print('nothing')
    else:
        if response.status_code == 200:
            print("请求成功一次！")
            greatAPI.append(all_ip)
def read_file(f1):
    f = open(f1, 'r')
    line = f.readline()
    all_ip = []
    while line:
        all_ip.append(line.strip())
        line = f.readline()
    f.close()
    print(all_ip)
    return all_ip


def test_proxies(f2, fc, filename):
    all_ip = read_file(f2)
    pool = Pool(200)
    match fc:
        case "1":
            pool.map(http_proxies_test, all_ip)

        case "2":
            pool.map(s4_proxies_test, all_ip)

        case "3":
            pool.map(s5_proxies_test, all_ip)

    with open(filename, 'a', encoding='utf-8') as fp:
        fp.truncate(0)
        for ip in greatAPI:
            fp.write(ip + '\n')
    greatAPI.clear()


if __name__ == '__main__':

    greatAPI = []
    """
    i = input(
        "1.HTTP \n"
        "2.SOCKS4 \n"
        "3.SOCKS5 \n"
    )
    match str(i):
        case "1":
            filename = "greatHttp_ip.txt"
            f1 = "http_proxy.txt"
            test_proxies(f1, "1", filename)

        case "2":
            filename = "greatSocks4_ip.txt"ww
            f1 = "socks4_proxy.txt"
            test_proxies(f1, "2", filename)

        case "3":
            filename = "greatSocks5_ip.txt"
            f1 = "socks5_proxy.txt"
            test_proxies(f1, "3", filename)

        case _:wwww
            print("输入错误！！！")

"""

    filename = "greatHttp_ip.txt"
    f1 = "http_proxy.txt"
    test_proxies(f1, "1", filename)

    filename = "greatSocks4_ip.txt"
    f1 = "socks4_proxy.txt"
    test_proxies(f1, "2", filename)

    filename = "greatSocks5_ip.txt"
    f1 = "socks5_proxy.txt"
    test_proxies(f1, "3", filename)


