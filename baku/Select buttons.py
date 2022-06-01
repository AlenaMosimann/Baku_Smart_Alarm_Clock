from tkinter import *
from tkinter import Tk

root = Tk()
root.title("Scrollbar")
root.geometry("1800x1200")

"""
minute_listbox = Listbox(root)
minute_listbox.pack()
for min in range(5,60, 5):
    minute_listbox.insert(END, min)
# this makes the listbox scrollable (widgets can be made scrollable)

minutes = Scrollbar(root, orient='vertical', command = minute_listbox.yview)
minutes.pack(side = LEFT, fill = BOTH)

minute_listbox.config(yscrollcommand = minutes.set)
"""
def min_show():
    label.config(text = min_click.get())

mins = [str(x) for x in range(5,60, 5)]

min_click = StringVar()
min_click.set(30)

min_drop = OptionMenu(root, min_click, *mins)
min_drop.pack()

button = Button(root, text="click", command = min_show)
button.pack()

label = Label( root , text = " " )
label.pack()





def hour_show():
    h_label.config(text = hour_click.get())



hours = [str(x) for x in range(1,24)]

hour_click = StringVar()
hour_click.set(6)

hour_drop = OptionMenu(root, hour_click, *hours)
hour_drop.pack()

hour_button = Button(root, text="click hour", command = min_show)
hour_button.pack()

h_label = Label( root , text = " " )
h_label.pack()


root.mainloop()



