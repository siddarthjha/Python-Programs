import tkinter as tk
t = tk.Tk()
print('I am created as a menu for Mr.Jha')
t.title('Menu made By Mr.Jha')


def men():
    print('New file Opened ')
    m = tk.Message(t, text='New file opened')
    m.pack()


def sav():
    print('File has been saved')
    m1 = tk.Message(t, text='file saved')
    m1.pack()


t.geometry('400x300')
m = tk.Menu(t)
f = tk.Menu(m, tearoff=0)
t.config(menu=m)
f.add_command(label='New', command=men)
f.add_command(label='New Project')
f.add_command(label='Open')
f.add_command(label='Save', command=sav)
f.add_command(label='Save as')
f.add_separator()
f.add_command(label='Settings')
f.add_separator()
f.add_command(label='Exit', command=t.quit)
m.add_cascade(label='File', menu=f)
ed = tk.Menu(m, tearoff=0)
ed.add_command(label='Undo')
ed.add_command(label='Redo')
ed.add_separator()
ed.add_command(label='Cut')
ed.add_command(label='Copy')
ed.add_command(label='Copy Path')
ed.add_command(label='Paste')
ed.add_command(label='Delete')
m.add_cascade(label='Edit', menu=ed)
h = tk.Menu(m, tearoff=0)
h.add_command(label='Help')
h.add_separator()
h.add_command(label='About')
m.add_cascade(label='Help', menu=h)
t.mainloop()
