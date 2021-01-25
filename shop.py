import requests

r = requests.get('https://api.peely.de/cdn/current/shop.png')
with open('shop.png', 'wb') as f:
    f.write(r.content)