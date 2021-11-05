f = open("fileText.txt", 'w')

for i in range(1,50):
	text = "This is line " + str(i) + "."
	f.write(text + "\n")
f.close()
	
