from tkinter import *
from tkinter import Tk

root = Tk()
root.title("Scrollbar")
root.geometry("1800x1200")


# select minute
mins = ["05"] + [str(x) for x in range(10,60, 5)]

min_click = StringVar()
min_click.set(30)
min_get_up = min_click.get()

min_drop = OptionMenu(root, min_click, *mins)
min_drop.grid(row=1, column=2)



# select hour
hours = ["01","02","03","04","05","06","07","08","09"] + [str(x) for x in range(10,25)]
print(hours)

hour_click = StringVar()
hour_click.set(6)
hour_get_up = hour_click.get()



hour_drop = OptionMenu(root, hour_click, *hours)
hour_drop.grid(row=1, column=1)


def time_show():
    label.config(text = f"{hour_click.get()}:{min_click.get()}")

button = Button(root, text="click", command = time_show)
button.grid(row=2, column=2)

label = Label(root , text = " ")
label.grid(row=3, column=2)












root.mainloop()



