from tkinter import *
from PIL import ImageTk, Image
from tkinter import colorchooser

root = Tk()
root.title("My Paint")
root.geometry("1100x600")

stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("black")


# Loading image
pencil_image = Image.open("pencil.png")
eraser_image = Image.open("eraser.png")
tools_label_image = Image.open("tools label.png")

# Resizing image
resized_pencil = pencil_image.resize((30, 30))
resized_eraser = eraser_image.resize((30, 30))
resized_tools_label = tools_label_image.resize((30, 30))


# Giving resized image variable easier name ;)
pencil_img = ImageTk.PhotoImage(resized_pencil)
eraser_img = ImageTk.PhotoImage(resized_eraser)
tools_label_img = ImageTk.PhotoImage(resized_tools_label)


# frame1 is toolbar
frame1 = Frame(root, height=100, width=1100)
frame1.grid(row=0, column=0, sticky=NW)

tools_frame = Frame(frame1, height=30, width=30, relief=SUNKEN, borderwidth=3)
tools_frame.grid(row=1, column=0)


# Tools frame
def use_pencil():
    stroke_color.set("black")
    canvas["cursor"] = "crosshair"


def use_eraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX


# buttons as images- uncomment if you prefer this version don't forget to change height and width in tool frames  to 30x30
pencil_button = Button(
    tools_frame,
    image=pencil_img,
    height=30,
    width=30,
    command=use_pencil,
    borderwidth=0,
)
pencil_button.grid(row=0, column=0)


eraser_button = Button(
    tools_frame,
    image=eraser_img,
    height=30,
    width=30,
    command=use_eraser,
    borderwidth=0,
)
eraser_button.grid(row=1, column=0)


tools_label = Button(
    tools_frame,
    image=tools_label_img,
    height=30,
    width=30,
    command=lambda: stroke_color.set("white"),
    borderwidth=0,
)
tools_label.grid(row=2, column=0)


# buttons as text - uncomment if you prefer this version don't forget to change height and width in tool frames  to 100x100

# pencil_button = Button(
#     tools_frame, text="Pencil", width=10, command=lambda: stroke_color.set("black")
# )
# pencil_button.grid(row=0, column=0)
# eraser_button = Button(
#     tools_frame, text="Eraser", width=10, command=lambda: stroke_color.set("white")
# )
# eraser_button.grid(row=1, column=0)

# tools_label = Button(tools_frame, text="Tools", width=10)
# tools_label.grid(row=2, column=0)


# Size Frame
size_frame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
size_frame.grid(row=1, column=1)

default_button = Button(size_frame, text="Default", width=10, command=use_pencil)
default_button.grid(row=0, column=0)

options = [1, 2, 3, 4, 5, 6, 20]

size_list = OptionMenu(size_frame, stroke_size, *options)
size_list.grid(row=1, column=0)


size_label = Label(size_frame, text="Size", width=10)
size_label.grid(row=2, column=0)


# color box frame
color_box_frame = Frame(frame1, height=100, width=100)
color_box_frame.grid(row=1, column=2)


def select_color():
    selected_color = colorchooser.askcolor(title="Select Color")
    print(select_color)
    if selected_color[1] == None:
        selected_color.set("black")
    else:
        stroke_color.set(selected_color[1])


color_box_button = Button(
    color_box_frame, text="Select Color", width=10, command=select_color
)
color_box_button.grid(row=0, column=0)

# colors frame
colors_frame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=2)
colors_frame.grid(row=1, column=3)

red_button = Button(
    colors_frame,
    text="Red",
    bg="red",
    width=10,
    command=lambda: stroke_color.set("red"),
)
red_button.grid(row=0, column=0)

green_button = Button(
    colors_frame,
    text="Green",
    bg="green",
    width=10,
    command=lambda: stroke_color.set("green"),
)
green_button.grid(row=1, column=0)

blue_button = Button(
    colors_frame,
    text="Blue",
    bg="blue",
    width=10,
    command=lambda: stroke_color.set("blue"),
)
blue_button.grid(row=2, column=0)

# frame 2 is canvas
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
    # type of code to make brush for future reference canvas.create_oval(x, y, x + 1, y + 1, fill="black")

    if prev_point != [0, 0]:
        canvas.create_polygon(
            prev_point[0],
            prev_point[1],
            current_point[0],
            current_point[1],
            fill=stroke_color.get(),
            outline=stroke_color.get(),
            width=stroke_size.get(),
        )

    prev_point = current_point

    if event.type == "5":
        prev_point = [0, 0]


canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

root.resizable(False, False)
root.mainloop()
