from flask import Flask, jsonify, request
from flask_restful import Api, reqparse, Resource
import bigbasket
import json

app = Flask(__name__)
api = Api(app)

shoppinglist = reqparse.RequestParser()
shoppinglist.add_argument('item', type=str, required=True)
shoppinglist.add_argument('quantity', type=str, required=True)

items = json.load(open('bigbasket/items.json'))

@app.route('/')
def msg():
    return 'hey'

@app.route('/self_order/shopping_list/', methods = ['GET'])
def get():
    item_id = str(request.args['item_id'])
    try:
        return {item_id: items[item_id]}
    except:
        return {'message':'Item not in list'}

class Add_Shopping_List(Resource):

    def get(self, item_id):
        return items[item_id]

    def put(self, item_id):
        args = shoppinglist.parse_args()

        items[item_id] = args

        with open('bigbasket/items.json', 'w') as fp:
            json.dump(items, fp, indent=4)

        return jsonify({item_id: args})


api.add_resource(Add_Shopping_List, "/self_order/add_shopping_list/<string:item_id>")


class Checkout(Resource):
    def get(self):
        bigbasket.main()
        with open('bigbasket/items.json', 'w') as fp:
            json.dump({}, fp, indent=4)

        return jsonify({'message':'DONE SUCESSFULLY'})


api.add_resource(Checkout, '/self_order/checkout')

if __name__ == '__main__':
    app.run(host='192.168.1.7', port=5441 ,debug=True)
