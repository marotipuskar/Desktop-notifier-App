from tkinter import *

win = Tk()
win.title("Desktop Notifier App window")
win.geometry("600x400")

# Function to load and set a background image
def set_background():
    # Load the image
    background_image = PhotoImage(file="h.ico")  # Replace "background_image.png" with your image file path
    
    # Create a label with the image
    background_label = Label(win, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Make sure the image is not garbage collected
    background_label.image = background_image

# Call the function to set the background image
set_background()

# Your other widgets can be added on top of this background
label = Label(win, text="Welcome To Desktop Notifier App", font=('Helvetica 17 bold'))
label.pack()

win.mainloop()
