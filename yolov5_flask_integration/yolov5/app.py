from flask import Flask, jsonify
from flask_restful import Resource, Api
from detect import *

app = Flask(__name__)
api = Api(app)


class Detection(Resource):

    @staticmethod
    def get():
        output = main(parse_opt())
        final = output.split()
        with open("yolov5_flask_integration/yolov5/classes.txt", "r") as a_file:
            list_of_lists = []
            for line in a_file:
                stripped_line = line.strip()
                line_list = stripped_line.split()
                list_of_lists.append(line_list)

        dic = {}
        for st in final:
            index = 0
            for line in list_of_lists:
                if st in line[0]:
                    print(st)
                    dic1 = {'item': st, "quantity": ''}
                    dic[str(index)] = dic1
                    if index > 22:
                        break
                index += 1
        return jsonify(dic)


api.add_resource(Detection, '/yolo/detection')
if __name__ == '__main__':
    app.run(debug=True)
