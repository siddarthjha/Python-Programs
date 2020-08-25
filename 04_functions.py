"""
Functions and their manipulation.
"""
print('I was created for Functions,built-in Functions and lambda Functions by Mr.Jha')


def func(*n):
    print('Hello World')
    print('Hey', n)
    print(type(n))


func('sid', 25)
print('Function for sum of two numbers')


def sum(a, b):
    return a+b


'''
a = int(input('Enter value for a'))
b = int(input('Enter value for b'))
print('Sum of those numbers are', sum(a, b))
'''


def ref(l):
    print('l value before changes',l)
    l.append(3)
    l.append(4)
    print('Inside function l value after changes', l)


l = [1, 2]
ref(l)
print('Outside function l value after changes:', l)


def change(s, y):
    print('String value before change:-', s)
    s += ' hahaha'
    print('String value inside function after changes:-', s)


s = 'What a joke'
y = 'hey'
change(y='hey', s='What a joke ')
print('The string value after changes outside the function:-', s)
z = lambda a, b: a-b
print('lambda function result', z(4, 6))
x1 = 10
print(' The binary value of 10 is  ', bin(x1))
s1 = 'Yo'
print('The bytes in-built function', bytes(s1, 'ascii'))
print('Trying to call a variable through Callable method', callable(s1))
code = 'x=1\ny=2\nprint(x+y)'
com = compile(code, 'x.py', 'exec')
x = 1
exec(com)
exec('print(x==1)')
print(sum(['as, sa'], ['abc']))
print(sum([1, 2, 4], ['as', 'sa']))
print(sum([1, 2, 3], [1, 3, 4]))
s2 = sum([4, 5, 6], [1, 2, 3])
print(s2)
l2 = [1, 'k', 3, 's', False]
print('It checks that whether it is iterable or not----', any(l2))
print('This converts objects onto byte array objects-', bytearray(s1, 'utf-8'))
print('It parses the expression and executes', eval("print('Hello1')"))
print('These are the list of attributes in this Program', dir())


def fu_n(x):
    if x > 5:
        return x


p1 = filter(fu_n, [4, 6, 9])
print('It returns the data in list with filtering according to the condition', list(p1))
print('Hash value of String', hash('Sid'))
print(hash(23.98))
# print(help())
print('The is is always unique to each object', id("sid"))
l2 = [10, 5, 6]
print(slice(4, 5, 6))
print(sorted(l2), 'This sorts in ascending by default and in dictionary it only sorts the keys but not values')
print('It represents the number in unicode---', ord('A'))
print('It returns the immutable sequence of numbers given in range', list(range(0, 11)))



