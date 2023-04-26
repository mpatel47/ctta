from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Autocompleteapi(Resource):
    
    def get(self):
        return jsonify({'success': True})

    
    def post(self):
        records = []
        provided_fields = set(request.json.keys())
        approved_fields = set(['search'])
        if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
        try:
            searchbox = request.json["search"]
            s = """SELECT c_name FROM company WHERE c_name LIKE '{}%' LIMIT 10""".format(searchbox)
            rows = db.engine.execute(s)
            for row in rows:
                record = {}
                record['c_name'] = row[0]              
                records.append(record)
            return jsonify({'success': True, 'data': records})
        except SQLAlchemyError as e:
            return jsonify({'success': False})

       
       
 