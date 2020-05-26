print('Yeah I am created for the sole purpose of understanding Exceptions to Mr.Jha')
try:
    a = int(input('Enter a number for a'))
    b = int(input('Enter a number for b'))
    c=float(a/b)
    print(c)
except ZeroDivisionError:
    print('Divide by zero occurred')
except Exception:
    print('Exception occurred')
else:
    print('Division successfully completed')
finally:
    print('Now lets continue to other')
try:
    f=open('file123.txt', 'r')
    print(f.readline())
# except Exception:
#  print('Exception occurred')
except IOError:
    print('Some error occurred in file cannot open the file')
except ArithmeticError:
    print('Arithmetic Error')
else:
    print('The file opened successfully')
finally:
    print('Here i will always execute because i am Finally block')
try:
    d = int(input('Enter your age'))
    if d < 18:
        raise ValueError;
    else:
        print('You are eligible ')
except ValueError:
    print('You are not eligible')
else:
    print('Successfully completed')
finally:
    print('Let us move to other')


