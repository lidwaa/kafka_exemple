from confluent_kafka.admin import AdminClient, NewTopic

def create_topic(topic_name, num_partitions=3, replication_factor=1):
    admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

    topic = NewTopic(
        topic=topic_name,
        num_partitions=num_partitions,
        replication_factor=replication_factor
    )

    fs = admin_client.create_topics([topic])

    for topic, future in fs.items():
        try:
            future.result()
            print(f"Topic '{topic}' created successfully.")
        except Exception as e:
            print(f"Failed to create topic '{topic}': {e}")

if __name__ == "__main__":
    create_topic("transactional-topic")
