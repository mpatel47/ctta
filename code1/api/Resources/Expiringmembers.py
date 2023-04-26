from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime

import sqlalchemy
from sqlalchemy.exc import SQLAlchemyError

class Expiringmemberapi(Resource):

  def get(self):
    try:
        current_date = datetime.datetime.now()
        thirty_days_from_now = current_date + datetime.timedelta(days=30)
        s = """SELECT c_name, c_location, m_membership_tier, u_email, m_membership_expiration
             FROM member
             INNER JOIN user ON m_user_id = u_id
             INNER JOIN company ON m_company_id = c_id"""
        data = db.engine.execute(s)
        result = []

        for row in data:
            if row[4]:
                row_date = datetime.datetime.strptime(row[4], '%m/%d/%Y %H:%M')
                if current_date <= row_date <= thirty_days_from_now:
                    company_information = {
                        'name': row[0],
                        'association': row[1],
                        'tier': row[2],
                        'expiration_date': row[4],
                        'expiring_email': row[3]
                    }
                    result.append(company_information)
                else:
                    continue

        if not result:
            return jsonify({'message': 'No expiring memberships found.'})
        count = len(result)
        response = {'count': count, 'payload': result}
        return jsonify(response)

    except SQLAlchemyError as e:
        return jsonify({'message': 'An error occurred while processing your request.'})
    
  
  

                
