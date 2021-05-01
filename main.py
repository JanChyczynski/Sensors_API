from flask import Flask
from flask_restful import Api, Resource
from sensor import Sensor

app = Flask(__name__)
api = Api(app)

sensors = {}

class Sensors_res(Resource):
    def __init__(self):
        self.counter = len(sensors)

    def get(self):
        return {key: sensors[key].__dict__() for key in sensors.keys()}


api.add_resource(Sensors_res, "/sensors")

if __name__ == "__main__":
    app.run(debug=True)