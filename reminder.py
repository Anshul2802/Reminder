import time
import pyttsx3
from plyer import notification

engine = pyttsx3.init()

engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)

for i in range (5): #repaet 5 times
    
    time.sleep(3600) #1hour timeout
    # engine.say("It's been 1hour. Drink water now.")
    # engine.runAndWait()
    notification.notify(
        title = "Water Reminder",
        message = "It's been 1hour, don't forget to drink water",
        timeout =10
    )