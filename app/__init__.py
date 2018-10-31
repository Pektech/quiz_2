from flask import Flask
from flask_ask import Ask

app = Flask(__name__)
ask = Ask(app, "/")

import logging

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


from app import alexa

# from app import mechanics


@app.route("/pek")
def hello_world():
    return "Hello Pek and Monk"


if __name__ == "__main__":
    app.run()
