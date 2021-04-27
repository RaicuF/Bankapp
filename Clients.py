import Bankapp
# Clients
clients = {}

for client in clients:
    print(clients[client])

def add_clients():
    id_unic = len(clients)
    name = input('Client name\n>>')
    last_name = input('Last name client\n>>')
    phone = input('Client phone\n>>')
    city = input('Client city\n>>')
    new_client = f'{id_unic},{name},{last_name},{phone},{city}\n'
    if id_unic in add_clients():
        return 'Id added'
    if name in add_clients():
        return 'Name added'
    if last_name in add_clients():
        return 'Added last name'
    if phone in add_clients():
        return 'Phone number added'
    if city in add_clients():
        return 'City added'
    elif new_client in add_clients():
        print('Client added')
    else:
        return 'Main menu'

