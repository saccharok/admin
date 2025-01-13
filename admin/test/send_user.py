import pika

message = '12345'
credentials = pika.PlainCredentials('sophie', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0', credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='admin')
channel.basic_publish(exchange='', 
                      routing_key='admin',
                      body=message)
connection.close()