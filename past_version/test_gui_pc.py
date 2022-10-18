from tkinter import *
from time import strftime


root = Tk()
root.geometry("300x200")
frame = Frame(root)
frame.pack()


def time():
    lbl.config(text = strftime('%H:%M'))
  

lbl = Label(frame, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
  

lbl.pack(anchor = 'center')
time()



def destroy():
    frame.destroy()



stop_button = Button(frame, text= "start", command=destroy)
stop_button.pack()




root.mainloop()
