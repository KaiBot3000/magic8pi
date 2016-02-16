from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

fortunes = {
    "english": ["yes", "no", "I think so"],
    # "spanish": ["si", "no", "creo que si"]
}

class Magic(Resource):
    def get(self):
        fortune = random.choice(fortunes["english"])
        return {"fortune": fortune}

api.add_resource(Magic, "/")

if __name__ == "__main__":
    app.run(debug=True)