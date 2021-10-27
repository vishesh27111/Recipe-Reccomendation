from flask import Flask, jsonify
from flask_restful import Api, reqparse, Resource
import bigbasket
import json

app = Flask(__name__)
api = Api(app)

shoppinglist = reqparse.RequestParser()
shoppinglist.add_argument('item', type=str, required=True)
shoppinglist.add_argument('quantity', type=str, required=True)

items = json.load(open('bigbasket/items.json'))


class WelcomeMSG(Resource):
    @staticmethod
    def get():
        return {'message': 'Welcome to Recipe Recommendation API.'}


api.add_resource(WelcomeMSG, '/')


class Get_Shopping_List(Resource):
    @staticmethod
    def get(item_id):  # Get specific item details
        try:
            return jsonify({item_id: items[item_id]})
        except KeyError:
            return jsonify({'message': 'Item not in list'})


api.add_resource(Get_Shopping_List, '/self_order/get_shopping_list/<string:item_id>')


class Add_Shopping_List(Resource):  # Modifying the Shopping List
    @staticmethod
    def put(item_id):
        args = shoppinglist.parse_args()
        items[item_id] = args
        with open('bigbasket/items.json', 'w') as fp:
            json.dump(items, fp, indent=4)
        return jsonify({item_id: args})


api.add_resource(Add_Shopping_List, "/self_order/add_shopping_list/<string:item_id>")


class Checkout(Resource):
    @staticmethod
    def get():
        bigbasket.main()
        with open('bigbasket/items.json', 'w') as fp:
            json.dump({}, fp, indent=4)
        return jsonify({'message': 'ORDERED SUCCESSFULLY'})


api.add_resource(Checkout, '/self_order/checkout')

if __name__ == '__main__':
    app.run(host='192.168.1.7', port=5000, debug=True)
