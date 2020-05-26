import tkinter as tk
import tkinter.messagebox as m


t = tk.Tk()
t.geometry('100x100')
s = tk.Message(t)
m.showinfo('Mr.Jha', 'I am message box created by Mr.Jha')


def fun():
    t1 = tk.Toplevel(t)
    t1.mainloop()


b = tk.Button(t, text='Open', command=fun)
b.pack()
t.mainloop()
