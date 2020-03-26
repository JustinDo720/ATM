import random, time, sys
import pandas as pd

file_name = 'bank_data.csv'


def user_info(fname, lname, age, email, gen_card_number, cvc, pin, minital = None):
    if minital:
        full_name = f'{fname} {minital} {lname}'
    else:
        full_name = f'{fname} {lname}'

    starting_balance = float(0)

    user_info = [dict(
        full_name=full_name,
        age=age,
        email=email,
        card_number=gen_card_number,
        security_number=cvc,
        pin=pin,
        balance=starting_balance
    )]

    df = pd.DataFrame()
    df = df.append(user_info)

    df.to_csv(file_name, mode='a', header=False)


def gen_card_number():
    user_card_num = []

    number_without_zero = random.randrange(1, 9)
    for i in range(16):
        if i == 1:
            user_card_num.append(str(number_without_zero))
        elif i == 12:
            user_card_num.append(str(number_without_zero))
        else:
            ran_number = random.randrange(0, 9)
            user_card_num.append(str(ran_number))

    user_card_num_str = ''.join(user_card_num)
    return user_card_num_str


def gen_cvc_number():
    cvc_number = []
    for i in range(3):
        ran_number = random.randrange(0, 9)
        cvc_number.append(str(ran_number))
        while cvc_number[0] == '0':
            cvc_number[0] = str(ran_number)
    cvc_number_str = ''.join(cvc_number)
    return cvc_number_str

def main_screen():
    print("Welcome to Justin's bank!\nPlease fill out the following information:")
    fname = input('First Name: ')
    minit = input('Middle Initial(Press enter to skip): ')
    lname = input('Last Name: ')
    email = input('Email: ')

    try:
        age = int(input('Age: '))
        pin = int(input('4-Digit Pin: '))
        if age < 18:
            print('We apologize but you are not older enough')
            sys.exit()
        else:
            while len(str(pin)) != 4:
                pin = input('Please enter 4 digits: ')
        print('Please wait...')
        time.sleep(1)

        card_number = gen_card_number()
        cvc_number = gen_cvc_number()
        user_info(fname, lname, age, email, card_number, cvc_number, pin, minit)

        print(f'''\nPlease save your information:
            Card Number:%s-%s-%s-%s 
            Cvc Number: {cvc_number}
            Pin Number: {pin}
            Balance: 0
            ''' % (card_number[:4], card_number[4:8], card_number[8:12], card_number[12:16]))
    except ValueError as error:
        print('Please enter numbers')
        continue_adding_user = input('Would you like to add another person?').lower()
        while continue_adding_user[0] == 'y':
            main_screen()


main_screen()
