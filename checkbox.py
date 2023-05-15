# gui program to create a checkbox widget using tkinter module

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_boolean_var = tk.BooleanVar()

my_checkbutton = ttk.Checkbutton(
    root,
    text="Check when the option is True",
    variable=my_boolean_var
)
my_checkbutton.pack()
root.mainloop()
