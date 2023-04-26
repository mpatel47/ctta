from website import create_app
from website.model import db
from api import create_api
from flask import jsonify

app = create_app()

api = create_api(app)



@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
    app.app_context()
    #with app.app_context():
     #db.create_all()
    app.run()
