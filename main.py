from flask import Flask
from flask_restful import Api, Resource, reqparse
from sensor import Sensor

app = Flask(__name__)
api = Api(app)

sensors_post_args = reqparse.RequestParser()
sensors_post_args.add_argument("address", type=str, help="The address of the sensor is required", required=True)
sensors_post_args.add_argument("owner", type=str, help="The name of the owner of the sensor is required", required=True)

sensors = {}

class Sensors_res(Resource):
    def __init__(self):
        self.counter = len(sensors)

    def get(self):
        return {key: sensors[key].__dict__() for key in sensors.keys()}

    def post(self):
        args = sensors_post_args.parse_args()
        sensors[self.counter] = Sensor(address=args["address"], owner=args["owner"])
        self.counter += 1
        return {"message": "posted", "id": self.counter-1}, 201

api.add_resource(Sensors_res, "/sensors")

if __name__ == "__main__":
    app.run(debug=True)