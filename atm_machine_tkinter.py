from tkinter import *
from tkinter import messagebox
from atm_machine_backend import *
import json


#with open(file_name, 'w') as f:
    #json.dump(new_balance,f, indent=4)


root = Tk()

greetings_message = messagebox.showinfo('Greetings', 'Please click on one of the following buttons below')

atm_label = Label(root,text='ATM')
atm_label.grid(row=0,column=1)

withdraw_entry = Entry(root)
withdraw_entry.grid(row=1,column=0, sticky=W)

withdraw_button = Button(root, text='Withdraw',)
withdraw_button.grid(row=2, column=0, sticky=W)

deposit_entry = Entry(root)
deposit_entry.grid(row=1, column=3,sticky=E)

deposit_button = Button(root, text='Deposit')
deposit_button.grid(row=2, column=3, sticky=E)

check_balance_button = Button(root, text=f'{current_balance}')
check_balance_button.grid(columnspan=4)

'''check_balance_entry = Entry(root)
check_balance_entry.grid() 

quick_cash_button = Button(root, text='Quick Cash')
quick_cash_button.grid(row=5, column=3)'''

root,mainloop()