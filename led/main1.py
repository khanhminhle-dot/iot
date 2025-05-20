# nhấn nút 2 luần liên tiếp thì sáng còn 1 luần thì tắt

from gpiozero import LED, Button
from time import time, sleep
from signal import pause

led = LED(17)
button = Button(18, pull_up = True)

click_count = 0
last_press_time  = 0

def handle_button_press():
    global last_press_time, click_count
    now = time()
    if now - last_time < 0.5:
        click_count += 1
    else :
        click_count == 1
    last_press_time = now
    if click_count == 2:
        led.on()
    elif click_count == 1:
        led.off()
button.when_pressed  = handle_button_press()
pause()