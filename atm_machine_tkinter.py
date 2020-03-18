from atm_machine_backend import *
from tkinter import *
from tkinter import messagebox
import json

file_name = 'balance.json'
list_of_transaction = []


def withdraw_tk():
    if authentication:
        current_balance[0] -= float(withdraw_entry.get())
        new_balance_display = current_balance
        check_balance_button.config(text= f'Current Balance: ${str(new_balance_display[0])}')
        list_of_transaction.append(current_balance)


def deposit_tk():
    if authentication:
        current_balance[0] += float(deposit_entry.get())
        new_balance_display = current_balance
        check_balance_button.config(text= f'Current Balance: ${str(new_balance_display[0])}')
        list_of_transaction.append(current_balance)


root = Tk()

atm_label = Label(root,text='ATM')
atm_label.grid(row=0,column=1)

withdraw_entry = Entry(root)
withdraw_entry.grid(row=1,column=0, sticky=W)

withdraw_button = Button(root, text='Withdraw', command=withdraw_tk)
withdraw_button.grid(row=3, column=0, sticky=W)

deposit_entry = Entry(root)
deposit_entry.grid(row=1, column=3,sticky=E)

deposit_button = Button(root, text='Deposit', command=deposit_tk)
deposit_button.grid(row=3, column=3, sticky=E)

check_balance_button = Label(root, text= f'Current Balance: ${str(current_balance[0])}', width=50)
check_balance_button.grid(columnspan=5)

greetings_message = messagebox.showinfo('Greetings', 'Please enter an amount or use quick cash :D')

root,mainloop()

actual_balance = list_of_transaction.pop()

print(actual_balance)
with open(file_name, 'w') as f:
    json.dump(actual_balance,f, indent=4)