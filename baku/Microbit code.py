from microbit import *

def check_movement_pulse():
    move_strength = input.acceleration(Dimension.STRENGTH)
    if move_strength > 1500:
        basic.show_number(1)
    else:
        basic.show_number(0)

while True:
    check_movement_pulse()

'''
Funktioniert dieser Code so bei Ihnen?
Hier finden Sie z.B. noch etwas Inspiration zum Accelerometer:
https://rothe.io/?page=ref/microbit/5-accelerometer/
'''

'''
Und haben Sies schon geschafft, den micro:bit per Bluetoothe mit dem RaspberryPi zu verbinden? Z.B. so ähnlich:
https://developingfordata.com/2020/10/12/raspberry-pi-microbit/

'''