from confluent_kafka import Producer, KafkaError

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_messages(transactional_id, topic_name):
    producer = Producer({
        'bootstrap.servers': 'localhost:9092',
        'transactional.id': transactional_id
    })

    producer.init_transactions()

    try:
        producer.begin_transaction()

        for i in range(10):
            message = f"Transaction message {i}"
            producer.produce(topic_name, message.encode('utf-8'), callback=delivery_report)

        # Commit the transaction
        producer.commit_transaction()
        print("Transaction committed successfully.")

    except Exception as e:
        print(f"Transaction failed: {e}")
        producer.abort_transaction()

    producer.flush()

if __name__ == "__main__":
    produce_messages("my-transactional-id", "transactional-topic")
