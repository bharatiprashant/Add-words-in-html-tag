import os

with open("word.txt",'r') as f: #storing  the text file in the variable f
	content = f.readlines() #reading the text file line by line
content = [x.strip() for x in content] #removing the character from the front and back
if os.path.exists("result.txt"):
	os.remove("result.txt")
new_file= open("result.txt",'w+')
for x in content:
	new_file.write("<p>"+x+"</P>\r\n")
	print(x)

new_file.close()
	