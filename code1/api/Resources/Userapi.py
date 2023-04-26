from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Userapi(Resource):

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

            sql = """
                    select c_name , u_firstname , u_middlename, u_lastname, u_suffix, c_address_line_1, c_address_line_2, c_city, c_location, c_postal_code,
                    c_website,c_phone, c_fax, m_fleet_size
                    from company, user, member
                    where u_id = ? and  m_user_id = u_id and m_company_id = c_id ;
                """
            
            rows = db.engine.execute(sql, (u_id))

            #rows = self.cur.fetchall()
            
            for row in rows:
                record = {}
                record['name'] =            row[0]
                record['firstname'] =       row[1]
                record['middlename'] =      row[2]
                record['lastname'] =        row[3]
                record['suffix'] =          row[4]
                record['address_line_1'] =  row[5]
                record['address_line_2'] =  row[6]
                record['city'] =            row[7]
                record['location'] =        row[8]
                record['postal_code'] =     row[9]
                record['website'] =         row[10]
                record['phone'] =           row[11]
                record['fax'] =             row[12]
                record['fleetsize'] =       row[13]
                records.append(record)
            
        except db.Error as e:
            abort(500, error='Could not process request')

        response = {
            'payload': records
        }

        return jsonify(response)
    def post(self): 
       #todo
        if request.content_type != 'application/json':
            abort(400, error="JSON data required")
        
        provided_fields = set(request.json.keys())
        approved_fields = set(['u_id','name', 'firstname' , 'middlename' ,'lastname' ,'suffix','address_line_1','address_line_2', 'city', 
                               'location' ,'postal_code' ,'website', 'phone' ,'fax' ,'fleetsize' ])
        # Throws error if fields are incorrect
        if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
        
        
        
        try:
             #todo
          u_id = request.json['u_id']
          name = request.json['name']
          firstname = request.json['firstname']
          middlename =request.json['middlename']
          lastname = request.json['lastname']
          suffix = request.json['suffix']
          address_line_1 = request.json['address_line_1']
          address_line_2 = request.json['address_line_2']
          city = request.json['city']
          location = request.json['location']
          postal_code = request.json['postal_code']
          website = request.json['website']
          phone = request.json['phone']
          fax = request.json['fax']
          fleetsize = request.json['fleetsize']

          s = """ UPDATE company , user , member 
                  SET 
                  c_name = ? , u_firstname = ?  , u_middlename = ? , u_lastname = ? , u_suffix = ? , c_address_line_1 = ? ,
                  c_address_line_2 = ? , c_city = ?, c_location = ? , c_postal_code = ? ,
                  c_website = ?,c_phone = ? , c_fax = ? , m_fleet_size = ?
                  WHERE 
                  u_id = ? and  m_user_id = u_id and m_company_id = c_id ;
              """
          s1 = """ UPDATE company
                   SET 
                  c_name = ?, c_address_line_1 = ?, c_address_line_2 = ?, c_city = ?, c_location = ?, c_postal_code = ?, c_website = ?, c_phone = ?, c_fax = ?
                  WHERE c_id IN (
                    SELECT m_company_id FROM member WHERE m_user_id = ?
                     );
               """
          s2 = """ UPDATE user
                   SET 
                   u_firstname = ?, u_middlename = ?, u_lastname = ?, u_suffix = ?
                  WHERE u_id = ?;
                """
          s3 = """ UPDATE member
                  SET 
                 m_fleet_size = ?
                 WHERE m_user_id = ?;
          
               """
          #db.engine.execute(s1,(name,firstname,middlename,lastname,suffix,address_line_1,address_line_2, city, 
                               #location,postal_code,website, phone,fax,fleetsize, u_id) )
          db.engine.execute(s1,(name,address_line_1, address_line_2,city,location,postal_code, website, phone,fax,u_id ))
          db.engine.execute(s2,(firstname,middlename,lastname,suffix, u_id))
          db.engine.execute(s3,(fleetsize, u_id))


        except SQLAlchemyError as e :
            #todo
            #print (e)
            return False


        return True
    def delete():
        if request.content_type != 'application/json':
            abort(400, error="JSON data required")
        
        provided_fields = set(request.json.keys())
        approved_fields = set(['u_id',
                           ])
        # Throws error if fields are incorrect
        if not provided_fields.issubset(approved_fields):
            abort(400, error='Incorrect field usage')
        try:
           u_id = request.json['u_id']
           s = """ DELETE from  USER where u_id = ?"""
           db.engine.execute(s, (u_id))
        except SQLAlchemyError as e:
         return False
        #todo
        return True
    
