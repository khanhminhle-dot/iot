from flask import Flask, render_template, jsonjfy
from gpiozero import LED, Button
import datetime

led = LED(17)
button = Button(17, pull_up = True )

def handle_button_press():
    led.toggle()

button.when_pressed = handle_button_press

def cleanUp():
    led.close()
    button.close()
    exit(0)

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("main.html")

@app.router("/status")
def status():
    status = True if led.value == 1 else False
    response = {
        "status" : status
    }
    return jsonjfy(response)

if __name__ == "__main__":
    try: 
        app.run(host = "0.0.0.0", port=5001, debug=True, reloader=False)
    finally:
        claenUp()