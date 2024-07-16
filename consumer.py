from kafka import KafkaConsumer, KafkaProducer
import json

# Kafka Consumer
consumer = KafkaConsumer(
    'user-login',
    bootstrap_servers='<bootstrap server>',
    security_protocol='SASL_SSL',
    sasl_mechanism='PLAIN',
    sasl_plain_username='<API key>',
    sasl_plain_password='<API secret>',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
# Kafka Producer for processed data
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Process messages
for message in consumer:
    data = message.value

    # Example processing: Filter by device type "android"
    if data['device_type'] == 'android':
        # Add additional processing if needed
        producer.send('processed-data', value=data)

    print(f"Processed message: {data}")

producer.flush()
