import time
import datetime
print('I am created to make understand Mr.Jha about basics of python')
print('Continuation from Basics file')
# Iam single line comment
''' I am 
   multi-line comment
'''
a = 1000
b = 18
print('i am Siddarth, age is', str(b), 'My salary is', str(a))
# a = int(input("Enter a number"))
'''
if a%2==0:
    print("The  number is even--", str(a))
else:
    print("The number is odd--", str(a))
b = int(input("Enter a number from 1-5"))
if b == 1:
    print("The number entered is 1")
elif b == 2:
    print("The number entered is 2")
elif b == 3:
    print("The number entered is 3")
elif b ==4:
    print("The number entered is 4")
elif b==5:
    print("The number entered is 5")
print("Done looping")
'''
#  print(range(1, 10))
#  range(1, 10)
#  We will print 2 table
'''
i = j = 0
n = 2
for i in range(1, 11):
    print("%d * %d =%d" %(n, i, (n*i)))
for i in range(1, 6):
    print()
    for j in range(0, i+1):
        print("*", end="");
for i in range(0,5):
    print(i)
    break
else:
    print('Else statement');
print("yo break statement occurred in between")

i = 1
while i <= 5:
    print(i)
    i = i+1
j = 1
while j <= 5:
    print(j)
    j = j+1
    break
else:
    print('I am else loop in while')
    '''
l = [1, 2, 3, 4, 5]
f = 0
for i in l:
   print('Element-', i)
   if i == 3:
       pass;
   f = 1
   print('We are inside pass')
   if f == 1:
       print('We are outside pass')
# Date and Time
print(time.time())
print(time.localtime(time.time()))
time.sleep(2)
print(time.asctime(time.localtime(time.time())))
print(datetime.datetime.now())
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
import json
for sa in range(5):
 print(sa)
 break
 else:
  print('Else statement')

