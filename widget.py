import tkinter as tk

# GUI program to add a button
parent = tk.Tk()
parent.title("Title - Button")
my_button = tk.Button(parent, text="quit", height=1,
                      width=35, command=parent.destroy)
my_button.pack()
parent.mainloop()

# GUI program to add a canvas
parent = tk.Tk()

canvas_width = 100
canvas_height = 80
w = tk.Canvas(parent,
              width=canvas_width,
              height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")
parent.mainloop()
