from tkinter import *
from functools import partial

def validate_login(username, password):
    print("Username entered:", username.get())
    print("Password entered:", password.get())

# window
tkWindow = Tk()
tkWindow.geometry("400x150")
tkWindow.title("tkinter Login Form - pythonexample.org")

# username label and text entry box
usernameLabel = Label(tkWindow, text="Username").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show="*").grid(row=1, column=1)

validateLogin = partial(validate_login, username, password)

# Login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=2, column=0)

tkWindow.mainloop()
