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

@router.route("/<int:authId>", methods=["GET"])
def getParticularAuhor(authId):
    author = model.Author.query.filter_by(id=authId)
    author = model.AuthorSchema().dump(author)
    return flask.make_response(flask.jsonify({
        "ok": True,
        "data": autor,
    }))


@router.route("/", methods=["POST"])
def addAuthor():
    author = flask.request.get_json()
    model.author.Author(**author).create()
    return flask.make_response(flask.jsonify({
        "ok": True,
    }))

@router.router("/<int:authId>", methods=["DELETE"])
def deleteAuthor(authId):
    AutherObj = model.Author.query.filter_by(id=authId)
    AutherObj.delete()
    return flask.make_response(flask.jsonify({
        "ok":True,
    }))

