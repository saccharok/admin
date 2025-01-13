class Queue:
    def __init__(self, operation):
        self.operation = operation
    def get_queue(self):
        queue = ''
        if self.operation == 1 or self.operation == 2:
            queue = 'auth'
        else:
            queue = 'menu'
        return queue