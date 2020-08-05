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


      


