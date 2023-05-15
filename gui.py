from tkinter import *

root = Tk()  # top level window

# create label
label = Label(root, text="Hello Python")
label.pack()

def callback():
    label.config(text="You clicked me!", fg="red", bg="yellow")  # added font color and background color on click

# create button(now with the command function)
button = Button(root, text="click me!", command=callback)
button["state"] = "disabled"  # can disable the button
button["state"] = "normal"  # back to normal
button.pack()

root.geometry("350x350")
root.mainloop()
