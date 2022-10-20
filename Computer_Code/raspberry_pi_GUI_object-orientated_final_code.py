from tkinter import ttk
import datetime as dt
import serial
from tkinter import *
from time import strftime
from PIL import ImageTk, Image
from constants import *





class AlarmClock:
    def __init__(self, master):
        '''This function initialises the "start_frame" and "main_frame". To the "master" (parameter) the widgets will
        be attached. The two different frames are split into two methods to break up the code and increase readability.'''
        self.init_start_frame(master)
        self.init_main_frame(master)

    def init_start_frame(self, master):
        '''The method "init_start_frame" creates the "start_frame" and adds Baku's eyes and the "time_label" which
        shows the current time. By pressing the "Alarm Time" button you switch from the "start_frame" to the "main_frame".'''
        # Create "start_frame" (shows time and Baku's eyes)
        self.start_frame = Frame(master, width=500, height=500, background='#a33651') # The "self." makes the variable global inside of the class
        self.start_frame.grid(row=0, column=0, sticky="news")

        # Get today's date
        self.t = dt.datetime.today()

        # Baku's eyes get appended to the frame
        # Logic from Andrew Clark
        image = ImageTk.PhotoImage(Image.open("eyesBaku.png").resize((96, 137))) # Variables without the "self." can only be referenced in the method (local variable)
        baku_eyes_label = Label(self.start_frame)
        baku_eyes_label.image = image
        baku_eyes_label.configure(image=image, borderwidth=0)
        baku_eyes_label.grid(row=2, column=0, pady=(20,5))
        
        # The "time_label" displays the current time
        self.time_label = Label(self.start_frame, font=('calibri', 40, 'bold'), background='#a33651', foreground='#fffdd0')
        self.time_label.grid(row=3, column=0, padx=50, pady=20)
        self.time()

        # The "start" button raises the main_frame (visible) so that it is on top of the start_frame (not visible)
        raise_main_frame_button = Button(self.start_frame, text= "Alarm Time", command=lambda:self.raise_frame(self.main_frame), background='#fffdd0')
        raise_main_frame_button.grid(row=4, column=0)

    def init_main_frame(self, master):
        # Create "main_frame" (contains Combobox to get User Input, Buttons and Labels)
        self.main_frame = Frame(master, width=500, height=500, background='#a33651')
        self.main_frame.grid(row=0, column=0, sticky="news")

        # Makes sure that at the beginning the start_frame is on top of the main_frame (start default)
        self.raise_frame(self.start_frame)


        # Combobox for a set time
        # Select hour
        self.set_hour_click = StringVar(self.main_frame, INITIAL_HOUR) # This variable stores the value selected in the combobox (same for a time range)
        set_hour_drop = ttk.Combobox(self.main_frame, width=10, textvariable=self.set_hour_click, values=HOURS)
        set_hour_drop.grid(row=1, column=1, padx=10, pady=(30, 3))

        # Select minute
        self.set_min_click = StringVar(self.main_frame, INITIAL_MINUTES) # This variable stores the value selected in the combobox (same for a time range)
        set_min_drop = ttk.Combobox(self.main_frame, width=10, textvariable=self.set_min_click, values=MINUTES)
        set_min_drop.grid(row=1, column=2, padx=10, pady=(30, 5))

        # Combobox for a time range
        # Select hour
        self.range_hour_click = StringVar(self.main_frame, INITIAL_HOUR)
        range_hour_drop = ttk.Combobox(self.main_frame, width=10, textvariable=self.range_hour_click, values=HOURS)
        range_hour_drop.grid(row=5, column=1, padx=10, pady=5)

        # Select minute
        self.range_min_click = StringVar(self.main_frame, INITIAL_MINUTES)
        range_min_drop = ttk.Combobox(self.main_frame, width=10, textvariable=self.range_min_click, values=MINUTES)
        range_min_drop.grid(row=5, column=2, padx=10, pady=5)


        # Set alarm time buttons
        # Button to set the alarm time for today
        set_time_button_today = Button(self.main_frame,
                                       text="set alarm for today",
                                       command=lambda: self.alarm_time(
                                           self.set_time_label,
                                           self.t.day,
                                           self.set_hour_click.get(),
                                           self.set_min_click.get(),
                                           "set_alarm_time"),
                                       relief="raised",
                                       background = '#fffdd0')
        set_time_button_today.grid(row=2, column=1, padx=10, pady=10)

        # Button to set the alarm time for tomorrow
        set_time_button_tomorrow = Button(self.main_frame,
                                          text="set alarm for tomorrow",
                                          command=lambda: self.alarm_time(
                                              self.set_time_label,
                                              (self.t.day+1),
                                              self.set_hour_click.get(),
                                              self.set_min_click.get(),
                                              "set_alarm_time"),
                                          relief="raised", 
                                          background = '#fffdd0')
        set_time_button_tomorrow.grid(row=2, column=2, padx=10, pady=10)

        # Set alarm time label
        self.set_time_label = Label(self.main_frame, text=" ", background='#a33651')
        self.set_time_label.grid(row=3, column=2)


        # Range alarm time buttons
        # Button to start the range alarm time today
        range_time_button_today = Button(self.main_frame, 
                                         text="range alarm for today", 
                                         command=lambda: self.alarm_time(
                                             self.range_time_label, 
                                             self.t.day,
                                             self.range_hour_click.get(), 
                                             self.range_min_click.get(), 
                                             "range_alarm_time"), 
                                         relief="raised", 
                                         background = '#fffdd0')
        range_time_button_today.grid(row=6, column=1, padx=10, pady=10)

        # Button to start the range alarm time tomorrow
        range_time_button_tomorrow = Button(self.main_frame, 
                                            text="range alarm for tomorrow", 
                                            command=lambda: self.alarm_time(
                                                self.range_time_label, 
                                                (self.t.day+1),
                                                self.range_hour_click.get(), 
                                                self.range_min_click.get(), 
                                                "range_alarm_time"), 
                                            relief="raised", 
                                            background = '#fffdd0')
        range_time_button_tomorrow.grid(row=6, column=2, padx=10, pady=10)

        # Range alarm time label
        self.range_time_label = Label(self.main_frame, text=" ", background='#a33651')
        self.range_time_label.grid(row=7, column=2)
        

        # The "Restart" button clears the screen (empties the labels).
        clear_screen_button = Button(self.main_frame, text="Restart", command=self.clear_screen, background='#fffdd0')
        clear_screen_button.grid(row=10, column=1)

        # The "Clock" button raises the start_frame (visible) so that it is on top of the main_frame (not visible)
        raise_start_frame_button = Button(self.main_frame, text= "Clock", command=lambda:self.raise_frame(self.start_frame), background='#fffdd0')
        raise_start_frame_button.grid(row=10, column=2)

    def time(self):
        # Based on: https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/ [retrieved 07. August 2022]
        '''The method "time" configures the text of the label "time_label" so that the current time is displayed'''
        self.time_label.config(text = strftime('%H:%M:%S'))
        self.time_label.after(1000, self.time)
    
    def raise_frame(self, frame):
        '''The method "raise_frame" raises one frame above another (only the top frame is visible)'''
        frame.tkraise()

    # Send a command to the micro:bit and show the response
    def serial_output(self, action):
        # Based on: https://funprojects.blog/2019/05/21/control-microbits-from-your-pc/ [retrieved 24. August 2022]
        '''The method "serial_output" takes the parameter "action" ("set_alarm_time" or "range_alarm_time" + seconds
        until awakening, type str). The string variable "action" is sent to the microbit via serial connection (output).
        The microbit then waits for the given seconds.'''
        print("Requested action: ",action)
        out = action + "\n" # A new line so the micro:bit can check for received data
        out2 = out.encode('utf_8') # The message sent by serial connection must be encrypted
        ser.write(out2)

    def count_seconds(self, day, hours, minutes):
        '''The method "count_seconds" takes as parameters the day, hour and minutes of the time you want to wake up.
        The return value is the difference in seconds between the current time and the time you want to wake up.'''
        t = dt.datetime.today() # Saves the current time
        time_now = dt.datetime(t.year, t.month, t.day, t.hour, t.minute, t.second)
        wake_up = dt.datetime(t.year, t.month, day, hours, minutes)
        seconds = int((wake_up-time_now).total_seconds())
        return seconds

    def alarm_time(self, time_label, day, hour_click, min_click, mode):
        '''The method "alarm_time" takes the following parameters: the time label ("range_time_label" or "set_time_label"),
        the day you want to wake up, the hour and minute selected in the combobox and the mode ("set_alarm_time" or "range_alarm_time").
        The method configures the time label and sends the mode and seconds to the microbit via the serial connection.'''
        time_label.config(text=f"Alarm set for {hour_click}:{min_click}")
        seconds_wait = self.count_seconds(int(day), int(hour_click), int(min_click))
        self.serial_output(f"{mode} {seconds_wait}")

    def clear_screen(self):
        '''The method "clear_screen" blanks all labels on the screen so a new alarm time can be set.'''
        self.set_time_label.config(text="")
        self.range_time_label.config(text="")




# Configuring the serial connection
ser = serial.Serial(port='COM3', baudrate=115200)


# Configuring the GUI window
root = Tk()
root.title("Baku: Smart Alarm Clock")
root.geometry("480x320")
root.configure(background='#a33651')




if __name__=="__main__": # The code is only run if the program is run directly, and not imported
    clock = AlarmClock(root) # Creating the class object "clock"
    root.mainloop()
