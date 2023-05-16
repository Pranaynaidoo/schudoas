import tkinter as tk

parent = tk.Tk()
# create the widget
mytext = tk.Text(parent)

# inserta string at the beginning
mytext.insert("1.0", "- Python exercises, solution -")

# insert a string into the current text
mytext.insert("1.19"," practice")

# delete the first and last charecter (includeing a newline charecter)
mytext.delete("1.0")
mytext.delete("end- 2 chars")
mytext.pack()
parent.mainloop()