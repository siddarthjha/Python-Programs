import numpy as np
import numpy.matlib as npm
import matplotlib.pyplot as plt
from sys import getsizeof as size
print('I am the Start of numpy for sole sake of understanding to Mr.Jha')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)  # Default data type is integer
print(a)
print(type(a))
print('The dimension the array-', a.ndim)
print('Each element size is(in Bytes)', a.itemsize)
print('The data type of element is ', a.dtype)
print('Size of array is', a.size)
print('The shape of Array is', a.shape)
a1 = a.reshape(1, 9)
print(a1)
print('The reshape array', a.reshape(1, 9))
print(a[0, 2])
print(a1[0, 8])  # Slicing the array and accessing elements
a2 = np.linspace(5, 15, 4)
print('The evenly spaced values return with in given range', a2)
print('The maximum element', a.max())
print('The minimum element', a.min())
print('The sum of array is', a.sum())
print('The maximum element column wise{0} and minimum element {1}'.format(a.max(axis=0), a.min(axis=0)))
print('Square root =', np.sqrt(a))
print('Standard Deviation =', np.std(a))  # s
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Sum of a and b ndarray is', (a + b))
print('Arrays vertically concatenated-', np.vstack((a, b)))
print('Arrays horizontally concatenated-', np.hstack((a, b)))
a4 = np.dtype(int, True)
print(a4)
d = np.dtype(np.int32)
print(d)
d4 = np.dtype([('salary', np.float)])
arr = np.array([(10000.12,), (20000.50,)], dtype=d4)
print(arr['salary'])
a5 = np.empty((2, 3), dtype=int)
print(a5)
a6 = np.zeros((3, 3), dtype=complex, order='F')
print(a6)
a7 = np.ones((4, 3), dtype=int, order='F')
print(a7)
a8 = np.array([['sid'], ['dar'], ['thk']])
print(type(a8))
l1 = [1, 2, 3, 4, 5, 6]
l2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
a9 = np.asarray(l1)
a10 = np.asarray(l2)
print('We created with multiple list', a10)
print('We created an ndarray from list', a9)
print('Similarly we can create with list and tuple ')
l3 = b'helloo'
print(type(l3))
a11 = np.frombuffer(l3, dtype='S2')  # It used to create array from specified buffer
print(a11)
l4 = iter(l1)
a12 = np.fromiter(l4, dtype=int)  # It returns one dimension ndArray object
print("The dimension ndarray ", a12)
a13 = np.arange(0, 12, 3, int)
print('The array given in the range over certain interval is printed', a13)
a14 = np.linspace(10, 20, 5)
print(a14)
a14 = np.logspace(10, 25, num=6, base=10, endpoint=True, dtype=float)
print(a14)
l5 = [1, 2, 3]
l6 = [4, 5, 6]
a15 = np.array(l5)
a16 = np.array(l6)
c = a16 * a15
print(c)
l6 = [[1, 2, 3], [4, 5, 6]]
a17 = np.array(l6)
a18 = a17 + a16
print(a18)
print('Iterating over Array')
for x in np.nditer(a17):
    print(x, end='')
