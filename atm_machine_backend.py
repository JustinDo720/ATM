import sys
import pandas as pd
from collections import deque

file_name = 'bank_data.csv'

bank_data = pd.read_csv(file_name)
df = pd.DataFrame(bank_data)


def authentication(four_digits, cvc):

    df['card_number'] = df['card_number'].astype(dtype=str)
    df['four_digits'] = df['card_number'].apply(lambda x: x[12:16])

    for rows in range(df.shape[0]):
        auth_four_digits = df.loc[rows, 'four_digits']
        auth_cvc = df.loc[rows, 'security_number']

        if four_digits == auth_four_digits and cvc == auth_cvc:
            new_data = df.loc[rows]
            print(f"\nWelcome {new_data['full_name']}! Please enter your pin:")
            chances = 0
            while chances != 3:
                pin = int(input('Pin: '))
                if pin == new_data['pin']:
                    user_information(index=rows)
                    print('Authenticated')
                    return True
                else:
                    print('Failed Authentication. Please try again later...')
                    chances += 1


current_balance = []
index_list = []


def user_information(index):
    user_balance = df.loc[index, 'balance']
    current_balance.append(user_balance)
    index_list.append(index)


def withdraw():
    global current_balance
    amount = input('Please enter the withdraw amount: ')
    current_balance[0] -= float(amount)
    send_to_data(amount, current_balance)


def deposit():
    global current_balance
    amount = input('Please enter the deposit amount: ')
    current_balance[0] += float(amount)
    send_to_data(amount, current_balance)


def quick_cash():
    global current_balance
    amount = input('Please enter the amount below:\n$5\n$10\n$20\n$50\n$100\n')
    current_balance[0] -= int(amount)
    send_to_data(amount, current_balance)


def check_balance():
    print(f'Current balance: {current_balance[0]}')


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
    print('Welcome, please enter the last 4 digits on your card and cvc.')

    chances = 0
    while chances != 3:
        four_digits = str(input('Last 4 digits on your card: '))
        cvc = int(input('Cvc: '))
        authenticated = authentication(four_digits, cvc)
        if authenticated:
            break
        chances += 1

    if authenticated:
        print('''\nPlease select the number corresponding to the options below:
    1. Withdraw
    2. Deposit
    3. Quick Cash
    4. Check Balance
    5. Exit''')
        user_option = input()
        return user_option
    else:
        print('User Unauthenticated')


def send_to_data(amount, balance):
    global index_list
    df.loc[index_list[0], 'balance'] = balance
    dict_of_data = df.iloc[index_list[0]].to_dict()
    new_df = pd.Series(dict_of_data)
    df.append(new_df, ignore_index=True)
    if 0 in df.index:
        df.to_csv(file_name, mode='w', index=False)
    else:
        df.to_csv(file_name, mode='w')
    previous_balance = balance[0] - float(amount)
    print(f'''\nTransferred {amount} completed.\nPrevious Balance: {previous_balance}.\nNew Balance: {balance[0]}''')
