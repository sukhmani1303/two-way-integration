from confluent_kafka import Producer
import json 

# kafka configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'queue-producer'
}

# Creating a Kafka producer instance
producer = Producer(producer_config)

queue_topic = 'customer' # kafka queue name

def add_item_to_queue(item_data):

    try:
        item_data_json = json.dumps(item_data)
        # item_data_json['internal_update'] = True
        producer.produce(queue_topic, key=None, value=item_data_json)
        producer.poll(0)

    except Exception as e:
        raise Exception(f"Error adding item to Kafka queue: {str(e)}")
