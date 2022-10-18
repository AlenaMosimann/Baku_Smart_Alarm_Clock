def on_received_number(receivedNumber):
    global getNumber
    getNumber = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(end_number)
input.on_button_pressed(Button.A, on_button_pressed_a)

def alarm_reaction():
    while getNumber != end_number:
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
    global cmd
    cmd = serial.read_line()
    if cmd == "set_alarm_time":
        serial.write_line("Wake up!")
        alarm_reaction()
        music.stop_all_sounds()
        basic.clear_screen()
    elif cmd == "range_alarm_time":
        serial.write_line("Starting to check ...")
        while True:
            if input.acceleration(Dimension.STRENGTH) > 1500:
                alarm_reaction()
            else:
                music.stop_all_sounds()
                basic.clear_screen()
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

cmd = ""
getNumber = 0
end_number = 0
serial.redirect_to_usb()
serial.set_baud_rate(BaudRate.BAUD_RATE115200)
radio.set_group(93)
end_number = 1
