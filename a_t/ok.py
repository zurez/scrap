from bs4 import BeautifulSoup
from urllib2 import urlopen

#url="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=tyy&filterNone=true&start=21&q=tablet+accessories&ajax=true&_=1444565698163"

counter=2000000
flag=5000
all_links=[]
i=0
with open("log.txt","r") as g:
	start=int(g.read())
total=0
def get_link(url):

	data=urlopen(url).read()
	soup=BeautifulSoup(data,"lxml")
	for a in soup.find_all('a', href=True):
		total+=1
		with open("links.txt","a") as f:
			f.write(a["href"]+"#")

while i<flag:
	url="http://www.flipkart.com/lc/pr/pv1/spotList1/spot1/productList?sid=tyy&filterNone=true&start=%s&q=tablet+accessories&ajax=true&_=1444565698163"%(start)
	try:

		
		# data = urlopen(url).read()
		# soup= BeautifulSoup(data)
		
		# for a in soup.find_all('a', href=True):
		# 	total+=1
		# 	with open("links.txt","a") as f:
		# 		f.write(a["href"]+"#")
		get_link(url)
		i+=1
		start= start+20
		print start
	except KeyboardInterrupt:
		with open("log.txt","wb+") as f :
			f.write(str(start))
		raise
        		
	except Exception as m:
		print "An error occured"
		try:

			data = urlopen(url).read()
			soup= BeautifulSoup(data)
			
			for a in soup.find_all('a', href=True):
				total+=1
				with open("links.txt","a") as f:
					f.write(a["href"]+"#")
				
			i+=1
			start= start+20
			print start

		except:
			print "Another error"
			try:
				data = urlopen(url).read()
				soup= BeautifulSoup(data)
				
				for a in soup.find_all('a', href=True):
					total+=1
					with open("links.txt","a") as f:
						f.write(a["href"]+"#")
					
				i+=1
				start= start+20
				print start
			except Exception as e: 
				print e
				print "Skipping.."

