from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Transferdriverapi(Resource):
    
    def get(self):

        return jsonify({'success': True})
    
    def post(self, d_id):

        if request.content_type != 'application/json':
            abort(400, error="JSON data required")
        
        provided_fields = set(request.json.keys())
        approved_fields = set([ 'c_name' ])
        # Throws error if fields are incorrect
        if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
        try:
    
             #todo
          driver_id = d_id
          cname = request.json['c_name']
          

         
          s = """UPDATE driver
                 SET d_company_id = (select c_id from company where c_name = ?)
                where d_id = ?  """
          db.engine.execute(s , (cname , driver_id ) )
          
          
        except SQLAlchemyError as e:
        #todo
           
           return jsonify({'success': False})
        return jsonify({'success': True})            

    
    