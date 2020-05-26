print('I am created for the purpose to make understand the modules concept to Mr.Jha')
from functions import func
func('sidd')
import functions as f
f.func('Yeah', 'I am that function', 'hahaha')
s = dir(f)
print(s)
# reload(functions)


def fun_1(a):
    print('Iam second file modules---', a)

