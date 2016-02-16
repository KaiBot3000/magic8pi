from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

replies = {
    "english": ["yes", "no", "I think so"],
    # "spanish": ["si", "no", "creo que si"]
}

class Magic(Resource):
    def get(self):
        reply = random.choice(replies["english"])
        return {"reply": reply}

api.add_resource(Magic, "/")

if __name__ == "__main__":
    app.run(debug=True)