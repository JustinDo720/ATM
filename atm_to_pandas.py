import pandas as pd

csv_location = 'atm_db.csv'

info = {
        'first_name':'Justin',
        'middle_name': 'Hoang',
        'last_name': 'Do',
        'age':18,
        'email':'jdo@example.com',
        'card_number':2176010517604587,
        'cvc':111,
        'pin':4444,
        'balance': 0
}

info2 = ('Justin','hoang','Do', 18, 'jdo@exmaple.com', 2176010517604587, 111,4444)
df = pd.DataFrame()
df = df.append(info, ignore_index=True)

df.to_csv(csv_location)