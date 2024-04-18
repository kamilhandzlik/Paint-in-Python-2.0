from tkinter import *

root = Tk()
root.title("My Paint")
root.geometry("1100x600")


frame1 = Frame(root, height=100, width=1100, bg="red")
frame1.grid(row=0, column=0)

frame2 = Frame(root, height=500, width=1100, bg="blue")
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)


def paint(event):
    x = event.x
    y = event.y
    canvas.create_line(x, y, 120, 120, fill="black")


canvas.bind("<Button-1>", paint)

root.resizable(False, False)
root.mainloop()
