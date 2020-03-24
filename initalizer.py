import pandas as pd

file_name = 'bank_data.csv'

start_info = [dict(
        full_name='Admin',
        age=None,
        email=None,
        card_number=None,
        security_number=None,
        pin=None,
        balance=float(0)
    )]

df = pd.DataFrame(start_info)
df.to_csv(file_name)

print('Welcome! Please enter a password for your Admin account')
password = input('Password: ')  # Make an admin for removing rows aka users

