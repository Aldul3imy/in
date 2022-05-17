import requests
import threading
G = '\033[2;32m' #اخضر
R = '\033[1;31m' #احمر



tweets = open('proxies_list.txt', 'r', encoding='utf-8')
wtweets = open('goodproxy.txt', 'w+', encoding='utf-8')
def che(proxy):
#	proxy='114.4.104.254:3128'
	prox={
		'https' : str(proxy)
	}
	pr= prox['https']
	try:
		req = requests.get("https://ipinfo.io/json",proxies=prox)
		print(G+"Connected : "+pr)
		wtweets.write(pr+'\n')
	except requests.exceptions.ConnectionError:
		print(R+"Connection Error : "+pr)
		



#ch= threading.Thread(target=che,args=('114.4.104.254:3128',))
#ch.start()

tweets= tweets.read()
lent = len(tweets.split('\n'))

for x in range(lent):
	z= tweets.split('\n')[x]
	ch= threading.Thread(target=che,args=(z,))
	ch.start()
	
	