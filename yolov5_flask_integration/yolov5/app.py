from flask import Flask, jsonify
from detect import *

app = Flask(__name__)


@app.route('/yolo/detection', methods = ['GET'])
def yolov5():
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


if __name__ == '__main__':
    app.run(debug=True)

