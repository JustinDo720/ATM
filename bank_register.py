import random
import time
import json
import sys

file_name = 'bank_data.json'


def user_info(fname, lname, age, email, gen_card_number, cvc, pin, minital = None):
    if minital:
        full_name = f'{fname} {minital} {lname}'
    else:
        full_name = f'{fname} {lname}'

    user_info_dd = [dict(
        full_name =full_name,
        age=age,
        email=email,
        card_number= gen_card_number,
        security_number = cvc,
        pin = pin,
    )]

    with open(file_name, 'w') as fp:
        json.dump(user_info_dd, fp, indent=4)

def gen_card_number():
    user_card_num = []
    for i in range(16):
        ran_number = random.randrange(0, 9)
        user_card_num.append(str(ran_number))
    user_card_num_str = ''.join(user_card_num)
    return user_card_num_str


def gen_cvc_number():
    cvc_number = []
    for i in range(3):
        ran_number = random.randrange(0, 9)
        cvc_number.append(str(ran_number))
    cvc_number_str = ''.join(cvc_number)
    return cvc_number_str

print("Welcome to Justin's bank!\nPlease fill out the following information:")
fname = input('First Name: ')
minit = input('Middle Initial(Press enter to skip): ')
lname = input('Last Name: ')
age = input('Age: ')
email = input('Email: ')
pin = input('4-Digit Pin: ')

if age < '18':
    print('We apologize but you are not older enough')
    sys.exit()
else:
    while len(pin) != 4:
        pin = input('Please enter 4 digits: ')

print('Please wait...')
time.sleep(3)

card_number = gen_card_number()
cvc_number = gen_cvc_number()
user_info(fname, lname, age, email,card_number, cvc_number, pin, minit)

print(f'''\nPlease save your information:
Card Number: {card_number} 
Cvc Number: {cvc_number}
Pin Number: {pin}
Balance: 0
''') # Make sure to change the card number to ####-####-####-####

with open('balance.json','w') as fp:
    start_balance = [0]
    json.dump(start_balance,fp,indent=4) # start the intial balance in balance.json