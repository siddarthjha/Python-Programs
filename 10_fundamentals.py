"""
Please uncomment and execute as there may be use of similar variables.
List Set Tuple Dictionary
"""
# List
"""
l = ['Siddarth', 40, 'CSE']
print(l)
print('Student Name is {0} and his roll number is {1} enrolled with in {2}'.format(l[0], l[1], l[2]))
print(l[-1])
l = [1, 98, 3, 4]
print(max(l))
# s='hey'
# print(list(s))
print(l.copy())
print(l.count(4))
print(l.sort())
print(l)
# Set
s = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturady', 'Sunday'}
print(s)
print(type(s))
s.add('yo')
print(s)
s.update('hello')
print(s)
# print(s.clear())
print(s.copy())
s.remove('Sunday')
print(s)
s1 = {'January', 'February'}
print(s1)
print(s.union(s1))
print(s.intersection())
print(s.isdisjoint(s1))
s.pop()
print(s)
print(s.discard('hahaha'))
print('We are done')
s2 = frozenset(s)
print(s2)
# Dictionary
d = {'Name': 'Siddarth', 'Age': 19, 'Sex': 'Male'}
d1 = {'Name': 'Shristi', 'Age': 19, 'Sex': 'Female'}
print(d)
print(d.get('Name'))
del d['Sex']
print(d)
print(d.keys())
print(d.values())
d.update(d1)
print(d)
d.popitem()
print(d)
d.pop('Age')
print(d)
print('Name' in d)
"""
print('We will be implementing operations on list')
list1 = []
print('Empty list', list1)
list2 = [1, 'sid', 2, 'nik']
print('Second list', list2)
list1.append(1)
list1.append('ashu')
print('List_1 after adding elements', list1)
print('Slicing', list2[0:2])
list1.remove(1)
print('After removing elements from list_1', list1)
list1.clear()
print('After clearing list1',list1)
list2.pop()
print('After poping the second list', list2)
list2.extend(['anu', 3, 'nik', 'aa'])
print('Extending the list', list2)
