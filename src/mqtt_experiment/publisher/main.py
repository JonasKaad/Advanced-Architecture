# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = "mosquitto"
port = 1883
topic = "topic/experiment"
# Generate a Client ID with the publish prefix.
client_id = f"publish-timer"

start_time = 0 
end_time = 0 
msg_count = 1
msgs_to_send = 1000
timings = []

payload = "lol"

with open("1mb.txt") as f:
    payload = f.read()

print("Loaded payload with " + str(len(payload)) + " chars", flush=True)

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
    client.subscribe(topic+"-reply")
    return client

def send_one_message(client):
    global msg_count
    global msgs_to_send
    global start_time
    global timings
    global payload
    if(msg_count > msgs_to_send):
        client.loop_stop()
        print("Stopping test", flush=True)
        sum = 0
        for t in timings:
            sum += t
        print("Average timing: " + str(sum/len(timings)) + ", N=" + str(len(timings)), flush=True)
        return
    print("Sending one message", flush=True)
    msg = str(msg_count) + payload
    start_time = time.perf_counter()
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Sent `{msg[0:10]}...` ({len(msg)} chars) to topic `{topic}`", flush=True)
    else:
        print(f"Failed to send message to topic {topic}", flush=True)
    msg_count += 1



def on_message(client, userdata, message):
    global start_time
    global end_time
    global timings
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    timings.append(elapsed_time)
    print("Round-trip time for `"+ str(message.payload)[0:10] +"...`: ", elapsed_time, flush=True)
    time.sleep(0.1)
    send_one_message(client)


def run():
    global msg_count
    print("Starting publisher.. (Waiting 2 seconds)", flush=True)
    time.sleep(2)
    client = connect_mqtt()
    client.loop_start()
    print("Starting message loop in 2 seconds", flush=True)
    time.sleep(2)
    send_one_message(client) #Start the loop
    while True:
        time.sleep(1)


if __name__ == "__main__":
    run()
