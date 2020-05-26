import tkinter as tk
print('I am created to know about text widget to Mr.Jha')
t = tk.Tk()

s = tk.Scrollbar(t)
s.pack(side=tk.RIGHT, fill=tk.Y)
t1 = tk.Text(t)
t1.pack()
t1.insert(tk.INSERT, 'Haaa ')
t1.insert(tk.END, 'Ok i am text written to understand to Mr.Jha\nAnd in text it consist of multi-line\nYeah this is '
                  'text written by Mr.Jha :)')
t.mainloop()
