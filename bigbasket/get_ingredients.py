import requests
BASE = 'http://127.0.0.1:5000/'

details = {'item': 'tomato', 'quantity': '1'}
response = requests.put(BASE + "/self_order/shopping_list/1", details)

print(requests.get(BASE + '/self_order/shopping_list/1').json())