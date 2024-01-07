from time import *
from tkinter import *
from tkinter import messagebox


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    time_label.after(250, update)

def full(events):
    if window.attributes('-fullscreen') == True:
        window.config(window.attributes('-fullscreen', False))
    elif window.attributes('-fullscreen') == False:
        window.config(window.attributes('-fullscreen', True))


window = Tk()
window.geometry("1000x500")
window.title("Clock")
window['background'] = "#141414"

window.bind("<F11>", full)

time_label = Label(window, font=("Terminal", 100), bg = "#141414", fg="white")
time_label.pack(expand=True)

update()

window.mainloop()