from tkinter import *
from tkinter import messagebox
import pandas as pd
from collections import deque

fp = 'bank_data.csv'

bank_data = pd.read_csv(fp)
df = pd.DataFrame(bank_data)
user_information = {}
test_balance = deque(maxlen=1)


def login_screen():

    def authenticate_all():

        df['card_number'] = df['card_number'].astype(dtype=str)
        df['four_digits'] = df['card_number'].apply(lambda x: x[12:16])

        df['security_number'] = df['security_number'].astype(dtype=str)
        df['three_cvc'] = df['security_number'].apply(lambda x: x[:3])

        df['pin'] = df['pin'].astype(dtype=str)
        df['four_pin'] = df['pin'].apply(lambda x: x[:4])

        for rows in df.index:
            auth_four_digits = df.loc[rows, 'four_digits']
            auth_cvc = df.loc[rows, 'three_cvc']
            auth_pin = df.loc[rows, 'four_pin']

            if auth_four_digits == four_digits_entry.get()\
                    and str(auth_cvc) == str(cvc_label_entry.get())\
                    and str(auth_pin) == str(pin_entry.get()):
                user = df.loc[rows]
                test_balance.append(df.loc[rows,'balance'])
                user_information['index'] = rows
                user_information['balance'] = df.loc[rows,'balance']
                user_information['user'] = user

                root.withdraw()
                atm_machine()
                return True

        if auth_four_digits != four_digits_entry.get():
            status_bar = Label(root, text='Please try again.', fg='Red', bg='gainsboro')
            status_bar.config(font=30)
            status_bar.grid(row=5, columnspan=2)

    root = Tk()
    root.title('Login Page')
    root.config(bg='gainsboro')
    root.geometry('300x200')
    login_label = Label(root, text='Login', fg='purple',bg='gainsboro')
    login_label.config(font=100)
    login_label.grid(row=0, column=1)

    four_digits_label = Label(root, text='Last Four Digits:',bg='gainsboro')
    four_digits_label.grid(row=1, sticky=N+S+E+W)
    four_digits_entry = Entry(root,show="*")
    four_digits_entry.grid(row=1, column=1)

    cvc_label = Label(root, text='Cvc:', bg='gainsboro')
    cvc_label.grid(row=2, sticky=E)
    cvc_label_entry = Entry(root, show="*")
    cvc_label_entry.grid(row=2, column=1)

    pin_label = Label(root, text='Pin:', bg='gainsboro')
    pin_label.grid(row=3, sticky=E)
    pin_entry = Entry(root, show="*")
    pin_entry.grid(row=3, column=1)

    submit_button = Button(root, text='Login',command= authenticate_all, bg='gainsboro')
    submit_button.grid(row=4, column=1)
    cancel_button = Button(root, text='Cancel', command= root.destroy, bg='gainsboro')
    cancel_button.grid(row=4, column=0)

    root.mainloop()

    authenticated = authenticate_all
    return authenticated


def atm_machine():
    global user_information
    list_of_transaction = deque(maxlen=3)
    tk_current_user = user_information['user']
    current_balance = user_information['balance']

    def withdraw_tk():
        global test_balance
        tk_current_balance = test_balance[0]
        tk_current_balance -= float(withdraw_entry.get())
        new_balance_display = tk_current_balance
        test_balance.append(new_balance_display)
        check_balance_label.config(text=f'Current Balance: ${str(new_balance_display)}')
        list_of_transaction.append(tk_current_balance)

    def deposit_tk():
        global test_balance
        tk_current_balance = test_balance[0]
        tk_current_balance += float(deposit_entry.get())
        new_balance_display = tk_current_balance
        test_balance.append(new_balance_display)
        check_balance_label.config(text=f'Current Balance: ${str(new_balance_display)}')
        list_of_transaction.append(tk_current_balance)

    def send_to_data_from_tk():
        global test_balance
        final_balance = test_balance[0]
        df.loc[user_information['index'], 'balance'] = final_balance
        if 0 in df.index:
            df.to_csv(fp, mode='w', index=False)
        else:
            df.to_csv(fp, mode='w')

        balance_message = messagebox.showinfo(title='Saved Balance', message=f'New Balance: ${final_balance}')
        print(f'''\nNew Balance: {final_balance}''')

    root1 = Tk()
    root1.title('Account: {}'.format(tk_current_user['full_name']))

    new_atm_label = Label(root1, text='Justin\'s ATM', font=100)
    new_atm_label.grid(row=0, column=2)

    withdraw_entry = Entry(root1)
    withdraw_entry.grid(row=1, column=0, sticky=W)
    withdraw_button = Button(root1, text='Withdraw', command=withdraw_tk)
    withdraw_button.grid(row=3, column=0, sticky=W)

    deposit_entry = Entry(root1)
    deposit_entry.grid(row=1, column=3)
    deposit_button = Button(root1, text='Deposit', command=deposit_tk)
    deposit_button.grid(row=3, column=3)

    check_balance_label = Label(root1, text=f'Current Balance: ${str(current_balance)}', font=75)
    check_balance_label.grid(row=4, column=2)

    save_button = Button(root1, text='Save', command=send_to_data_from_tk)
    save_button.grid(row=5, column=2)

    greetings_message = messagebox.showinfo('Greetings', f'Welcome {df.loc[user_information["index"],"full_name"]}!')

    root1.mainloop()

login_screen()