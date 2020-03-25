from atm_machine_backend import *
from tkinter import *
from tkinter import messagebox
import pandas as pd

fp = 'bank_data.csv'

bank_data = pd.read_csv(fp)
df = pd.DataFrame(bank_data)
user_index = []


def login_screen():
    global user_index

    def authenticate_all():
        df['card_number'] = df['card_number'].astype(dtype=str)
        df['four_digits'] = df['card_number'].apply(lambda x: x[12:16])

        for rows in range(df.shape[0]):
            auth_four_digits = df.loc[rows, 'four_digits']
            auth_cvc = df.loc[rows, 'security_number']
            auth_pin = df.loc[rows, 'pin']

            if auth_four_digits == four_digits_entry.get()\
                    and float(auth_cvc) == float(cvc_label_entry.get()+'.0')\
                    and float(auth_pin) == float(pin_entry.get()+'.0'):
                user = df.loc[rows]
                user_index.append(rows)
                authenticated_message = messagebox.showinfo(title='Authenticated', message=f'Welcome {user["full_name"]}!')
                root.withdraw()
                atm_machine()
                return True
            else:
                status_bar = Label(root, text='Please try again.', fg='Red', bg='gainsboro')
                status_bar.config(font=30)
                status_bar.grid(row=5, columnspan=2)
                return False

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
    global user_index

    list_of_transaction = []
    tk_current_balance = df.loc[user_index[0], 'balance']
    tk_current_user = df.loc[user_index[0]]
    print(tk_current_balance)

    def withdraw_tk():
        global tk_current_balance
        tk_current_balance -= float(withdraw_entry.get())
        new_balance_display = tk_current_balance
        check_balance_button.config(text=f'Current Balance: ${str(new_balance_display)}')
        list_of_transaction.append(tk_current_balance)

    def deposit_tk():
        global tk_current_balance
        tk_current_balance += float(deposit_entry.get())
        new_balance_display = tk_current_balance
        check_balance_button.config(text=f'Current Balance: ${str(new_balance_display)}')
        list_of_transaction.append(tk_current_balance)

    def send_to_data_from_tk(balance):
        global tk_current_balance
        tk_current_balance = balance
        print(df)
        #df.to_csv(file_name)

        print(f'''\nNew Balance: {balance}''')

    root1 = Tk()
    root1.title('Account: {}'.format(tk_current_user['full_name']))

    atm_label = Label(root1, text='Justin\'s ATM')
    atm_label.grid(row=0, column=3)

    withdraw_entry = Entry(root1)
    withdraw_entry.grid(row=1, column=0, sticky=W)

    withdraw_button = Button(root1, text='Withdraw', command=withdraw_tk)
    withdraw_button.grid(row=3, column=0, sticky=W)

    deposit_entry = Entry(root1)
    deposit_entry.grid(row=1, column=10, sticky=E)

    deposit_button = Button(root1, text='Deposit', command=deposit_tk)
    deposit_button.grid(row=3, column=10, sticky=E)

    check_balance_button = Label(root1, text=f'Current Balance: ${str(tk_current_balance)}', width=50)
    check_balance_button.grid(row=6, columnspan=15)

    greetings_message = messagebox.showinfo('Greetings', 'Please enter an amount or use quick cash :D')

    root1.mainloop()

    try:
        actual_balance = list_of_transaction.pop()
        print(actual_balance)
        send_to_data_from_tk(balance=actual_balance)
    except IndexError as error:
        print('No change in balance')


login_screen()