import json

from sseclient import SSEClient
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

bootstrap_servers = ['localhost:19090', 'localhost:19091', 'localhost:19092']

kafka_client = KafkaAdminClient(
    bootstrap_servers=bootstrap_servers,
    client_id='PythonClient'
)

# verify if topics exists
topic = 'wikimedia'
current_topics = kafka_client.list_topics()

if topic not in current_topics:
    new_topic = NewTopic(
        name=topic,
        num_partitions=3,
        replication_factor=2,
    )
    
    kafka_client.create_topics(new_topics=[new_topic])
    
url = 'https://stream.wikimedia.org/v2/stream/recentchange'
client = SSEClient(url)

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

for msg in client:
    outputMsg = msg.data
    if len(outputMsg) > 2:
        outputJS = json.loads(outputMsg)
        print("Send ", outputJS)
        producer.send(topic=topic, value=json.dumps(outputJS).encode())
