import flask_sqlalchemy as alchemy
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
    try:
        author = model.db.session.execute(author).one()
    except alchemy.orm.exc.NoResultFound:
        return flask.make_response(flask.jsonify({
            "ok": True,
            "data": [],
        }))
    author = model.AuthorSchema().dump(author[0])
    return flask.make_response(flask.jsonify({
        "ok": True,
        "data": author,
    }))


@router.route("/", methods=["POST"])
def addAuthor():
    author = flask.request.get_json()
    model.author.Author(**author).create()
    return flask.make_response(flask.jsonify({
        "ok": True,
    }))

@router.route("/<int:authId>", methods=["DELETE"])
def deleteAuthor(authId):
    AuthorObj = model.Author.query.filter_by(id=authId)
    try:
        AuthorObj = model.db.session.execute(AuthorObj).one()
    except alchemy.orm.exc.NoResultFound :
        return flask.make_response(flask.jsonify({
            "ok": False,
        }), 404)
    AuthorObj[0].delete()
    return flask.make_response(flask.jsonify({
        "ok":True,
    }))

