import requests

BASE = "http://127.0.0.1:5000/"

details = {"item": "ufwfdsfdsffdsf", "quantity": "21"}

response = requests.put(BASE + "/self_order/add_shopping_list/10", details)

# print(response.json())

# print(requests.get(BASE + "/self_order/shopping_list/6").json())