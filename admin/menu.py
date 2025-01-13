from position import Position
from prettytable import PrettyTable
from consumer import send as send
from producer.recive import Recive

class Menu:
    positions = []
    count = 0
    def __init__(self):
        pass

    def get_menu(self, ID):
        operation = 'read'
        data = {
            'ID': ID,
            'operation': operation
        }
        send.run(4, data)
        r = Recive()
        while True:
            data = r.get()
            if isinstance(data, dict) and 'positions' in data:
                for item in data['positions']:
                    position = Position(item)
                    self.positions.append(position)
                self.show_menu()
                break
        for item in data['positions']:
            position = Position(item)
            self.positions.append(position)
        self.show_menu()

    def add_position(self, ID, name, description, cost):
        data = {
            'ID': ID,
            'name': name,
            'description' : description, 
            'cost' : cost
        }
        send.run(3, data)
        r = Recive()
        while True:
            data = r.get()
            if data == 'done':
                data = {
                'ID': ID,
                'operation': 'update'
                }
                send.run(5, data)
                r = Recive()
                data = r.run()
                self.positions.clear()
                break
        for item in data['positions']:
            position = Position(item)
            self.positions.append(position)
        self.show_menu()

    def delete_position(self, ID, idpos):
        data = {
            'ID': ID,
            'idpos': idpos
        }
        send.run(6, data)
        r = Recive()
        while True:
            data = r.get()
            if data == 'done':
                data = {
                'ID': ID,
                'operation': 'update'
                }
                send.run(5, data)
                r = Recive()
                data = r.run()
                self.positions.clear()
                break
        for item in data['positions']:
            position = Position(item)
            self.positions.append(position)
        self.show_menu()

    def show_menu(self):
        table = PrettyTable()
        table.field_names = ["ID", "Позиция", "Описание", "Цена"]
        for position in self.positions:
            table.add_row([position.ID, position.name, position.description, position.cost])
        print(table)