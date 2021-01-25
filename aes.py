import requests
import json

def fetch_dynamic_keys():
    response = requests.get('https://fortnite-api.com/v2/aes')
    if response.status_code == 200:
        json_data = response.json()
        write_to_file(json_data['data']['dynamicKeys'], 'keys.txt')
    else:
        print(f'Error: {response.status_code}')

def fetch_items():
    response = requests.get('https://fortnite-api.com/v2/cosmetics/br/new')
    if response.status_code == 200:
        json_data = response.json()
        write_to_file(json_data['data']['items'], 'new.txt')
    else:
        print(f'Error: {response.status_code}')

def write_to_file(data, file_name):
    with open(file_name, 'w') as fw:
        json.dump(data, fw)
        

fetch_dynamic_keys()
fetch_items()
