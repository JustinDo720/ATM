import sys
from json_reader import json_info
import json

file_name = 'balance.json'
with open(file_name, 'r') as f:
    previous_balance = json.load(f)

current_balance = [previous_balance[0]]

def authentication(pin):
    user_pin = json_info[0]['pin']
    if pin == user_pin:
        return True
    else:
        print('User unauthenticated')
        sys.exit()


def print_current_amount(balance):
    print(f'Current amount after change: {current_balance}')

def withdraw():
    if authentication:
        amount = input('Please enter the withdraw amount: ')
        current_balance[0] -= int(amount)
        print_current_amount(current_balance)


def deposit():
    if authentication:
        amount = input('Please enter the deposit amount: ')
        current_balance[0] += int(amount)
        print_current_amount(current_balance)

def quick_cash():
    if authentication:
        amount = input('Please enter the amount below:\n$5\n$10\n$20\n$50\n$100\n')
        current_balance[0] -= int(amount)
        print_current_amount(current_balance)


def check_balance():
    print(f'Current balance: {current_balance}')

def option(number):
    if number == '1':
        withdraw()
    elif number == '2':
        deposit()
    elif number == '3':
        quick_cash()
    elif number == '4':
        check_balance()
    else:
        print('Thank You')
        sys.exit()


def screen():
    print('Welcome, please insert your card and enter your pin.')
    pin = input('Pin: ')
    authentication(pin)

    if authentication:
        print(f'Welcome {json_info[0]["full_name"]}!')
        print('''Please select the number corresponding to the options below:
    1. Withdraw
    2. Deposit
    3. Quick Cash
    4. Check Balance
    5. Exit''')
        user_option = input()
        return user_option


