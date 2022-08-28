def on_pin_pressed_p0():
    radio.send_number(end_number)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

end_number = 0
radio.set_group(93)
end_number = 1