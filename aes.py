import requests
import json

def get_request():
    return requests.get(url = 'https://fortnite-api.com/v2/aes')

def fetch_dynamic_keys():
    response = get_request()
    if response.status_code == 200:
        json_data = response.json()
        write_to_file(json_data['data']['dynamicKeys'])

def write_to_file(data):
    with open('keys.json', 'w') as fw:
        json.dump(data, fw)
        

fetch_dynamic_keys()
