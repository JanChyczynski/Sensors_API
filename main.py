from flask import Flask, abort
from flask_restful import Api, Resource, reqparse

from sensor import Sensor

app = Flask(__name__)
api = Api(app)

sensors_post_args = reqparse.RequestParser()
sensors_post_args.add_argument("address", type=str, help="The address of the sensor is required", required=True)
sensors_post_args.add_argument("owner", type=str, help="The name of the owner of the sensor is required", required=True)
sensor_patch_args = reqparse.RequestParser()
sensor_patch_args.add_argument("address", type=str)
sensor_patch_args.add_argument("owner", type=str)

sensors = {}

def assert_sensor_exists(id):
    if id not in sensors:
        abort(404, "No sensor with given ID")


class Sensor_res(Resource):
    def get(self, id):
        assert_sensor_exists(id)
        return sensors[id].__dict__()

    def patch(self, id):
        assert_sensor_exists(id)
        args = dict(sensor_patch_args.parse_args())
        print(args)
        if "address" in args and args["address"] is not None:
            sensors[id].address = args["address"]
        if "owner" in args and args["owner"] is not None:
            sensors[id].owner = args["owner"]
        return "", 204

    def delete(self, id):
        assert_sensor_exists(id)
        sensors.pop(id)
        return "", 204


class Sensors_res(Resource):
    def __init__(self):
        self.counter = len(sensors)

    def get(self):
        return {key: sensors[key].__dict__() for key in sensors.keys()}

    def post(self):
        args = sensors_post_args.parse_args()
        sensors[self.counter] = Sensor(address=args["address"], owner=args["owner"])
        self.counter += 1
        return {"message": "posted", "id": self.counter - 1}, 201


api.add_resource(Sensor_res, "/sensor/<int:id>")
api.add_resource(Sensors_res, "/sensors")

if __name__ == "__main__":
    app.run(debug=False)
