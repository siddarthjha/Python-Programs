import tkinter as tk
root = tk.Tk()
root.geometry('400x250')
counter = 0
print('I have made a counting seconds for Mr.Jha')


def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


root.title("Counting Seconds Created by Mr.jha")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()