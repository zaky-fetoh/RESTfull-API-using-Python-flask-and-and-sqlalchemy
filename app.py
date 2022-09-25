import flask
import model
import routes

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
model.db.init_app(app)
with app.app_context():
    model.db.create_all()


app.register_blueprint(routes.author.router, url_prefix="/author")



if __name__ == "__main__":
    app.run(host="localhost",
            port=3000)
