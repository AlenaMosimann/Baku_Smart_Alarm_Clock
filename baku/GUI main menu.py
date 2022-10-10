from tkinter import *
from math import *

root = Tk()


root.title("Main menu")
root.geometry("1800x1200")
# current_date = Label(root, text=)

radius = 200
angle = 30
oval_position_start = 100
oval_position_end = 500
x_origin = int((oval_position_start + oval_position_end)/2)
y_origin = int((oval_position_start + oval_position_end)/2)
print(x_origin, y_origin)


canvas = Canvas(root, width=1800, height=1200)
canvas.pack()
#canvas.create_oval(100, 100, 500, 500)
canvas.create_oval(oval_position_start, oval_position_start, oval_position_end, oval_position_end)

def circle():
    x = (radius*sin(angle)+radius)
    y = ((radius*cos(angle)-radius)*-1)
    print(x, y)
    canvas.create_line(x_origin, x_origin, x, y)
    """
    canvas.create_line(200,200, 7.713, 9.193)
    """

circle()

root.mainloop()






"""
h=0
m=0

def wait_and_add_degrees(h,m):
    sleep(60)
    h += 0.5
    m += 6


if


elif


elif h == 360:
    h = 0
elif m == 360:
    m = 0
"""









