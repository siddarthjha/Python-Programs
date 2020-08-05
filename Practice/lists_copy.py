l = [1, 2, 3]
l1 = l
# Now if we change the list l1 the list l will also get change because both are pointing to same memory location
print(id(l), id(l1))
print(l, l1)
l1[0] = 4
print(id(l), id(l1))
print(l, l1)
# So to avoid this proble we copy the list with slicing operator.
l1 = l[:]
print(id(l1), id(l))
print(l1, l)
# It is good for only lists as soon we introduce sublists the same problem arises
l2 = [1, 2, 3, [4, 5, 6]]
l3 = l2[:]
# Here if you want to change the first three elements there will be no problem.
# But when you change the sublist then the problem arises
l3[3][1] = 7
print(l3, l2)
# So to avoid the sublists problem we deepcopy module from copy
from copy import deepcopy
l3 = [1, 2, 3, [4, 5, 6]]
l4 = deepcopy(l3)
l3[3][7] = 7
print(l3, l4)
# Now the problem is solved and you can copy and update as you wish without any problem


      


