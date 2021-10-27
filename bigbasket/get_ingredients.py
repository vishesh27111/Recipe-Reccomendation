import requests

BASE = "http://192.168.1.7:5441/"

details = {"item": "ufwfdsfdsffdsf", "quantity": "21"}

response = requests.put(BASE + "/self_order/add_shopping_list/10", details)

print(response.json())

print(requests.get(BASE + "/self_order/shopping_list/?item_id=10").json())