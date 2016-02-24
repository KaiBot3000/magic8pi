from flask import Flask
from flask_restful import Api
from magic import replies, Magic, Language

app = Flask(__name__)
api = Api(app)

api.add_resource(Magic, "/magic8pi/v1/", "/magic8pi/v1/<string:language>")
api.add_resource(Language, "/magic8pi/v1/languages")


if __name__ == "__main__":
    app.run(debug=True)