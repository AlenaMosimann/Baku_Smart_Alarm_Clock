def on_received_number(receivedNumber):
    global end_number
    end_number = receivedNumber
radio.on_received_number(on_received_number)

def alarm_reaction():
    music.start_melody(music.built_in_melody(Melodies.BLUES),
        MelodyOptions.FOREVER_IN_BACKGROUND)
    while end_number == 0:
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
    global serial_input, serial_split, cmd, seconds_wait, end_number
    serial_input = serial.read_line()
    serial_split = serial_input.split(" ")
    cmd = serial_split[0]
    seconds_wait = parse_float(serial_split[1])
    if cmd == "set_alarm_time":
        basic.pause(seconds_wait * 1000)
        alarm_reaction()
        end_number = 0
        music.stop_all_sounds()
        basic.clear_screen()
    elif cmd == "range_alarm_time":
        basic.pause(seconds_wait * 1000)
        while True:
            if input.acceleration(Dimension.STRENGTH) > 1500:
                alarm_reaction()
            else:
                music.stop_all_sounds()
                basic.clear_screen()
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

seconds_wait = 0
cmd = ""
serial_split: List[str] = []
serial_input = ""
end_number = 0
serial.redirect_to_usb()
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
radio.set_group(93)
end_number = 0
