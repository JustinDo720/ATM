from atm_machine_backend import *
from tkinter import *
from tkinter import messagebox
import pandas as pd

#fp = 'bank_data.csv'

#bank_data = pd.read_csv(fp)
#df = pd.DataFrame(bank_data)


class Login:
    def __init__(self, master):
        master.title('Login Page')
        master.config(bg='gainsboro')
        master.geometry('300x200')

        self.login_label = Label(master, text='Login', fg='purple',bg='gainsboro')
        self.login_label.config(font=100)
        self.login_label.grid(row=0, column=1,sticky=N+S+E+W)

        self.four_digits_label = Label(master, text='Last Four Digits:',bg='gainsboro').grid(row=1, sticky=N+S+E+W)
        self.four_digits_entry = Entry(master, bg='white smoke').grid(row=1, column=1,sticky=N+S+E+W)

        self.cvc_label = Label(master, text='Cvc:', bg='gainsboro').grid(row=2, sticky=E)
        self.cvc_label_entry = Entry(master, bg='white smoke').grid(row=2, column=1)

        self.pin_label = Label(master, text='Pin:', bg='gainsboro').grid(row=3, sticky=E)
        self.pin_entry = Entry(master, bg='white smoke').grid(row=3, column=1)

        self.submit_button = Button(master, text='Login',command= self.authenticate, bg='gainsboro').grid(row=4, column=1)
        self.cancel_button = Button(master, text='Cancel', command= master.destroy,bg='gainsboro').grid(row=4, column=0)

root = Tk()
login_page = Login(root)
root.mainloop()