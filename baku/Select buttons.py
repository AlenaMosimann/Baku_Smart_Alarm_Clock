from tkinter import *
import datetime as dt
import pause

root = Tk()
root.title("Scrollbar")
root.geometry("1800x1200")


# select minute
mins = ["00", "05"] + [str(x) for x in range(10,60, 5)]

min_click = StringVar()
min_click.set("30")
# set minute get up
min_get_up = min_click.get()

min_drop = OptionMenu(root, min_click, *mins)
min_drop.grid(row=1, column=2)


# select hour
hours = ["01","02","03","04","05","06","07","08","09"] + [str(x) for x in range(10,25)]

hour_click = StringVar()
hour_click.set("06")
# set hour get up
hour_get_up = hour_click.get()

hour_drop = OptionMenu(root, hour_click, *hours)
hour_drop.grid(row=1, column=1)


def time_show():
    time_label.config(text = f"{hour_click.get()}:{min_click.get()}")
    t = dt.datetime.today()
    pause.until(dt.datetime(t.year, t.month, t.day, int(hour_click.get()), int(min_click.get())))
    print("hello")
    
    
    # continue code here


time_button = Button(root, text="set time", command = time_show)
time_button.grid(row=2, column=2)

time_label = Label(root , text = " ")
time_label.grid(row=3, column=2)





'''
t = dt.datetime.today()
print(dt.datetime(t.year, t.month, t.day, int(hour_get_up), int(min_get_up)))

pause.until(dt.datetime(t.year, t.month, t.day, int(hour_click.get()), int(min_click.get())))
print("hello")
'''











root.mainloop()


