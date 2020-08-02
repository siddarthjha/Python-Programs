"""
Database(sqlite3) connectivity and query execution.
"""
import sqlite3
print('I am created for Database purpose to understand all functions of sqlite to Mr.Jha :)')
c = sqlite3.connect('python db')
print('Created and Connected Successfully')
# s = "create table student(sap_id int primary key not null, name varchar(30) not null, course varchar(30) not null, year int); "
# c.execute(s)
# print('Table created successfully')
# s1 = "insert into student(sap_id, name, course, year) values (?, ?, ?, ?)"
# v = [(500062120, 'Shristi', 'CSE-Og', 2), (5000123, 'xyz', 'Cse-Og', 3), (500063455, 'Ayushi', 'CSE-Og', 2)]
# c.executemany(s1, v)
# c.commit()
# print('Record successfully inserted')
cur = c.cursor()
print(cur)                                 # This for shit No purpose of this :)
d = c.execute('select * from student')
print('Id\t Name\t Course\t Year')
# for i in d:
#   print(i[0], i[1], i[2], i[3])
r = d.fetchall()
print(r)
for i in r:
    print(i)

c.close()
