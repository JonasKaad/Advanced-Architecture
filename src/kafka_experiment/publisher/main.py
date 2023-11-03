from client import get_producer, DEFAULT_TOPIC, produce_msg, get_consumer
import time

start_time = 0
end_time = 0
msg_count = 1
msg_amount = 1000
timings = []
start_topic = "experiment-1"

def load_payload():
    return ""

def main():
    global msg_count
    global msg_amount
    global start_topic
    producer = get_producer()
    payload = load_payload()
    while(msg_count <= msg_amount):
        msg = str(msg_count) + payload
        start_time = time.perf_counter()
        producer.send(start_topic, msg)
        break
        


if __name__ == "__main__":
    main()
