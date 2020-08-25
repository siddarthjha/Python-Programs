with open("file.txt") as file:
	stuff=file.read()
	print(stuff)
	
	
print(file.closed)
print(stuff)

with open("file.txt",'w') as file1:
	file1.write("Yes motherfucker")
with open("file.txt") as file:
	stuff=file.read()
	print(stuff)
	
