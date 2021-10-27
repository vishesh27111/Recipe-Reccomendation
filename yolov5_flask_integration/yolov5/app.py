from flask import Flask, jsonify
from detect import *
from flask_restful import Api, reqparse, Resource
import json
import sys
sys.path.insert(1, '/Users/aryan/Desktop/Python/yolo_v5/Flask_API/bigbasket/')
import bigbasket

app = Flask(__name__)
api = Api(app)


class yolov5(Resource):
    def get(self):
        opt = parse_opt()
        out = main(opt)
        final = out.split()
        dic1 = {}
        a_file = open("/yolov5_flask_integration/yolov5/classes.txt", "r")

        list_of_lists = []
        for line in a_file:
            stripped_line = line.strip()
            line_list = stripped_line.split()
            list_of_lists.append(line_list)

        a_file.close()
        flag = 0
        index = 0
        dic = {}
        dic1 = {}
        for st in final:
            index = 0
            for line in list_of_lists:
                if st in line[0]:
                    print(st)
                    # dic1['item'] = st
                    # dic1['quantity'] = ''
                    dic1 = {'item': st, "quantity": ''}
                    dic[str(index)] = dic1
                    print(dic)

                    if index > 22:
                        break
                index += 1
        return jsonify(dic)


api.add_resource(yolov5, '/yolo/detection')

shoppinglist = reqparse.RequestParser()
shoppinglist.add_argument('item', type=str, required=True)
shoppinglist.add_argument('quantity', type=str, required=True)

items = json.load(open('/Users/aryan/Desktop/Python/yolo_v5/Flask_API/yolov5_flask_integration/items.json'))

@app.route('/')
def msg():
    return 'hey'


@app.route('/self_order/shopping_list', methods = ['GET'])
def get():
    item_id = str(request.args['item_id'])
    return {item_id: items[item_id]}


class Add_Shopping_List(Resource):

    def get(self, item_id):
        return items[item_id]

    def put(self, item_id):
        args = shoppinglist.parse_args()

        items[item_id] = args

        with open('/Users/aryan/Desktop/Python/yolo_v5/Flask_API/yolov5_flask_integration/items.json', 'w') as fp:
            json.dump(items, fp, indent=4)

        return jsonify({item_id: args})


api.add_resource(Add_Shopping_List, "/self_order/add_shopping_list/<string:item_id>")


class Checkout(Resource):
    def get(self):
        bigbasket.main()
        with open('/Users/aryan/Desktop/Python/yolo_v5/Flask_API/yolov5_flask_integration/items.json', 'w') as fp:
            json.dump({}, fp, indent=4)

        return jsonify({'output': 'DONE SUCESSFULLY'})


api.add_resource(Checkout, '/self_order/checkout')

if __name__ == '__main__':
    app.run(debug=True)

