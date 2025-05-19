from flask import Flask, render_template, jsonify
import datetime
from gpiozero import LED, Button
import signal
import sys

app = Flask(__name__)
led = LED(27)
button = Button(17, pull_up=True)

def button_pressed_callback():
    led.toggle()
    print("Button pressed. LED is now:", "ON" if led.is_lit else "OFF")
    button.when_pressed = button_pressed_callback

@app.route("/")
def index():
    return render_template("main.html")
@app.route("/status")
def status():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        'led_state': "ON" if led.is_lit else "OFF",
        'time': now
    })
def cleanup(signal_received=None, frame=None):
    print("\nCleaning up GPIO and exiting...")
    led.close()
    button.close()
    sys.exit(0)
signal.signal(signal.SIGINT, cleanup)
if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=False)
    finally:
        cleanup()