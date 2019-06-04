from sense_hat import SenseHat
import time

sense = SenseHat()
hold_time = 10
clear_time = 1
intensity = 175

while True:
    
    sense.clear()
    time.sleep(clear_time)
    msg = "COLOR THEORY"
    sense.show_message(msg, scroll_speed=0.1, text_colour=[intensity, intensity, intensity])

    time.sleep(clear_time)
    # PRIMARY COLORS
    for i in range(8):  sense.set_pixel(1,7-i, [intensity, 0, 0])
    for i in range(8):  sense.set_pixel(3,7-i, [0, intensity, 0])
    for i in range(8):  sense.set_pixel(5,7-i, [0, 0, intensity])
    time.sleep(hold_time)

    # WHITE
    sense.clear()
    time.sleep(clear_time)
    for i in range(8):  sense.set_pixel(2,7-i, [intensity, intensity, intensity])
    for i in range(8):  sense.set_pixel(3,7-i, [intensity, intensity, intensity])
    for i in range(8):  sense.set_pixel(4,7-i, [intensity, intensity, intensity])
    for i in range(8):  sense.set_pixel(5,7-i, [intensity, intensity, intensity])
    time.sleep(hold_time)
    
    # SECONDARY COLORS
    sense.clear()
    time.sleep(clear_time)
    for i in range(8):  sense.set_pixel(1,7-i, [intensity, intensity, 0])
    for i in range(8):  sense.set_pixel(3,7-i, [intensity, 0, intensity])
    for i in range(8):  sense.set_pixel(5,7-i, [0, intensity, intensity])
    time.sleep(hold_time)
    
