from sense_hat import SenseHat
import time

sense = SenseHat()
hold_time = 10
clear_time = 1

while True:
    
    sense.clear()
    time.sleep(clear_time)
    msg = "COLOR THEORY"
    sense.show_message(msg, scroll_speed=0.1, text_colour=[100, 100, 100])

    time.sleep(clear_time)
    # PRIMARY COLORS
    for i in range(8):  sense.set_pixel(1,7-i, [100, 0, 0])
    for i in range(8):  sense.set_pixel(3,7-i, [0, 100, 0])
    for i in range(8):  sense.set_pixel(5,7-i, [0, 0, 100])
    time.sleep(hold_time)

    # WHITE
    sense.clear()
    time.sleep(clear_time)
    for i in range(8):  sense.set_pixel(2,7-i, [100, 100, 100])
    for i in range(8):  sense.set_pixel(3,7-i, [100, 100, 100])
    for i in range(8):  sense.set_pixel(4,7-i, [100, 100, 100])
    for i in range(8):  sense.set_pixel(5,7-i, [100, 100, 100])
    time.sleep(hold_time)
    
    # SECONDARY COLORS
    sense.clear()
    time.sleep(clear_time)
    for i in range(8):  sense.set_pixel(1,7-i, [100, 100, 0])
    for i in range(8):  sense.set_pixel(3,7-i, [100, 0, 100])
    for i in range(8):  sense.set_pixel(5,7-i, [0, 100, 100])
    time.sleep(hold_time)
    
