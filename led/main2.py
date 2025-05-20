# khi nhấn thì sang thả ra thì tối

from gpiozero import LED, Button
from signal import pause
leb = LED(17)
button = Button(18, pull_up = True)

# khi nhấn when_pressed

button.when_pressed = leb.on()
button.when_released = leb.off()

pause()