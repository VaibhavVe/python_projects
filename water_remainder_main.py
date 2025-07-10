import time
from plyer import notification

while True:
    print("Please drink water!!!!!")
    notification.notify(title ="Please drink water", message = "Time to drink water")
    time.sleep(60*60)