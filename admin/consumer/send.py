from consumer.message import Message
from consumer.consumer import Consumer

def run(operation, data):
    mes = Message()
    if operation == 1:
        login = data['login']
        password = data['password']
        m = mes.create_auth(login, password)
    elif operation == 2:
        ID = data['ID']
        m = mes.create_user_info(ID)
    elif operation == 3:
        ID = data['ID']
        name = data['name']
        desription = data['desription']
        cost = data['cost']
        m = mes.create_create(ID, name, desription, cost)
    elif operation == 4:
        ID = data['ID']
        m = mes.create_read(ID)
    elif operation == 5:
        ID = data['ID']
        m = mes.create_update(ID)
    else:
        ID = data['ID']
        idpos = data['idpos']
        m = mes.create_delete(ID, idpos)
    c = Consumer(operation, m)
    c.send()