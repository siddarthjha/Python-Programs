import re
print('I am created to understand regex functions to Mr. Jha')
s = 'Hey I am Siddarth. Hey I am kumar. Hey I am Jha'
print(s)
x = re.search('Hey I am', s)
if (x):
    print('We found match')
else:
    print('No match Found')
x1 = re.findall('am', s)
x2 = re.search('\s', s)
print(x1)
print(x2.start())              # First space used location
x3 = re.split('\.', s)         # It splits according to the given value
x4 = re.split('\.', s, 1)      # It splits to the limited number of times
print(x3)
print(x4)
x5 = re.sub('I am', '', s)     # It substitutes the value given in place of given value
print(x5)
x6 = re.sub('I am', '', s, 1)  # We can control the number of occurrences by giving the count
print(x6)
