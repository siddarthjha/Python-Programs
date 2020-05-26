import tkinter as tk
t = tk.Tk()
t.geometry('300x150')
print('This program demonstrates about creation of Radiobutton to Mr.Jha')


def sel():
    s = 'You have selected '+str(r.get())
    l.config(text=s)


r = tk.StringVar()
r.set('C')
l1 = tk.Label(text='Select a Language to learn under Mr.Jha ')
l1.pack()
R1 = tk.Radiobutton(t, text="C", variable=r, value='C')
R1.pack(anchor=tk.W)
r2 = tk.Radiobutton(t, text='Java', variable=r, value='Java')
r2.pack(anchor=tk.W)
r3 = tk.Radiobutton(t, text='Python', variable=r, value='Python')
r3.pack(anchor=tk.W)
b = tk.Button(t, text='Submit', command=sel)
b.pack(anchor=tk.W)
l = tk.Label(t)
l.pack()
t.mainloop()
