from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("My Clock")
label = Label(root,font=("ds-digital",80),background='black',foreground='red')
label.pack(anchor='center')
def fetchtime():
    t=strftime('%H %M %S : %p')
    label.config(text=t)
    label.after(1000,fetchtime)
fetchtime()
root.mainloop()