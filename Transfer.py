#function Transfer
from Bankapp import menu
from Clients import *
import auth
# accountName = ''
# accountId = ''

# previousTransaction = 0

def transfer_money():
    balance = 0
    amount = (input('How much money you transfer?'))
    for amount in add_clients():
        print('I want to transfer  this amount')
        if amount in add_clients():
            balance += 1
            print('Money Transfered')
            break

transfer_money()