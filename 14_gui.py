"""
basic Button creation and manipulation
"""
import tkinter as tk
print('I have made 4 buttons for Mr.Jha')
p = tk.Tk()
r = tk.Button(p, text='Red', fg='Red')
r.pack(side='left')
b = tk.Button(p, text='Blue', fg='Blue')
b.pack(side='right')
bl = tk.Button(p, text="Black", fg='Black')
bl.pack(side='top')
g = tk.Button(p, text='Green', fg='Green')
g.pack(side='bottom')
w = tk.Label(p, text='Hello Siddarth')
w.pack()
p.mainloop()
