from tkinter import *

# Initialize constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Create the User Interface
window = Tk()
window.title("Pomodoro")
# window.minsize(width=600, height=400)

# Create the canvas for the image
canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.pack()

# Mainloop has to be at the end of the code
window.mainloop()