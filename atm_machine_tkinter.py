from atm_machine_backend import *
from tkinter import *
from tkinter import messagebox
import pandas as pd

fp = 'bank_data.csv'

new_bank_data = pd.read_csv(fp)
new_df = pd.DataFrame(new_bank_data)

tk_current_balance = new_df.balance.item()

list_of_transaction = []


def withdraw_tk():
    global tk_current_balance
    if authentication:
        tk_current_balance -= float(withdraw_entry.get())
        new_balance_display = tk_current_balance
        check_balance_button.config(text= f'Current Balance: ${str(new_balance_display)}')
        list_of_transaction.append(tk_current_balance)


def deposit_tk():
    global tk_current_balance
    if authentication:
        tk_current_balance += float(deposit_entry.get())
        new_balance_display = tk_current_balance
        check_balance_button.config(text= f'Current Balance: ${str(new_balance_display)}')
        list_of_transaction.append(tk_current_balance)


def send_to_data_from_tk(balance):
    df.loc[0, 'balance'] = balance
    df.to_csv(file_name)

    print(f'''\nNew Balance: {balance}''')


root = Tk()

atm_label = Label(root,text='Justin\'s ATM')
atm_label.grid(row=0,column=3)

withdraw_entry = Entry(root)
withdraw_entry.grid(row=1,column=0, sticky=W)

withdraw_button = Button(root, text='Withdraw', command=withdraw_tk)
withdraw_button.grid(row=3, column=0, sticky=W)

deposit_entry = Entry(root)
deposit_entry.grid(row=1, column=10,sticky=E)

deposit_button = Button(root, text='Deposit', command=deposit_tk)
deposit_button.grid(row=3, column=10, sticky=E)


check_balance_button = Label(root, text= f'Current Balance: ${str(tk_current_balance)}', width=50)
check_balance_button.grid(row=6, columnspan=15)

greetings_message = messagebox.showinfo('Greetings', 'Please enter an amount or use quick cash :D')

root.mainloop()

try:
    actual_balance = list_of_transaction.pop()
    print(actual_balance)
    send_to_data_from_tk(balance=actual_balance)
except IndexError as error:
    print('No change in balance')