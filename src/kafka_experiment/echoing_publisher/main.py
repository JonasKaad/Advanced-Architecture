from kafka import KafkaProducer, KafkaConsumer
import time

start_time = 0
msg_count = 1
msg_amount = 1000
timings = []
start_topic = "experiment-1"
end_topic = "experiment-2"
broker = ("strimzi-kafka-bootstrap:9092")
need_to_send = False

def load_payload():
    return ""

def send_msg(producer):
    global msg_count
    global end_topic
    global need_to_send
    payload = load_payload()
    msg = str(msg_count) + payload
    producer.send(end_topic, bytes(msg, 'utf-8'))
    producer.flush()
    msg_count += 1
    need_to_send = False

def recv_msg(consumer):
    global start_time
    global timings
    global need_to_send
    global msg_count
    records = consumer.poll(2000)
    for topic_data, consumer_records in records.items():
        for record in consumer_records:
            if(str(record.value.decode('utf-8'))!=""):
                need_to_send = True
    

def main():
    global msg_count
    global msg_amount
    global broker
    global need_to_send
    global start_topic
    producer = KafkaProducer(bootstrap_servers=[broker])
    consumer = KafkaConsumer(bootstrap_servers=[broker], auto_offset_reset='earliest')
    consumer.subscribe(start_topic)
    print("Starting...")
    initial = consumer.poll(2000)
    print("initial: " + str(initial))
    for topic_data, consumer_records in initial.items():
        for record in consumer_records:
            print("received initial: " + str(int(record.value.decode('utf-8'))))
    while(msg_count <= msg_amount):
        if(need_to_send):
            send_msg(producer)
        else:
            recv_msg(consumer)
    


if __name__ == "__main__":
    main()
