
from flask import Flask
from statuser import status

app = Flask(__name__)

@app.route("/")
def beat():
    return str(status())


if __name__ == "__main__":
    app.run()

