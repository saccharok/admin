from producer.producer import Producer
import threading
import json

class Recive:
    def __init__(self):
        self.producer = Producer()
    def run(self):
        threading.Thread(target=self.producer.recive, daemon=True).start()
    def get(self):    
        data = self.producer.get_data()
        return json.loads(data)