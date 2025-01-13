import json

class Message:
    # конструктор
    def __init__(self):
        pass

    # json auth
    def create_auth(self, login, password):
        file = 'admin/consumer/auth.json'
        with open(file, 'r') as f:
            data = json.load(f)
        data['login'] = login
        data['password'] = password
        return json.dumps(data)
    
    # json user_info
    def create_user_info(self, ID):
        file = 'admin/consumer/user_info.json'
        with open(file, 'r') as f:
            data = json.load(f)
        data['ID'] = ID
        return json.dumps(data)
    
    # json create
    def create_create(self, ID, name, desription, cost):
        file = 'admin/consumer/create.json'
        with open(file, 'r') as f:
            data = json.load(f)
        data['ID'] = ID
        data['name'] = name
        data['desription'] = desription
        data['cost'] = cost
        return json.dumps(data)
    
    # json read
    def create_read(self, ID):
        file = 'admin/consumer/create.json'
        with open(file, 'r') as f:
            data = json.load(f)
        data['ID'] = ID
        data['operation'] = 'read'
        return json.dumps(data)
    
    # json update
    def create_update(self, ID):
        file = 'admin/consumer/create.json'
        with open(file, 'r') as f:
            data = json.load(f)
        data['ID'] = ID
        data['operation'] = 'update'
        return json.dumps(data)
    
    # json delete
    def create_delete(self, ID, idpos):
        file = 'admin/consumer/create.json'
        with open(file, 'r') as f:
            data = json.load(f)
        data['ID'] = ID
        data['idpos'] = idpos
        return json.dumps(data)