from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Commentapi(Resource):
    
    def get(self):
        return jsonify({'success': True})

    
    def post(self):
        records = []
        provided_fields = set(request.json.keys())
        approved_fields = set(['u_id', 'comment'])
        if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
        try:
            userid = request.json["u_id"]
            comment = request.json["comment"]
            s = """ UPDATE company
                   SET 
                   c_internal_comment = ?
                  WHERE c_id IN (
                    SELECT m_company_id FROM member WHERE m_user_id = ?
                     );
                    """
            rows = db.engine.execute(s, (comment, userid))
            for row in rows:
                record = {}
                record['c_name'] = row[0]              
                records.append(record)
            return jsonify({'success': True, 'data': records})
        except SQLAlchemyError as e:
            return jsonify({'success': False})