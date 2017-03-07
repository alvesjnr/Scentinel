
from flask import Flask
from statuser import status


app = Flask(__name__)
PORT = 5678 #FIXME: read it from config.ini file

@app.route("/")
def beat():
    return str(status())


if __name__ == "__main__":
    app.run(port=PORT)


