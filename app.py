import flask


app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def getRout():
    p = flask.jsonify({
        "name":"WEWEW", 
        "SAdss":3223
    })
    print(p)
    return flask.make_response(p )


@app.route("/", methods= ["POST"])
def pot():
    data = flask.request.get_json()
    print( type(data) )
    


if __name__ == "__main__":
    app.run(host="localhost",
            port=3000)
