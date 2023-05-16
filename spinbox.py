# gui program to create a Spinbox widget using tkinter module

import tkinter as tk

root = tk.Tk()
text_var = tk.DoubleVar()

spin_box = tk.Spinbox(
    root,
    from_=0.6,  # Added an underscore after "from"
    to=50.0,
    increment=0.1,
    textvariable=text_var  # Added a comma after "0.1"
)
spin_box.pack()
root.mainloop()
