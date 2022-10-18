def on_received_number(receivedNumber):
    global stop_alarm
    stop_alarm = receivedNumber
radio.on_received_number(on_received_number)

def clear_screen():
    global stop_alarm
    stop_alarm = 0
    music.stop_all_sounds()
    basic.clear_screen()
def alarm_ringing():
    music.start_melody(music.built_in_melody(Melodies.BLUES),
        MelodyOptions.FOREVER_IN_BACKGROUND)
    while stop_alarm == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
        basic.pause(100)
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . # . # .
                        # . . . #
        """)
        basic.pause(100)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
        basic.pause(100)

def on_data_received():
    global serial_input, serial_split, mode, seconds_wait, range_time_boundary, check_range_time_boundary
    serial_input = serial.read_line()
    serial_split = serial_input.split(" ")
    mode = serial_split[0]
    seconds_wait = parse_float(serial_split[1])
    if mode == "set_alarm_time":
        basic.pause(seconds_wait * 1000)
        alarm_ringing()
        clear_screen()
    elif mode == "range_alarm_time":
        basic.pause(seconds_wait * 1000)
        range_time_boundary = 0
        check_range_time_boundary = True
        while check_range_time_boundary == True:
            basic.pause(1000)
            range_time_boundary += 1
            if input.acceleration(Dimension.STRENGTH) > 1500:
                alarm_ringing()
                clear_screen()
                check_range_time_boundary = False
            elif range_time_boundary == 30 * 60000:
                alarm_ringing()
                clear_screen()
                check_range_time_boundary = False
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

check_range_time_boundary = False
range_time_boundary = 0
seconds_wait = 0
mode = ""
serial_split: List[str] = []
serial_input = ""
stop_alarm = 0
serial.redirect_to_usb()
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
radio.set_group(93)
stop_alarm = 0
