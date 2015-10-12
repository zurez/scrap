from bs4 import BeautifulSoup
from urllib2 import urlopen 
# import xlsxwriter
# import time
# import os.path
filename= "links.txt"
divclass= "productSpecs"
# xlsfile="tablet.xlsx"
host="http://flipkart.com"

# workbook = xlsxwriter.Workbook("tablet.xlsx")#Create a new file


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
with open(filename) as f:
	
	counter=0
	for line in myreadlines(f,"#"):
		counter = counter +1
		url = host+line
		if url in register:print "Duplicate link"
		else:
			# time.sleep(10)
			try:

				# row=0
				# col=0
				# worksheet = workbook.add_worksheet()#Add a worksheet
				url = host+line
				# print url
				data = urlopen(url).read()
				

				soup= BeautifulSoup(data,"lxml")
				main_div= soup.find('div',{'class':divclass})
				html = soup.prettify("utf-8")
				fn="/home/joker/Desktop/scrap/tablet_temp/"+str(counter)+".txt"
				print fn
				with open ("fn","wb+") as g:
					g.write(html)
				# print type(main_div)

				
				
				# title=main_div.find('h3',{'class':'sectionTitle'})
				# print title.contents[0]
				# worksheet.write(row,col,title.contents[0])
				
				# row+=1
				# col+=1

				# tables= soup.findAll('table',{'class':'specTable'})
				# for i in tables:
				# 	pass
				# 	"""

				# 	"""
				# register.append(url)
				
				
			except:
				print "An error occured"
				pass


workbook.close()
			 
	
		


