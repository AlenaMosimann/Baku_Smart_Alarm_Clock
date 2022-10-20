from microbit import *
import radio
radio.on()
flag = True

while True:
    sleep(20)
    if button_a.was_pressed():
        flag = not flag
    elif flag:
        print((accelerometer.get_values(), ))







