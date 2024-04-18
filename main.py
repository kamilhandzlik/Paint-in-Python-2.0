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


# variables for pencil

prev_point = [0, 0]
current_point = [0, 0]


def paint(event):
    global prev_point
    global current_point
    x = event.x
    y = event.y
    current_point = [x, y]
    canvas.create_oval(x, y, x + 1, y + 1, fill="black")

    if prev_point != 0:
        canvas.create_line(
            prev_point[0], prev_point[1], current_point[0], current_point[1]
        )

    prev_point = current_point


canvas.bind("<B1-Motion>", paint)

root.resizable(False, False)
root.mainloop()
