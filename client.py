import paho.mqtt.client as paho
import random
import time
client = paho.Client()
client.connect("192.168.18.131", port=22)

while True:
    randomNum = random.randint(0, 5)
    if randomNum == 0:
        client.publish("I'll help you to call for polite")
        break
    elif randomNum == 1:
        client.publish("too close!")
    else:
        client.publish("you're safe")
    time.sleep(5)

client.disconnect()
