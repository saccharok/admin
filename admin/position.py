class Position:
    ID = ''
    name = ''
    description = ''
    cost = ''
    def __init__(self, dict):
        self.ID = dict['ID']
        self.name = dict['name']
        self.description = dict['description']
        self.cost = dict['cost']