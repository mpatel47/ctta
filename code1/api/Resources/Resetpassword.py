from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
class Resetpasswordapi(Resource):
    
    def get(self):
        return jsonify({'success': True})

    
    def post(self):
        
        provided_fields = set(request.json.keys())
        approved_fields = set(['u_id', 'password'])
        if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
        try:
            userid = request.json["u_id"]
            password = bcrypt.generate_password_hash(request.json["password"])
            s = """ UPDATE user
                   SET u_password = ?
                   
                  WHERE u_id = ?
                    """
            db.engine.execute(s, (password, userid))
            
            return jsonify({'success': True})
        except SQLAlchemyError as e:
            return jsonify({'success': False})