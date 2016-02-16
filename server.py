from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

replies = {
    "english": ["yes", "no", "I think so"],
    "spanish": ["si", "no", "creo que si"],
    "cat": ["purrrfectly possible", "hiss no", "mouse certainly"],
    "french": ["a chaque jour suffit sa peine", "non", "c'est kif-kif et bourricot",
                "ce ne sont pas vos oignons", "la mort du petit cheval",
                "qui vivra, verra", "sans l'ombre d'un doute",
                "triste comme un repas sans fromage"]
}

class Magic(Resource):
    def get(self, language="english"):
        """Given a language (english is default), returns random reply"""

        reply = random.choice(replies[language])
        return {"reply": reply}

class Language(Resource):
    def get(self):
        """Returns a list of available languages"""
        
        languages = replies.keys()
        return {"languages": languages}



api.add_resource(Magic, "/", "/<string:language>")
api.add_resource(Language, "/languages")


if __name__ == "__main__":
    app.run(debug=True)