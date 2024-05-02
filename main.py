from tkinter import *
from PIL import ImageTk, Image
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

root = Tk()
root.title("My Paint")
root.geometry("1100x600")


# -----------------------------------variables------------------------------------------
# stroke size options
options = [1, 2, 3, 4, 5, 10, 20, 40]

stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("black")

previous_color = StringVar()
previous_color.set("white")

previous_color_2 = StringVar()
previous_color_2.set("black")

# variables for pencil

prev_point = [0, 0]
current_point = [0, 0]


# variables for text
text_value = StringVar()


# ---------------------------------functions---------------------------------
# Tools frame
def use_pencil():
    stroke_color.set("black")
    canvas["cursor"] = "crosshair"


def use_eraser():
    stroke_color.set("white")
    canvas["cursor"] = DOTBOX


def select_color():
    selected_color = colorchooser.askcolor(title="Select Color")
    if selected_color[1] == None:
        selected_color.set("black")
    else:
        stroke_color.set(selected_color[1])
        previous_color_2.set(previous_color.get())
        previous_color.set(selected_color[1])

        previous_color_button["bg"] = previous_color.get()
        previous_color_2_button["bg"] = previous_color_2.get()


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


def save_image():
    try:
        file_location = filedialog.asksaveasfilename(defaultextension="jpg")
        x = root.winfo_rootx()
        y = root.winfo_rooty() + 100
        img = ImageGrab.grab(bbox=(x, y, x + 1100, y + 500))
        img.save(file_location)
        show_image = messagebox.askyesno("Paint App", "Do you want to open this image")
        if show_image:
            img.show()

    except Exception as e:
        messagebox.showinfo("Paint app: ", "Error occured")


def clear():
    if messagebox.askokcancel("Paint app: ", "Do you want to clear everything?"):
        canvas.delete("all")


def create_new():
    if messagebox.askyesno(
        "Paint app:", "Do you want to save before deleting everything?"
    ):
        save_image()
    clear()


def help():
    messagebox.showinfo(
        "Help",
        "1. Click on Select Color Option select specific color\n2. Click on Clear to clear entire Canvas",
    )


def settings():
    messagebox.showinfo("Settings", "Not availeble")


def about():
    messagebox.showinfo(
        "About", "idk what i should put here but somebody said it was good practice"
    )


def write_text(event):
    canvas.create_text(event.x, event.y, text=text_value.get())


# ---------------------------------images------------------------------------------
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


##################################################################################
# ---------------------------------------user interface---------------------------#
##################################################################################

# --------------------------------------------frame1-------------------------------------
# frame1 is toolbar
frame1 = Frame(root, height=100, width=1100)
frame1.grid(row=0, column=0, sticky=NW)

tools_frame = Frame(frame1, height=30, width=30, relief=SUNKEN, borderwidth=3)
tools_frame.grid(row=1, column=0)


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


# Size Frame
size_frame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=3)
size_frame.grid(row=1, column=1)

default_button = Button(size_frame, text="Default", width=10, command=use_pencil)
default_button.grid(row=0, column=0)

size_list = OptionMenu(size_frame, stroke_size, *options)
size_list.grid(row=1, column=0)


size_label = Label(size_frame, text="Size", width=10)
size_label.grid(row=2, column=0)


# color box frame
color_box_frame = Frame(frame1, height=100, width=100)
color_box_frame.grid(row=1, column=2)


color_box_button = Button(
    color_box_frame, text="Select Color", width=10, command=select_color
)
color_box_button.grid(row=0, column=0)

previous_color_button = Button(
    color_box_frame,
    text="Previous",
    width=10,
    command=lambda: stroke_color.set(previous_color.get()),
)
previous_color_button.grid(row=1, column=0)

previous_color_2_button = Button(
    color_box_frame,
    text="Previous 2",
    width=10,
    command=lambda: stroke_color.set(previous_color_2.get()),
)
previous_color_2_button.grid(row=2, column=0)


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


orange_button = Button(
    colors_frame,
    text="Orange",
    bg="orange",
    width=10,
    command=lambda: stroke_color.set("orange"),
)
orange_button.grid(row=0, column=1)

yellow_button = Button(
    colors_frame,
    text="yellow",
    bg="yellow",
    width=10,
    command=lambda: stroke_color.set("yellow"),
)
yellow_button.grid(row=1, column=1)

purple_button = Button(
    colors_frame,
    text="Purple",
    bg="purple",
    width=10,
    command=lambda: stroke_color.set("purple"),
)
purple_button.grid(row=2, column=1)

# save image frame
save_image_frame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=2)
save_image_frame.grid(row=1, column=4)

save_image_button = Button(save_image_frame, text="Save", width=10, command=save_image)
save_image_button.grid(row=0, column=0)

new_image_button = Button(save_image_frame, text="New", width=10, command=create_new)
new_image_button.grid(row=1, column=0)

clear_image_button = Button(save_image_frame, text="Clear", width=10, command=clear)
clear_image_button.grid(row=2, column=0)


# help and settings frame
help_settings_frame = Frame(frame1, height=100, width=100, relief=SUNKEN, borderwidth=2)
help_settings_frame.grid(row=1, column=5)


about_button = Button(help_settings_frame, text="about", width=10, command=about)
about_button.grid(row=0, column=0)

help_button = Button(help_settings_frame, text="help", width=10, command=help)
help_button.grid(row=1, column=0)

settings_button = Button(
    help_settings_frame, text="settings", width=10, command=settings
)
settings_button.grid(row=2, column=0)


# text frame
text_frame = Frame(frame1, height=100, width=200, relief=SUNKEN, borderwidth=2)
text_frame.grid(row=1, column=6)

text_title = Button(text_frame, text="Write your text here:", width=20, command=about)
text_title.grid(row=0, column=0)

text_button = Entry(text_frame, textvariable=text_value, width=20)
text_button.grid(row=1, column=0)

# note frame
note_frame = Frame(frame1, height=100, width=400, relief=SUNKEN, borderwidth=2)
note_frame.grid(row=1, column=7)

note_button = Text(note_frame, bg="white", width=40, height=5)
note_button.grid(row=0, column=0)


# frame 2 is canvas
frame2 = Frame(root, height=500, width=1100, bg="blue")
frame2.grid(row=1, column=0)

canvas = Canvas(frame2, height=500, width=1100, bg="white")
canvas.grid(row=0, column=0)


canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
canvas.bind("<Button-2>", write_text)

root.resizable(False, False)
root.mainloop()
