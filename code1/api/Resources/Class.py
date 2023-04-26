from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
import datetime
import sqlite3

class Class(Resource):

    def __init__(self):

        try:
            self.conn = sqlite3.connect('./code/instance/ctta_database.sqlite')
            self.conn.row_factory = sqlite3.Row
            self.cur = self.conn.cursor()

        except sqlite3.Error as e:
            abort(500)

    def get(self):
        classes = []
        page_number = 1
        page_size = 10
        
        try:

            if request.args:
                page_number = int(request.args['page_number'])

            offset = (page_number - 1) * page_size


            self.cur.execute("select * from class limit ? offset ?", (page_size, offset))
           
            rows = self.cur.fetchall()

            for row in rows:
                record = {}
                
                for key in row.keys():
                    record[key] = row[key]

                classes.append(record)

        except sqlite3.Error as e:
            abort(500, error='Could not process request')
            classes = []

        self.cur.execute("select count(*) from class")

        total_records = self.cur.fetchone()[0]

        total_pages = total_records // page_size

        total_pages = 1 if total_pages == 0 else total_pages

        response = {
            'payload': classes,
            'currentPage': page_number,
            'pageSize': page_size,
            'totalRecords': total_records,
            'totalPages': total_pages
        }

        self.conn.close()
        
        return jsonify(response)
    
    def post(self):

        if request.json:
            json = request.get_json()

            cl_time = json['cl_time']
            cl_zoom_link = json['cl_zoom_link']
        
        return jsonify({'message': 'post request received'})