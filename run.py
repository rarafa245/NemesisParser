import paho.mqtt.client as mqtt
import time

broker = 'localhost'

client = mqtt.Client('NemesisParser')
client.connect(broker)
time.sleep(4)
client.disconnect()