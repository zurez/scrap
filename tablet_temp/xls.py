import glob
import xlsxwriter
from bs4 import BeautifulSoup

def write(f):
	data=f.read()
	soup=BeautifulSoup(data,"lxml")
	worksheet= workbook.add_worksheet()
	title= soup.find("h3",{"class":"sectionTitle"}).contents[0]
	if title!=None:

		worksheet.write(0,0,title)
	table= soup.findChildren("table")
	rows = soup.findChildren(["th","td"])
	b=0
	

	try:
		i=0
		while i<len(rows):


		# for i in xrange(len(rows)):
			# print rows[i].get("class")
			
			if rows[i].get("class")[0]=="groupHead":
				# print "Heading: " + rows[i].text
				worksheet.write(b+1,0,rows[i].text)
				b+=1
				i+=1
				
				
				# rows.remove(rows[i])
			elif rows[i].get("class")[0]=="specsKey":
				worksheet.write(b+1,0,rows[i].text)
				worksheet.write(b+1,1,rows[i+1].text)
				# print rows[i].text + ":" + rows[i+1].text
				# rows.remove(rows[i])

				# rows.remove(rows[i+1])
				b+=1
				i+=2
			elif rows[i].get("class")[0]=="specsValue":
				# print "Value:" + rows[i].text
				worksheet.write(b+1,0,rows[i].text)
				b+=1
				i+=1
			else:
				print "Un" + rows[i].text

	except Exception as e:
		print "Filename: " +i
		print e
		workbook.close()




workbook= xlsxwriter.Workbook("tablet.xlsx")
for i in glob.glob("*"):
	if i=="xls.py" or i=="tablet.xlsx":print "lol"
	else:
		print i
		with open(str(i),"r") as f:
			write(f)
# with open("529","r") as f :
# 	write(f)
workbook.close()