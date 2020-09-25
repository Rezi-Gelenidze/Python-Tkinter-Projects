from tkinter import *
from PIL import ImageTk, Image
import os


def scan_for_images():
    ''' Function that checks and finds all 
    image filesin a current directory. Then
    it stores all image filenames in a list.'''

    filenames = os.listdir()
    images = []

    for filename in filenames:
        try:
            image = Image.open(filename)
        except:
            pass
        else:
            images.append(filename)
            image.close()

    return images


def check_buttons():
    global button_back
    global button_forward

    if current_index == 0:
        button_back["state"] = DISABLED
    else:
        button_back["state"] = NORMAL

    if current_index == image_filenames.index(image_filenames[-1]):
        button_forward["state"] = DISABLED
    else:
        button_forward["state"] = NORMAL


def view_another_image(direction):
    global image_widget
    global image_file
    global current_index

    if direction == "forward":
        current_index += 1
    else:
        current_index -= 1

    image_file = ImageTk.PhotoImage(Image.open(image_filenames[current_index]))
    image_widget["image"] = image_file

    check_buttons()


# Get all image filenames
image_filenames = scan_for_images()
current_index = 0
# create root window
root = Tk()
root.title("Image Viewer")

#---define widgets
# forward and back buttons
button_forward = Button(root, text=">>", command=lambda : view_another_image("forward"))
button_back = Button(root, text="<<", command=lambda : view_another_image("back"), state=DISABLED)

# image (label)
if image_filenames:
    image_file = ImageTk.PhotoImage(Image.open(image_filenames[0]))
    image_widget = Label(root, image=image_file)
else:
    # display message
    image_widget = Label(root, text="Images not found")
    
    # disable buttons (forward is already disabled)
    button_forward["state"] = DISABLED

#---grid widgets
button_forward.grid(row=1, column=1)
button_back.grid(row=1, column=0)
image_widget.grid(row=0, column=0, columnspan=2)

root.mainloop()
