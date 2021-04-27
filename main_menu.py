import auth



def menu():
    menu = ["1. Log on\n2. Add client\n3. Ceck balance\n4. Transfer Money\n5. Bank statement\n6. Log off"]
    while True:
        for submenu in (menu):
            print(submenu)
            option = (input('>>'))
            if option == '6':
                print('You are log off')
                break
            if option == '1':
                auth.utilizatori()
            if option == '2':
                add_clients()
            if option == '3':
                balance_clients()
            if option == '4':
                transfer_money()
            if option == '5':
                auth.canvas()
menu()

print('Bank Application Online...')
while True:
    user = input('username:\n> ')
    password = input('password\n> ')
    if auth.utilizatori(password) == True:
        menu()
    elif auth.utilizatori(password) == 'nu_exista':
        print('Utilizatorul nu exista, incearca din nou')
        continue
    elif auth.utilizatori(password) == 'parola_gresita':
        print('Parola gresita, incearca din nou')
        continue