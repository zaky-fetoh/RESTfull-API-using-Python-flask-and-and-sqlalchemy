import model
import flask

router = flask.Blueprint("author",__name__)

@router.route("/", methods=["GET"])
def getallAuthor():
    data = model.Author.query.all()
    data =  model.author.AuthorSchema(many=True).dump(data)
    return flask.make_response(flask.jsonify({
        "ok":True, "data": data,
    }))

@router.route("/", methods=["POST"])
def addAuthor():
    author = flask.request.get_json()
    model.author.Author(**author).create()
    return flask.make_response(flask.jsonify({
        "ok": True,
    }))

