import flask


app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def getRout():
    return "hello"


if __name__ == "__main__":
    app.run(host="localhost",
            port=3000)
