import tkinter as tk
print('I am a kind of user login created by Mr.Jha')
p = tk.Tk()
p.title('Login Page')


def fun():
    print('You have login to Mr.Jha creation')
    m = tk.Message(p, text='You have login to Mr.Jha creation')
    m.pack(side='top')


print('I have made Mr.Jha login to make him understand about Tkinter ')
p.geometry('400x250')
l = tk.Label(p, text='Username')
l.place(x=30, y=50)
l1 = tk.Label(p, text='Password')
l1.place(x=30, y=100)
e = tk.Entry()
e.place(x=90, y=50)
e1 = tk.Entry()
e1.place(x=90, y=100)
s = tk.Button(p, text='Login', command=fun, fg='Red', bg='Yellow', activebackground='Pink', activeforeground='Green')
s.place(x=120, y=140)

p.mainloop()
