from confluent_kafka import Consumer, KafkaError

def consume_messages(group_id, topic_name):
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': group_id,
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': False,
        'isolation.level': 'read_committed'
    })

    consumer.subscribe([topic_name])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.partition()}")
                else:
                    print(f"Error: {msg.error()}")
                continue

            print(f"Received message: {msg.value().decode('utf-8')}")
            consumer.commit()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages("transactional-group", "transactional-topic")
