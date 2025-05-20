import requests
import time
from gpiozero import LED, Button
from signal import pause

leb = LED(17)

response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    data = response.json() # trả về list user
    for user in data:
        print(user["id"], user["name"], user["username"])
        id = int(user["id"])
        if id % 2 == 0:
            leb.on()
        else:
            leb.off()
        time.sleep(1) 
else:
    print("call Api fail")
pause()