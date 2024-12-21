# Kafka Transactions Example

This project demonstrates the usage of **Kafka transactions** to guarantee exactly-once delivery of messages. It includes a producer that uses transactions to send messages and a consumer that reads only committed transactions.

---

## Project Structure

```
kafka-transactions-example/
│
├── producer/
│   ├── transactional_producer.py   # Producer script to send transactional messages
│
├── consumer/
│   ├── transactional_consumer.py   # Consumer script to process transactional messages
│
├── topics/
│   ├── create_topic.py             # Script to create the topic used in the example
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
```

---

## Prerequisites

1. **Kafka and Zookeeper**:

   - Kafka must be configured and running locally or on a server.
   - Ensure the following properties are set in your Kafka configuration:
     ```properties
     transaction.state.log.replication.factor=1
     transaction.state.log.min.isr=1
     ```

2. **Install Python Libraries**:
   - Install required Python dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

---

## Scripts Overview

### 1. Create Topic

The `create_topic.py` script creates the topic named `transactional-topic` with three partitions:

```bash
python topics/create_topic.py
```

### 2. Transactional Producer

The `transactional_producer.py` script sends a batch of transactional messages to the `transactional-topic`:

```bash
python producer/transactional_producer.py
```

### 3. Transactional Consumer

The `transactional_consumer.py` script consumes messages from the `transactional-topic`, reading only committed transactions:

```bash
python consumer/transactional_consumer.py
```

---

## How to Run

1. **Create the Topic**:

   ```bash
   python topics/create_topic.py
   ```

2. **Start the Producer**:

   ```bash
   python producer/transactional_producer.py
   ```

3. **Start the Consumer**:
   ```bash
   python consumer/transactional_consumer.py
   ```

---

## Validation

1. **Test Exactly-Once Semantics**:

   - Observe that messages are consumed only after the transaction is committed.
   - Simulate a failure in the producer (e.g., abort the transaction) and verify that no messages are delivered.

2. **Modify Producer or Consumer Logic**:
   - Adjust the producer to introduce an error before `commit_transaction()` and confirm that the messages remain invisible to the consumer.

---

## Dependencies

All required libraries are listed in `requirements.txt`:

```text
confluent-kafka
```

Install them with:

```bash
pip install -r requirements.txt
```

---

## Additional Notes

- **Isolation Level**: The consumer uses `isolation.level=read_committed` to ensure it only processes committed transactions.
- **Kafka Version**: Ensure your Kafka installation supports transactions (Kafka 0.11 or later).

---

## Project Author

- **Name**: EL BACHAR WALID
- **Field**: Data Science, AI, and Digital Health Engineering
