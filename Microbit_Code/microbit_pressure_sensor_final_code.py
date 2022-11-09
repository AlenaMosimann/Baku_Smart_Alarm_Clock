def on_pin_pressed_p0():
    radio.send_number(stop_alarm)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

stop_alarm = 0
radio.set_group(93)
stop_alarm = 1
