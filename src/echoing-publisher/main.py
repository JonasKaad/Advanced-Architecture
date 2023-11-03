# python 3.6

import random
import time
from paho.mqtt import client as mqtt_client

broker = "mosquitto"
port = 1883
topic = "topic/experiment"
# Generate a Client ID with the publish prefix.
client_id = f"subscription-replier"


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!", flush=True)
        else:
            print("Failed to connect, return code %d\n", rc, flush=True)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    client.subscribe(topic)
    return client


def on_message(client, userdata, message):
    print("Got message: %s %s" % (message.topic, message.payload), flush=True)
    client.publish(message.topic + "-reply", message.payload)

def run():
    print("Started echoing publisher!", flush=True)
    client = connect_mqtt()
    client.loop_start()
    while True:
        time.sleep(0.5)

if __name__ == "__main__":
    run()
