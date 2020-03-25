from atm_machine_backend import *
from tkinter import *
from tkinter import messagebox
import pandas as pd

fp = 'bank_data.csv'

bank_data = pd.read_csv(fp)
df = pd.DataFrame(bank_data)
print(df)



def main_screen():

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
                print('Success')
            else:
                print('Sleep')

    root = Tk()
    root.title('Login Page')
    root.config(bg='gainsboro')
    root.geometry('300x200')
    login_label = Label(root, text='Login', fg='purple',bg='gainsboro')
    login_label.config(font=100)
    login_label.grid(row=0, column=1)

    four_digits_label = Label(root, text='Last Four Digits:',bg='gainsboro').grid(row=1, sticky=N+S+E+W)
    four_digits_entry = Entry(root,show="*")
    four_digits_entry.grid(row=1, column=1)

    cvc_label = Label(root, text='Cvc:', bg='gainsboro').grid(row=2, sticky=E)
    cvc_label_entry = Entry(root, show="*")
    cvc_label_entry.grid(row=2, column=1)

    pin_label = Label(root, text='Pin:', bg='gainsboro').grid(row=3, sticky=E)
    pin_entry = Entry(root, show="*")
    pin_entry.grid(row=3, column=1)

    submit_button = Button(root, text='Login',command= authenticate_all, bg='gainsboro').grid(row=4, column=1)
    cancel_button = Button(root, text='Cancel', command= root.destroy, bg='gainsboro').grid(row=4, column=0)

    root.mainloop()

main_screen()