print('\nThe array to be transposed', a17)
a19 = a17.T
print('The transposed array-', a19)
# Numpy string Functions
print('Concatenation of strings in Numpy')
print(np.char.add(['Hi ', 'Nice '], ['How are you??', 'to meet you :)']))
print(np.char.multiply('Now i will be multiplied into two ', 2))
print(np.char.center('Mr.Jha', 40))
print(np.char.capitalize('i will make capital first letter of this sentence '))
print(np.char.title('i am being written as title '))
print(np.char.lower('I WILL LOWER THE CASE OF THE SENTENCE '))
print(np.char.upper('i will upper the case the sentence '))
print(np.char.split('I will split the sentence given '))
print(np.char.strip('            I will strip the           spaces  only from leading and trailing'))
s1 = "      haa haha    jahaha"
print(np.char.strip(s1))
print(np.char.join('hu yo', 'Hey'))                       # It will join the given string to each continuation of letter
print(np.char.replace(s1, 'haha', 'Heeheee'))
s2 = np.char.encode('Hello', 'cp500')
print('The encoded string is', s2)
print('Now we have decoded the string given passed into the argument in form of cp500')
print('The decoded string is', np.char.decode(s2, 'cp500'))
a20 = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
print('Our Array to perform operations', a20)
print('Th minimum element in the array is', np.amin(a20))
print('The maximum element in the array is', np.amax(a20))
print('The minimum element in the array row wise is', np.amin(a20, 0))
print('The maximum element in the array column wise is', np.amax(a20, 1))
print('Peak to Peak value along axis-0 is ', np.ptp(a20, 0))
print('Peak to Peak value along axis-1 is ', np.ptp(a20, 1))
print('Percentile along 0-axis is', np.percentile(a20, 10, 0))
print('Percentile along 0-axis is', np.percentile(a20, 100, 0))
print('Percentile along 1-axis is', np.percentile(a20, 100, 1))
print('Median along 0-axis', np.median(a20, 0))
print('Median along 1-axis', np.median(a20, 1))
print('Mean along 0-axis', np.mean(a20, 0))
print('Mean along 1-axis', np.mean(a20, 1))
print('Average along 0-axis', np.average(a20, 0))
print('Average along 1-axis', np.average(a20, 1))
print('Numpy Searching and Sorting')
a21 = np.array([[10, 28, 1], [12, 8, 36], [2, 58, 4]])
print(np.sort(a21))
print(a21)
print(np.sort(a21, 0))
d = np.dtype([('name', 'S20'), ('marks', int)])
a22 = np.array([('Siddarth', 74), ('Shristi', 82)], dtype=d)
print('Data sorted in order of marks', np.sort(a22, order='marks'))
z = np.argsort(a21)
print('These are the indices of the array to be sorted ', np.argsort(a21))
for i in z:
    print(a21[i], end='')

a23 = np.array(['Siddarth', 'Rahul', 'Shristi', 'Priya'])
a24 = np.array([80, 70, 74, 90])
z2 = np.lexsort((a23, a24))
print('Indices', z2)
for i in z2:
    print(a23[i], a24[i])

print(a23.nonzero())
print(a24.nonzero())
print(a22.nonzero())
print('It returns the indices of the condition true in array', np.where(a24 > 74))
print('Original Array', a24)
print('id of original array', id(a24))
a25 = a24
z1 = a24.view()
print('Referenced array(Assigning)', a25)
print('id of referenced array(Assigning)', id(a25))
print('Changes done on referenced array(Assigning)')
a25.shape = 2, 2
print('The referenced array after changes(Assigning)', a25)
print('This also affected the original array(Assigning)', a24)
print('id of view', id(z1))
print('id of original array', id(a24))
print('The view array(View)', z1)
z1.shape = 4, 1
print('Changes made to the view array(View)', z1)
print('But it didn\'t affect the original array(View)', a24)
# print('View', a24.view())
z3 = a24.copy()
print('id of copy array(Copy)', id(z3))
print('id of original array', id(a24))
z3.shape = 1, 4
print('Changes made to the copy array(Copy)', z3)
print('But it didn\'t affect original array', a24)
# NUMPY MATRIX LIBRARY
print('Numpy Matrix Library')
print(npm.empty((3, 3), dtype=int, order='F'))
print('Zeroes', npm.zeros((2, 3)))
print('Ones', npm.ones((1, 3)))
print('Eye function', npm.eye(3, 3, 0, int))
print('Identity', npm.identity(3, dtype=int))
print('Random', npm.rand(3, 3))
# NUMPY LINEAR ALGEBRA
print('Numpy Linear Algebra')
a26 = np.array([[10, 20], [30, 40]])
a27 = np.array([[50, 60], [70, 80]])
print(a26)
print(a27)
print('The dot product is ', np.dot(a26, a27))
print('The vector dot product is', np.vdot(a26, a27))
print('The inner function is', np.inner(a26, a27))
print('The matrix multiplication is', np.matmul(a26, a27))
print('The determinant of the matrix is', np.linalg.det(a26))
print('The solving of matrix in quadratic equation is', np.linalg.solve(a26, a27))
print('The inverse of matrix is', np.linalg.inv(a26))
print('The inverse of another matrix is', np.linalg.inv(a27))
print('Now Some extra information and knowledge on Numpy')
c = np.array([10, 20, 8, 90])
print(c)
plt.plot(c)
plt.show()
x = range(1, 10)
print(x)
dt2 = np.dtype([('Name', 'S20'), ('Semester', 'i1'), ('Course', 'S10')])
a29 = np.array([('Siddarth', 5, 'CSE'), ('Rahul', 5 ,'CSE'), ('Shristi', 5 ,'CSE')], dtype=dt2)
print(a29['Name'])