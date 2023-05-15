from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)  # size of the entry field
entry2 = ttk.Entry(root, width=30)
entry.insert(0, "Please enter your name")  # insert default text
entry2.config(show="*")  # show entered text as asterisks

entry.pack()
entry2.pack()

root.geometry("300x300")  # set window size
root.mainloop()
