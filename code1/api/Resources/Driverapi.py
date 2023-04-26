from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Driverapi(Resource):
  #todo
  def get(self):
    records = []

    # Throws error if content of request is not JSON
    if request.content_type != 'application/json':
        abort(400, error="JSON data required")

    provided_fields = set(request.json.keys())
    approved_fields = set(['u_id'])

        # Throws error if fields are incorrect
    if not provided_fields.issubset(approved_fields):
       abort(400, error='Incorrect field usage')
    
    try:
       u_id = request.json['u_id']

       s = """ Select d_id , d_first_name , d_last_name , d_email, d_phone 
               from driver 
               where d_company_id in (SELECT m_company_id FROM member WHERE m_user_id = ?)
       """
       rows = db.engine.execute(s, (u_id))
       for row in rows:
                record = {}
                record['d_id'] =        row[0]
                record['firstname'] =            row[1]
                record['lastname'] =       row[2]
                record['email'] =      row[3]
                record['phone'] =        row[4]
                records.append(record)
    
    except SQLAlchemyError as e:
       return False
    response = {
            'payload': records
        }

    return jsonify(response)
       
       
  def post(self):
    if request.content_type != 'application/json':
            abort(400, error="JSON data required")
        
    provided_fields = set(request.json.keys())
    approved_fields = set(['u_id', 'firstname' , 'middlename' ,'lastname' ,'suffix','address_line_1','address_line_2', 'city', 'email'
                                ,'postal_code' , 'phone', 'd_id' ])
        # Throws error if fields are incorrect
    if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
    try:
    
             #todo
          u_id = request.json['u_id']
          d_id = request.json['d_id']
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
          
          if d_id == 'Empty':
             s = """ WITH cte AS (
                     SELECT d.d_company_id
                     FROM driver d
                     JOIN member m ON d.d_company_id = m.m_company_id
                     WHERE m.m_user_id = ?
                        )
                   INSERT INTO driver (
                  d_company_id, d_first_name, d_address_line_1, d_address_line_2,
                  d_city, d_postal_code, d_phone, d_middle_name, d_last_name,
                  d_email, d_suffix
                ) VALUES (
                (SELECT d_company_id FROM cte),
                  ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?)
                """
             db.engine.execute(s,(  u_id , firstname, address_line_1, address_line_2,city, postal_code, phone, middlename,
                                 lastname,email,suffix, ) )
          else:
           s = """UPDATE driver
                 SET d_first_name = ?, d_address_line_1 = ?, d_address_line_2 = ?,
                d_city = ?, d_postal_code = ?, d_phone = ?,
                d_middle_name = ?, d_last_name = ?, d_email = ?,
                d_suffix = ?, d_company_id = (
               SELECT m_company_id
              FROM member
                 WHERE m_user_id = ?) where d_id = ?;  """
           db.engine.execute(s , (firstname, address_line_1, address_line_2,city, postal_code, phone, middlename,
                                 lastname,email,suffix, u_id, d_id ) )
          
          
    except SQLAlchemyError as e:
        #todo
           
           return jsonify({'success': False})
    return jsonify({'success': True})
  def delete(self):
    if request.content_type != 'application/json':
            abort(400, error="JSON data required")
        
    provided_fields = set(request.json.keys())
    approved_fields = set(['d_id',
                           ])
        # Throws error if fields are incorrect
    if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
    try:
         d_id = request.json['d_id']
         s = """ DELETE from  DRIVER where d_id = ?"""
         db.engine.execute(s, (d_id))
    except SQLAlchemyError as e:
         return False
         

    return True
