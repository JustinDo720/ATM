import json

file_name = 'bank_data.json'

with open(file_name) as fp:
    json_info = json.load(fp)
