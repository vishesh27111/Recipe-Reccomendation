import requests
BASE = "http://127.0.0.1:5000/"

details = {"item": "u", "quantity": "1"}

response = requests.put(BASE + "/self_order/shopping_list/6", details)

# print(response.json())

print(requests.get(BASE + "/self_order/shopping_list/6").json())