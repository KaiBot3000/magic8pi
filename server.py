from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Magic(Resource):
    def get(self):
        return {"yes": "it worked"}

api.add_resource(Magic, "/")

if __name__ == "__main__":
    app.run(debug=True)