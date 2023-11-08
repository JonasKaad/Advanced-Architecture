from kafka import KafkaProducer, KafkaConsumer
import time

start_time = 0
msg_count = 1
msg_amount = 1000
timings = []
start_topic = "experiment-1"
end_topic = "experiment-2"
broker = ("strimzi-kafka-bootstrap:9092")
need_to_send = True
text = "lol"

with open("1mb.txt") as f:
    text = f.read()

def send_msg(producer):
    global text
    global msg_count
    global start_topic
    global need_to_send
    global start_time
    payload = text
    msg = str(msg_count) + payload
    start_time = time.perf_counter()
    producer.send(start_topic, bytes(msg, 'utf-8'))
    producer.flush()
    need_to_send = False

def recv_msg(consumer):
    global start_time
    global timings
    global need_to_send
    global msg_count
    records = consumer.poll(500)
    for topic_data, consumer_records in records.items():
        for record in consumer_records:
            if(int(record.value.decode('utf-8'))==msg_count):
                end_time = time.perf_counter()
                elapsed = end_time - start_time
                timings.append(elapsed)
                msg_count += 1
                need_to_send = True
    

def main():
    global msg_count
    global msg_amount
    global broker
    global need_to_send
    global end_topic
    time.sleep(30) #Wait for echo to be started
    producer = KafkaProducer(bootstrap_servers=[broker])
    consumer = KafkaConsumer(end_topic, bootstrap_servers=[broker])
    consumer.poll(2000) # Dummy poll
    print("starting experiment")
    while(msg_count <= msg_amount):
        if(need_to_send):
            time.sleep(0.2)
            send_msg(producer)
        else:
            recv_msg(consumer)
    timings_sum = 0
    for t in timings:
        timings_sum += t
    print("Average timing: " + str(timings_sum/len(timings)) + ", N=" + str(len(timings)), flush=True)
    time.sleep(600)
    


if __name__ == "__main__":
    main()
