import sys
import pandas as pd

file_name = 'bank_data.csv'
#with open(file_name, 'r') as f:
 #   previous_balance = json.load(f)

bank_data = pd.read_csv(file_name)
df = pd.DataFrame(bank_data)

current_balance = df['balance'].item()

def authentication(pin):
    user_pin = df['pin'].item()
    if pin == int(user_pin):
        return True
    else:
        print('User unauthenticated')
        sys.exit()


def withdraw():
    if authentication:
        global current_balance
        amount = input('Please enter the withdraw amount: ')
        current_balance -= float(amount)
        send_to_data(amount, current_balance)

def deposit():
    if authentication:
        global current_balance
        amount = input('Please enter the deposit amount: ')
        current_balance += float(amount)
        send_to_data(amount, current_balance)

def quick_cash():
    if authentication:
        global current_balance
        amount = input('Please enter the amount below:\n$5\n$10\n$20\n$50\n$100\n')
        current_balance -= int(amount)
        send_to_data(amount, current_balance)


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
    pin = int(input('Pin: '))
    authentication(pin)

    if authentication:
        print(f'Welcome {df["full_name"].item()}!')
        print('''Please select the number corresponding to the options below:
    1. Withdraw
    2. Deposit
    3. Quick Cash
    4. Check Balance
    5. Exit''')
        user_option = input()
        return user_option


def send_to_data(amount, balance):
    df.loc[0, 'balance'] = balance
    df.to_csv(file_name)
    previous_balance = balance - float(amount)
    print(f'''\nTransferred {amount} completed.\nPrevious Balance: {previous_balance}.\nNew Balance: {balance}''')

