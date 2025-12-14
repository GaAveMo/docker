from flask import Flask, request, jsonify
import pika
import os

app = Flask(__name__)

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")

def send_message(message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()
    channel.queue_declare(queue='messages')

    channel.basic_publish(
        exchange='',
        routing_key='messages',
        body=message
    )

    connection.close()

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    message = data.get("message")

    send_message(message)
    return jsonify({"status": "Message sent to queue"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
