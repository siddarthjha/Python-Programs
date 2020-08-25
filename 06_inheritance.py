"""
Concept of Inheritance.
"""
print('I am created to make understand the concept of inheritance ')


class Upes:
    def __init__(self, i, n):
        print('I am a constructor of Upes ')
        self.i = i
        self.n = n
        print('Ok i am done bye....')

    def fun(self):
        print('I am a function of Upes class')
        print('Function of Upes  exited....')


class Cse:
    def __init__(self, i, n, s):
        print('I am a constructor of Cse')
        self.i = i
        self.n = n
        self.s = s
        print('Ok i am done bye.....')

    def func(self):
        print('I am a function of Cse class')
        print('Function of Cse class exited....')


class Cit(Upes, Cse):
    __c = 10

    def __init__(self, i, n):
        self.i = i
        self.n = n
        print('I am a constructor of CseOg class')
        print('Ok i am done')
        print('The Abstraction variable is this and its value is %d' % Cit.__c)

    def func(self):
        print('I am function of class CseOg(Overrided method of Cse Class)')
        print('Function of CseOg class is exited....')


obj = Cit(40, 'Sid')
obj.fun()
# obj.funct()
obj.func()
print(issubclass(Cit, Cse))
print(isinstance(obj, Cit))
# print(Cit.__c)                     # The __c is hidden to the class
