import flask_sqlalchemy as alchemy
import flask
import model

router = flask.Blueprint("book", __name__)


@router.route("/", methods=["GET"])
def getAllBooks():
    books = model.Book.query.all()
    books = model.BookSchema(many=True).dump(books)
    return flask.make_response(flask.jsonify({
        "ok": True,
        "data": books,
    }))


@router.route("/<int:bookId>", methods=["GET"])
def getAparticulerBook(bookId):
    book = model.Book.query.filter_by(id=bookId)
    try:
        book = model.db.session.execute(book).one()
    except alchemy.orm.exc.NoResultFound:
        return flask.make_response(flask.jsonify({
            "ok": False,
        }), 404)
    book = model.BookSchema().dump(book[0])
    return flask.make_response(flask.jsonify({
        "ok": True, "data": book,
    }))


@router.route("/", methods=["POST"])
def addBook():
    jBook = flask.request.get_json()
    model.Book(**jBook).create();
    return flask.make_response(flask.jsonify({
        "ok": True,
    }))


@router.route("/<int:BookId>", methods=["DELETE"])
def deleteBook(BookId):
    book = model.Book.query.filter_by(id=BookId)
    try:
        book = model.db.session.execute(book).one()
    except alchemy.orm.exc.NoResultFound:
        return flask.make_response(flask.jsonify({
            "ok": False,
        }), 404)
    book[0].delete()
    return flask.make_response(flask.jsonify({
        "ok": True,
    }))
