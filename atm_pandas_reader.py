import pandas as pd
csv_location = 'atm_db.csv'

csv_reader = pd.read_csv(csv_location)
df = pd.DataFrame(csv_reader)

user_pin = df.pin.item()
user_pin = int(user_pin)

#pin = input()
#if pin == str(user_pin):
 #   print('Authenticated')
 #   print()

user_balance = df['balance'].item()
print(user_balance)
amount = float(input('Amount:'))
def compute():
    global user_balance
    user_balance+= amount
    print(user_balance)

compute()