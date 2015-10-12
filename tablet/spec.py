from bs4 import BeautifulSoup
import sys, logging
# from urllib2 import urlopen 
# from stem import Signal
# from stem.control import Controller
# import xlsxwriter
import time
# import mechanize
from selenium import webdriver
driver= webdriver.Chrome()


logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)
# import os.path
filename= "links.txt"
divclass= "productSpecs"
# xlsfile="tablet.xlsx"
host="http://flipkart.com"
headers ={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0', 'Accept-Encoding' : 'gzip, deflate', 'Accept' :'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
# workbook = xlsxwriter.Workbook("tablet.xlsx")#Create a new file

def new_identity():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
def myreadlines(f, newline):
  buf = ""
  while True:
    while newline in buf:
      pos = buf.index(newline)
      yield buf[:pos]
      buf = buf[pos + len(newline):]
    chunk = f.read(4096)
    if not chunk:
      yield buf
      break
    buf += chunk
register=[]
def get_spec(url):
	# browser= mechanize.Browser()
	# browser.open(url)
	# data = urlopen(url).read()
	driver.get(url)
	data=driver.page_source
	# driver.quit()
	#data= browser.response().read()
	print "Data taken "
	soup=BeautifulSoup(data,"lxml")
	main_div= soup.find('div',{'class':divclass})
	print "main_div created"
	title=main_div.find('h3',{'class':'sectionTitle'})
	print title.contents[0]
	html =main_div.prettify("utf-8")
	with open (str(counter),"wb+") as g:
		print "Saving File"
		g.write(html)

with open(filename) as f:
	
	counter=0
	for line in myreadlines(f,"#"):
		
		url = host+line
		if url in register:print "Duplicate link"
		else:
			counter = counter +1
			# time.sleep(10)
			try:
				url = host+line
				get_spec(url)
				
			
			
				register.append(url)
				print "Job Done"
				time.sleep(4)
		
			except KeyboardInterrupt:raise
        		
			except Exception as m:

				print "An error occured"
				print  m
				try:
					url = host+line
					get_spec(url)
					register.append(url)
					time.sleep(4)
				except:
					print "Level 2 error" + url
					pass



# workbook.close()
			 
	
		


