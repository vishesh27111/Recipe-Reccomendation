from flask import Flask, jsonify
from flask_restful import Api, reqparse, Resource
from bigbasket import *

app = Flask(__name__)
api = Api(app)

shoppinglist = reqparse.RequestParser()
shoppinglist.add_argument('item', type=str, required=True)
shoppinglist.add_argument('quantity', type=str, required=True)
items = {}


class Get_Shopping_List(Resource):

    def get(self, item_id):
        return items[item_id]

    def put(self, item_id):
        args = shoppinglist.parse_args()
        items[item_id] = args
        return jsonify({item_id: args})


api.add_resource(Get_Shopping_List, '/self_order/shopping_list/<int:item_id>')


class Checkout(Resource):
    def get(self):
        # browser = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        browser = webdriver.Chrome(options=options)
        browser.get('https://www.bigbasket.com/')
        # browser.get('https://www.bigbasket.com/auth/login/')
        # login(browser)
        shopping_list, quantity_list = get_shopping_list()
        shopping_list = [s.rstrip() for s in shopping_list]
        for item, quantity in zip(shopping_list, quantity_list):
            search(browser, item)
            add_item(browser, quantity)
            browser.get('https://www.bigbasket.com/')

        go_to_checkout(browser)
        # checkout(browser)
        return jsonify({'output': 'DONE SUCESSFULLY'})


api.add_resource(Checkout, '/self_order/checkout')

if __name__ == '__main__':
    app.run(debug=True)
