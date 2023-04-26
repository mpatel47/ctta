from flask import jsonify, request
from flask_restful import Resource, abort
from werkzeug.exceptions import BadRequest
from website.model import db
import datetime
import sqlite3


class Company(Resource):

    def post(self):
        if request.form:
            form = request.form

            try:
                c_name = form["c_name"]
                c_address_line_1 = form["c_address_line_1"]
                c_address_line_2 = form["c_address_line_2"]
                c_city = form["c_city"]
                c_location = form["c_location"]
                c_state_abbreviation = form["c_state_abbreviation"]
                c_postal_code = form["c_postal_code"]
                c_website = form["c_website"]
                c_phone = form["c_phone"]
                c_fax_area_code = form["c_fax_area_code"]
                c_fax = form["c_fax"]
                c_internal_comment = form["c_internal_comment"]

            except Exception as e:
                abort(400, "invalid usage")

            db.engine.execute(
                "insert into company(c_name, c_address_line_1,c_address_line_2,c_city,c_location,c_state_abbreviation,c_postal_code,c_website,c_phone,c_fax_area_code,c_fax,c_internal_comment) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                (
                    c_name,
                    c_address_line_1,
                    c_address_line_2,
                    c_city,
                    c_location,
                    c_state_abbreviation,
                    c_postal_code,
                    c_website,
                    c_phone,
                    c_fax_area_code,
                    c_fax,
                    c_internal_comment,
                ),
            )

        return 200