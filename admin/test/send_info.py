import pika
import json

file = 'user_info.json'
with open(file, 'r') as f:
    message = json.load(f)
message_str = json.dumps(message)
credentials = pika.PlainCredentials('sophie', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='admin')
channel.basic_publish(exchange='', 
                      routing_key='admin',
                      body=message_str)
connection.close()