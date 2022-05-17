import random
import requests
import threading

G = '\033[2;32m' #اخضر
R = '\033[1;31m' #احمر
def randio():
	a= str(random.randint(1,254))
	b= str(random.randint(1,254))
	c= str(random.randint(1,254))
	d= str(random.randint(1,254))
	e='.'
	p=['8080','1256','5018','8181','3127','53281','999']
	return a+e+b+e+c+e+d+':'+random.choice(p)

num = int(input("Numper Proxies : "))



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




for x in range(num):
	z= randio()
	ch= threading.Thread(target=che,args=(z,))
	ch.start()
	
	