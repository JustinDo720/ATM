from atm_machine_backend import *
import json

choice = screen()
option(choice)
new_balance = current_balance

with open(file_name, 'w') as f:
    json.dump(new_balance,f, indent=4)
