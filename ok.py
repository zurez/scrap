from bs4 import BeautifulSoup
from urllib2 import urlopen
#url="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=tyy%2Chry&filterNone=true&start=%s&ajax=true&_=1443688903409"%(start)
start=20
counter=20
flag=35
all_links=[]
i=0
while i<flag:


	url="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=tyy%%2Chry&filterNone=true&start=%s&ajax=true&_=1443688903409"%(start)
	data = urlopen(url).read()
	soup= BeautifulSoup(data)
	total=0
	for a in soup.find_all('a', href=True):
		total+=1
		with open("links.txt","a") as f:
			f.write(a["href"]+"#")
		
	i+=1
	start= start+20
	print total
	

