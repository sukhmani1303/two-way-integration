import json
import stripe
from confluent_kafka import Consumer, KafkaError

keys = json.load(open(r'D:\zenskar\assignment\zenskar-assignment\keys.JSON'))

stripe.api_key = keys['STRIPE_SECRET_KEY']

# Defining Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'worker-group',
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer instance
consumer = Consumer(consumer_config)


queue_topic = 'customer' # kafka queue name
consumer.subscribe([queue_topic]) # consumer has to sub to a producer's queue 

def process_queue_items():
    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error while consuming message: {msg.error()}")
                    break

            item_data = json.loads(msg.value())
            process_item(item_data)

    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()

def process_item(item_data):
    try:
        print(f"Processing : {item_data}")
        
        stripe.Customer.modify(
                item_data['id'],
                name=item_data["name"],
                email=item_data["email"]
        )

    except Exception as e:
        print(f"Error processing item: {str(e)}")

if __name__ == "__main__":
    process_queue_items()
