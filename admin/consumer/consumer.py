import pika
from consumer.myqueue import Queue

class Consumer:
    def __init__(self, operation, message):
        q = Queue(operation)
        self.queue = q.get_queue()
        self.message = message
    def send(self):
        credentials = pika.PlainCredentials('sophie', 'password')
        connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue)
        channel.basic_publish(exchange='', 
                      routing_key=self.queue,
                      body=self.message)
        connection.close()