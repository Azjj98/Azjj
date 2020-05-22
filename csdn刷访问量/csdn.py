import time
from pyquery import PyQuery as pq
import requests
from bs4 import BeautifulSoup
import random  
from fake_useragent import UserAgent 
from lxml import etree
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

def get_random_ip(ip_list):  
    proxy_list = []  
    for ip in ip_list:  
        proxy_list.append(ip)  
        f=open('IP.txt','a+',encoding='utf-8')  
        f.write('http://' + ip)  
        f.write('\n')  
        f.close()  
    proxy_ip = random.choice(proxy_list)  
    proxies = {'http':proxy_ip}  
    return proxies
def get_ip_list(url, headers):  
    web_data = requests.get(url, headers=headers)  
    soup = BeautifulSoup(web_data.text, 'lxml')  
    ips = soup.find_all('tr')  
    ip_list = []  
    for i in range(1, len(ips)):  
        ip_info = ips[i]  
        tds = ip_info.find_all('td') #tr标签中获取td标签数据  
        if not tds[8].text.find('天')==-1:  
            ip_list.append(tds[1].text + ':' + tds[2].text)  
    return ip_list
if __name__ == '__main__':  
    # range(1,3)是页数 一共很多页 所以我们取很多很多页
    print('=========================================================')
    print('==========        ==============                     ====')
    print('=========          ==========================      ======')
    print('========    ====    ========================     ========')
    print('=======    ======    ======================     =========')
    print('======    ========    ===================     ===========')
    print('=====                  =================    =============')
    print('====    ============    ==============     ==============')
    print('===    ==============    ===========      ===============')
    print('==    ================    ========       ================')
    print('=    ==================    ======      ==================')
    print('=   ====================    ===                         =')
    print('=========================================================')  
    for i in range(1,500):
        url = 'http://www.xicidaili.com/wt/{}'.format(i) 
        headers = {  
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'  
        } 
        
        ip_list = get_ip_list(url, headers=headers)  
        proxies = get_random_ip(ip_list)
        ip = str(proxies)  
        print('当前代理IP为：%s'%ip)
        mycsdn = 'https://blog.csdn.net/'  ##我们的需要刷的博客地址
        #mycsdn.ip(proxies)
        csdn = requests.get(url = mycsdn,proxies = proxies)
        selector = etree.HTML(csdn.text)
        fwl = selector.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[1]/div/span[2]/text()')
        c = str(fwl)
        print('==当前文章访问量为：%s=='%c)
        print('==请等待60秒，进行下一次请求==')
        time.sleep(60)
        print('||||访问成功~~ 访问量+1 ||||')  