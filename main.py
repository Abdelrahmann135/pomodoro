from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
reps = 0
timers = ""


def reset():
    global reps
    reps = 0
    window.after_cancel(timers)
    label1.config(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    label2.config(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"))
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def phases():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer(60 * LONG_BREAK_MIN)
        label1.config(text="Long Break", fg=RED, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    elif reps % 2 == 0:
        timer(60 * SHORT_BREAK_MIN)
        label1.config(text="Short Break", fg=PINK, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
    else:
        timer(60 * WORK_MIN)
        label1.config(text="Work time", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start():
    phases()


def timer(count):
    global timers
    mint = floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{mint}:{sec}")
    if count > 0:
        timers = window.after(1000, timer, count - 1)
    else:
        phases()
        marks = ""
        for _ in range(floor(reps / 2)):
            marks += "/"
        label2.config(text=marks, fg=GREEN, font=(FONT_NAME, 15, "bold"))

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
label1 = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label1.grid(column=2, row=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
button1 = Button(text="Start", highlightthickness=0, command=start)
button1.grid(column=1, row=3)
button2 = Button(text="Reset", highlightthickness=0, command=reset)
button2.grid(column=13, row=3)
label2 = Label(text="", fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
label2.grid(column=2, row=4)
window.mainloop()
