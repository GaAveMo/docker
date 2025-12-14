import pika
import os

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=RABBITMQ_HOST)
)
channel = connection.channel()

channel.queue_declare(queue='messages')

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

channel.basic_consume(
    queue='messages',
    on_message_callback=callback,
    auto_ack=True
)

print("Consumer started. Waiting for messages...")
channel.start_consuming()
