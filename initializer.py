import pandas as pd

file_name = 'ATM_backend/bank_data.csv'

start_info = [dict(
        full_name=None,
        age=None,
        email=None,
        card_number=None,
        security_number=None,
        pin=None,
        balance=None
    )]

df = pd.DataFrame(start_info)
df.to_csv(file_name)

print('Welcome! Thank You for initializing. Please register before using the ATM.')


