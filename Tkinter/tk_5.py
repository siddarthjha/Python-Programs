import tkinter as tk
t = tk.Tk()
print('I am created to make understand about Listbox to Mr.Jha')
''''
This was made for Frame but it was nothing different.... ;)
t.geometry('200x200')
f = tk.Frame(t)
f.pack(side='left')
b = tk.Button(t, text='button1', fg='Blue', bg='red', activebackground='Blue')
b.pack(side='right')
b1 = tk.Button(t, text='Button2', fg='Black', bg='Green', activebackground='pink')
b1.pack(side='left')
'''

t.geometry('250x250')
lb1 = tk.Label(t, text='The students in Mr.Jha project')
lb = tk.Listbox(t)
lb.insert(1, 'Siddarth')
lb.insert(2, 'Shristi')
lb.insert(3, 'Priya')
lb.insert(4, 'Rahul Yadav')
b = tk.Button(t, text='Delete', command=lambda lb=lb: lb.delete(tk.ANCHOR))
lb1.pack()
lb.pack()
b.pack()
t.mainloop()