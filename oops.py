print('I am created to make understand the OOPS concept to Mr.Jha')
class Emp:

    id = 40
    name = 'Siddarth'
    print(id)
    print(name)

    def __init__(self, i, n):
        self.i = i
        self.n = n
        print('Id=%d and Name:%s' % (i, n))

    def display(self):
        print('ID=%d and Name:%s' % (self.id, self.name))


obj = Emp(39, 'Rajiv')
obj.display()
print(getattr(obj, 'i'))               # Here attribute is retrieved
print(setattr(obj, 'n', 'Shristi'))    # Here attribute is set to the given value
print(getattr(obj, 'n'))               # Here attribute is retrieved  after resetting the value
print(hasattr(obj, 'n'))               # Here attribute is  being checked whether present or not
print(delattr(obj, 'n'))               # Here attribute is being deleted/Removed
print(hasattr(obj, 'n'))               # Here attribute is being checked after deleting the attribute
print(obj.__doc__)                     # Contains class documentation
print(obj.__dict__)                    # Contains dictionary information
print(obj.__module__)                  # Used to access the module in which class is defined
print(obj.__class__)                   # Returns the class name
# print(obj.__name__)                    # Used to access the class name
# print(obj.__bases__)                 # Contains tuple including all base classes