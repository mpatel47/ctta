from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Editdriverapi(Resource):
  #todo

      
  def get(self, id):
    records = []

    # Throws error if content of request is not JSON
    if request.content_type != 'application/json':
        abort(400, error="JSON data required")


    
    try:
       d_id = id

       s = """ Select d_first_name , d_last_name , d_email, d_phone, d_address_line_1,d_address_line_2, d_postal_code,d_city,d_suffix, d_middle_name  
               from driver 
               where d_id = ?
       """
       rows = db.engine.execute(s, (d_id))
       for row in rows:
                record = {}
                record['firstname'] =            row[0]
                record['lastname'] =       row[1]
                record['email'] =      row[2]
                record['phone'] =        row[3]
                record['d_address_line_1'] =        row[4]
                record['d_address_line_2'] =        row[5]
                record['d_postal_code'] =        row[6]
                record['d_city'] =        row[7]
                record['d_suffix'] =        row[8]
                record['d_middle_name'] =        row[9]
                records.append(record)
    
    except SQLAlchemyError as e:
       return False
    response = {
            'payload': records
        }

    return jsonify(response)
       
       
  def post(self, id):
    if request.content_type != 'application/json':
            abort(400, error="JSON data required")
        
    provided_fields = set(request.json.keys())
    approved_fields = set(['d_id', 'firstname' , 'middlename' ,'lastname' ,'suffix','address_line_1','address_line_2', 'city', 'email'
                                ,'postal_code' , 'phone' ])
        # Throws error if fields are incorrect
    if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
    try:
    
             #todo
          d_id = id
          firstname = request.json['firstname']
          middlename =request.json['middlename']
          lastname = request.json['lastname']
          suffix = request.json['suffix']
          address_line_1 = request.json['address_line_1']
          address_line_2 = request.json['address_line_2']
          city = request.json['city']
          postal_code = request.json['postal_code']
          phone = request.json['phone']
          email = request.json['email']

          #sql = """ Select d_id
               #from driver 
               #where d_company_id in (SELECT m_company_id FROM member WHERE m_user_id =? ) """
          #d_id = db.session.execute(sql,(u_id) )
          #db.session.close()
          #if d_id == None:
              #return "no driver"
          #else:
          
         
          s = """UPDATE driver
                 SET d_first_name = ?, d_address_line_1 = ?, d_address_line_2 = ?,
                d_city = ?, d_postal_code = ?, d_phone = ?,
                d_middle_name = ?, d_last_name = ?, d_email = ?,
                d_suffix = ? 
                where d_id = ?  """
          db.engine.execute(s , (firstname, address_line_1, address_line_2,city, postal_code, phone, middlename,
                                 lastname,email,suffix,d_id ) )
          
          
    except SQLAlchemyError as e:
        #todo
           
           return jsonify({'success': False})
    return jsonify({'success': True})
