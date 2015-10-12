with open ("links.txt","r") as f:
	 content = f.read()
	 counter=0
	 for i in content:
	 	if i=="#":counter+=1
	 print counter