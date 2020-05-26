import tkinter as tk
t = tk.Tk()
print('I am consisting of check buttons for Mr.Jha')
t.geometry('400x400')
l1 = tk.Label(t, text='Please select the language you want to get training by Mr.Jha ')
l1.pack(side='top')
cv1 = tk.IntVar()
cv2 = tk.IntVar()
cv3 = tk.IntVar()


def fun():
    print('Selected languages is \n C=%d, Java=%d, Python=%d' % (cv1.get(), cv2.get(), cv3.get()))
    m = tk.Message(t, text='Thank you for choosing the subject. \n All the Best...')
    m.place(x=120, y=220)


c1 = tk.Checkbutton(t, text='C', variable=cv1, offvalue=0, onvalue=1, height=2, width=10)
c2 = tk.Checkbutton(t, text='Java', variable=cv2, offvalue=0, onvalue=1, height=2, width=10)
c3 = tk.Checkbutton(t, text='Python', variable=cv3, offvalue=0, onvalue=1, height=2, width=10)
b = tk.Button(t, text='Submit', fg='Red', bg='Yellow', command=fun)
b1 = tk.Button(t, text='Close', fg='Red', bg='Green', command=t.quit)
c1.pack()
c2.pack()
c3.pack()
c1.place(x=52, y=30)
c2.place(x=58, y=60)
c3.place(x=65, y=90)
b.place(x=80, y=140)
b1.place(x=160, y=140)
t.mainloop()
