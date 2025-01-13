from prettytable import PrettyTable
from consumer import send
from producer.recive import Recive

class User:
    ID = ''
    login = ''
    name = ''
    surname = ''
    post = ''
    
    def __init__(self):
        self.login = input("Введите логин: ")
        password = input("Введите пароль: ")
        data = {
            "login": self.login,
            "password": password
        }
        send.run(1, data)
        r = Recive()
        r.run()
        while True:
            res = r.get()
            if res not in ['undefined', '']:
                self.ID = res
                break
        data = {
                    "ID": self.ID
                }
        send.run(2, data)
        data.clear()
        while True:
            data = r.get()
            if isinstance(data, dict) and data:
                self.set_info(data['ID'], data['name'], data['surname'], data['post'])
                self.show_info()
                break

    def set_info(self, ID, name, surname, post):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.post = post

    def show_info(self):
        table = PrettyTable()
        table.field_names = ["ID", "Имя", "Фамилия", "Должность"]
        table.add_row([self.ID, self.name, self.surname, self.post])
        print(table)