import math
import time
from tkinter import *

# Initialize constants
PINK = "#F8A89D"
RED = "#F1583F"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Create the User Interface
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create the canvas for the image
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

# Create main label
timer_label = Label(text="Timer", font=(
    FONT_NAME, 40, "bold"), fg=RED, background=YELLOW)
timer_label.grid(column=1, row=0)

# Create checkmarks label
checkmarks_label = Label(text="✓", font=(
    FONT_NAME, 40, "bold"), fg=GREEN, background=YELLOW)
checkmarks_label.grid(column=1, row=3)


def start_clicked():
    # When start button is clicked, call the countdown function
    countdown(WORK_MIN * 60)


def reset_clicked():
    # Make Reset button do action
    pass


def countdown(count):
    # Create the timer display

    # Covert seconds to minutes for display
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Display the remaining time
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# Create Start Button
start_button = Button(text="Start", command=start_clicked,
                      highlightthickness=0)
start_button.grid(column=0, row=2)

# Create Reset Button
reset_button = Button(text="Reset", command=reset_clicked,
                      background=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Mainloop has to be at the end of the code
window.mainloop()
