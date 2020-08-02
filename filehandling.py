"""
Basic file manipulation functions.
"""
print('The file handling things are there here.......')
file = open('file.txt', 'r')
print(file.tell())

if file:
    print('File opened')
    print(file.read(100))
    print(file.readline())
else:
    print('File not opened : Error might have occurred')
file.close()
print('File is closed now')
f = open('f.txt', 'w+')
f.write('Yeah bitch')
print(f.tell())
f2 = open('f.txt', 'a+')
print(f2)
f2.write(' Alright')
print(f2.readline())
f1 = open('sd.png', 'rb')
print(f1)
print(f1.read(1000))
f.close()
f1.close()
f2.close()
with open('f.txt', 'r') as f3:
    print(f3.readline())
print('All files closed')
import os
# os.rename('f.txt', 'file1.txt')
# os.remove('f.txt')
# os.mkdir('new')
# os.chdir('new')
print(os.getcwd())
# os.rmdir('new')
