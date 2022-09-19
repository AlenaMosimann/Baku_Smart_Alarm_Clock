from tkinter import *
from time import strftime
from PIL import ImageTk, Image
import ttk
import datetime as dt
import serial



root = Tk()
root.title("Micro:bit")
root.geometry("500x500")
frame1 = Frame(root, width=500, height=500)
frame1.grid(row=0, column=0)
frame2 = Frame(root, width=500, height=500)
frame2.grid(row=0, column=0)
# used in set_alarm_time and range_alarm_time
t = dt.datetime.today()




def time():
    '''This function configures the text of the Label "time_label"
    so that the current time is displayed'''
    time_label.config(text = strftime('%H:%M:%S'))
    time_label.after(1000,time)


def change_frame(frame):
    '''This function swaps the first frame with the second frame (only second frame visible)'''
    frame.tkraise()




# Code for frame1

# Baku's eyes are displayed on the screen
path = "C:/Users/atmos/PycharmProjects/Baku_Smart_Wecker/baku/googly_eyes.png"
raw_image = Image.open(path)
resized_image = raw_image.resize((150, 150))
googly_eyes = ImageTk.PhotoImage(resized_image)
googly_eyes_label = Label(frame1, image=googly_eyes)
googly_eyes_label.grid(row=1, column=0)


# The "time_label" displays the current time
time_label = Label(frame1, font = ('calibri', 40, 'bold'),
            background = 'purple',
            foreground = 'white')
time_label.grid(row=3, column=0)
time()



# Change to frame2

# The button "start" swaps the frames, so frame2 is on top/visible
change_frame_button = Button(frame1, text= "start", command=lambda:change_frame(frame2))
change_frame_button.grid(row=4, column=0)

change_frame(frame1)







# configure the serial connections
ser = serial.Serial(
    port='COM3',
    baudrate=115200)



# Send a command to the micro:bit and show the response
def serial_output(action):
    '''The parameter is the requested action (set_alarm_time or range_alarm_time + seconds until you wake up).
    The action and seconds until you wake up is sent per serial to the microbit (output).
    The micronbit then waits for the given seconds.'''
    print ("Requested action: ",action)
    out = action + "\n"
    out2 = out.encode('utf_8') # the serial response must be encripted
    ser.write(out2)
    lstatus.config(text = ser.readline())


def count_seconds(hours, minutes):
    '''The parameters are the hour and minute you want to wake up. The function
    returns the seconds from the current time until when the time you want to wake up.'''
    time_now = dt.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)
    # for getting up the next morning "t.month" must be "(t.day)+1" because it's the next day!
    wake_up = dt.datetime(t.year, t.month, ((t.day)+1), hours, minutes)
    seconds = int((wake_up-time_now).total_seconds()) # *1000000
    return seconds






# Combobox set alarm time

# select hour
set_hours = ["01","02","03","04","05","06","07","08","09"] + [str(x) for x in range(10,25)]
set_hour_click = StringVar(frame2)
set_hour_click.set("06")
set_hour_drop = ttk.Combobox(frame2, width=10, textvariable=set_hour_click, values=set_hours)
set_hour_drop.grid(row=1, column=1)

# select minute
set_mins = ["00","01","02","03","04","05","06","07","08","09"] + [str(x) for x in range(10,60)]
set_min_click = StringVar(frame2)
set_min_click.set("30")
set_min_drop = ttk.Combobox(frame2, width=10, textvariable=set_min_click, values=set_mins)
set_min_drop.grid(row=1, column=2)





# Combobox range alarm time

# select hour
range_hours = ["01","02","03","04","05","06","07","08","09"] + [str(x) for x in range(10,25)]
range_hour_click = StringVar()
range_hour_click.set("06")
range_hour_drop = ttk.Combobox(frame2, width=10, textvariable=range_hour_click, values=range_hours)
range_hour_drop.grid(row=5, column=1)

# select minute
range_mins = ["00","01","02","03","04","05","06","07","08","09"] + [str(x) for x in range(10,60)]
range_min_click = StringVar()
range_min_click.set("30")
range_min_drop = ttk.Combobox(frame2, width=10, textvariable=range_min_click, values=range_mins)
range_min_drop.grid(row=5, column=2)











# functions for set and range time

def set_alarm_time():
    '''This function runs the code for a set alarm time'''
    set_time_label.config(text = f"Alarm set for {set_hour_click.get()}:{set_min_click.get()}")
    set_seconds_wait = count_seconds(int(set_hour_click.get()), int(set_min_click.get()))
    serial_output(f"set_alarm_time {set_seconds_wait}")
    # serial_output(f"set_alarm_time {seconds_wait}")
    
    
def range_alarm_time():
    '''This function runs the code for a range alarm time'''
    range_time_label.config(text = f"Alarm starts checking at {range_hour_click.get()}:{range_min_click.get()}")
    range_seconds_wait = count_seconds(int(range_hour_click.get()), int(range_min_click.get()))
    serial_output(f"range_alarm_time {range_seconds_wait}")
    # serial_output("range_alarm_time")
    






# set alarm time button and label
set_time_button = Button(frame2, text="set alarm time", command = lambda: set_alarm_time(), relief="raised")
set_time_button.grid(row=2, column=2)

# set alarm time label
set_time_label = Label(frame2, text = " ")
set_time_label.grid(row=3, column=2)





# range alarm time button
range_time_button = Button(frame2, text="range alarm time", command = lambda: range_alarm_time(), relief="raised")
range_time_button.grid(row=6, column=2)

# range alarm time label
range_time_label = Label(frame2, text = " ")
range_time_label.grid(row=7, column=2)




# Label to show message from Microbit
lstatus = Label(frame2, text= "")
lstatus.grid(row = 9, column = 1)





def clear_screen():
    "This function clears all the labels on the screen, so a new alarm time can be set."
    set_time_label.config(text="")
    range_time_label.config(text="")
    lstatus.config(text="")
   

clear_screen_button = Button(frame2, text="Restart", command=clear_screen)
clear_screen_button.grid(row = 10, column = 1)






root.mainloop()
