import tkinter as tk
p = tk.Tk()
p.title('Fuck off giphy')
print('I have inserted a image on window to Mr.Jha')
p.geometry('400x400')
l1 = tk.PhotoImage(file='giphy.gif')
w = tk.Label(p, image=l1).pack(side='right')
w1 = tk.Label(p, justify=tk.LEFT, padx=10, text='Fuck off').pack(side='left')

p.mainloop()
