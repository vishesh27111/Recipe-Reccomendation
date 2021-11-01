from flask import Flask, jsonify
from flask_restful import Resource, Api
from recommender import *

app = Flask(__name__)
api = Api(app)


class Recommender(Resource):

    @staticmethod
    def get():
        recommendation = recommender()
        rec = {}
        i = 0
        for j in recommendation:
            rec[i] = j
            i += 1

        print(rec)
        return rec


api.add_resource(Recommender, '/recommender/content')


if __name__ == '__main__':
    app.run(debug=True)
