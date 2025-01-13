import pika
import threading

class Producer:
    def __init__(self, data = None):
        self.data = data
        self.event = threading.Event()
        credentials = pika.PlainCredentials('sophie', 'password')
        connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', credentials=credentials))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='admin')
    def recive(self):        
        def callback(ch, method, properties, body):
            self.data = body
            self.event.set()
            ch.basic_ack(delivery_tag=method.delivery_tag)
        self.channel.basic_consume(on_message_callback=callback, queue='admin')
        self.channel.start_consuming()
    def get_data(self):
        self.event.wait()  
        return self.data