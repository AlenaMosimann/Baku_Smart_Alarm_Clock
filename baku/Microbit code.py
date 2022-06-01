from microbit import *

def check_movement_pulse():
    move_strength = input.acceleration(Dimension.STRENGTH)
    if move_strength > 1500:
        basic.show_number(1)
    else:
        basic.show_number(0)

while True:
    check_movement_pulse()
