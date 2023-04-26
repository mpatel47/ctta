from flask_login import UserMixin

from flask_sqlalchemy import SQLAlchemy




#db = SQLAlchemy()
db = SQLAlchemy()



ACCESS = {
    
    'member': 1,
    'admin': 2
}



class Users(UserMixin, db.Model):

    __tablename__ = 'user'

    u_id =                          db.Column(db.Integer, primary_key = True)
    u_username =                    db.Column(db.String, nullable = False, unique = True)
    u_password =                    db.Column(db.String, nullable = False)
    u_email =                       db.Column(db.String, nullable = False)
    u_firstname =                   db.Column(db.String, nullable = False)
    u_middlename =                  db.Column(db.String, nullable = True)
    u_lastname =                    db.Column(db.String, nullable = False)
    u_suffix =                      db.Column(db.String, nullable = True)
    u_role =                        db.Column(db.Integer, default = 1)


    def get_id(self):
        return self.u_id

    def check_password(self, password):
        return self.u_password == password
    
    def is_admin(self):
        return self.u_role == ACCESS['admin']

    def is_user(self):
        return self.u_role == ACCESS['member']
    def allowed(self, access_level):
        return self.u_role >= access_level

class Tier(db.Model):
    __tablename__ = 'tier'

    t_id =                          db.Column(db.Integer, primary_key = True)
    t_name =                        db.Column(db.String, nullable = False)
    t_cost =                        db.Column(db.Float, nullable = False)

class Member(db.Model):

    __tablename__ = 'member'

    m_id =                          db.Column(db.Integer, primary_key = True)
    m_user_id =                     db.Column(db.String, db.ForeignKey('user.u_id'), nullable = False)
    m_tier_id =                     db.Column(db.Integer, db.ForeignKey('tier.t_id'), nullable = False)
    m_company_id =                  db.Column(db.Integer, db.ForeignKey('company.c_id'), nullable = False)
    m_registration_date =           db.Column(db.DateTime, nullable = False)
    m_approved_site_member =        db.Column(db.Integer, nullable = False)
    m_date_approved =               db.Column(db.DateTime, nullable = False)
    m_last_login =                  db.Column(db.DateTime, nullable = True)
    m_suspended =                   db.Column(db.Boolean, nullable = False)
    m_last_updated =                db.Column(db.DateTime, nullable = False)
    m_membership_tier =             db.Column(db.String, nullable = False)
    m_has_donated =                 db.Column(db.Boolean, nullable = False)
    m_has_purchased_online =        db.Column(db.Boolean, nullable = False)
    m_last_purchase =               db.Column(db.DateTime, nullable = True)
    m_has_registeration_event_online = db.Column(db.Boolean, nullable = False)
    m_last_event_registered =       db.Column(db.DateTime, nullable = True)
    m_code =                        db.Column(db.String, nullable = False)
    m_date_last_renewed =           db.Column(db.DateTime, nullable = True)
    m_membership_expiration =       db.Column(db.DateTime, nullable = False)
    m_voting_district =             db.Column(db.String, nullable = False)
    m_fleet_size =                  db.Column(db.Integer, nullable = False)

class Company(db.Model):

    __tablename__ = 'company'

    c_id =                          db.Column(db.Integer, primary_key = True)
    c_name =                        db.Column(db.String, nullable = False)
    c_address_line_1 =              db.Column(db.String, nullable = False)
    c_address_line_2 =              db.Column(db.String, nullable = True)
    c_city =                        db.Column(db.String, nullable = False)
    c_location =                    db.Column(db.String, nullable = False)
    c_state_abbreviation =          db.Column(db.String(2), nullable = False)
    c_postal_code =                 db.Column(db.String(5), nullable = False)
    c_website =                     db.Column(db.String, nullable = True)
    c_phone =                       db.Column(db.String(10), nullable = False)
    c_fax_area_code =               db.Column(db.String(3), nullable = True)
    c_fax =                         db.Column(db.String(10), nullable = True)
    c_internal_comment =            db.Column(db.String, nullable = True)

class Driver(db.Model):

    __tablename__ = 'driver'

    d_id =                          db.Column(db.Integer, primary_key = True)
    d_company_id =                  db.Column(db.Integer, db.ForeignKey('company.c_id'), nullable = True)
    d_email =                       db.Column(db.String, nullable = False)
    d_phone =                       db.Column(db.String, nullable = False)
    d_address_line_1 =              db.Column(db.String, nullable = False)
    d_address_line_2 =              db.Column(db.String, nullable = True)
    d_postal_code =                 db.Column(db.String(5), nullable = True)
    d_city =                        db.Column(db.String, nullable = False)
    d_first_name =                  db.Column(db.String, nullable = False)
    d_middle_name =                 db.Column(db.String, nullable = True)
    d_last_name =                   db.Column(db.String, nullable = False)
    d_suffix =                      db.Column(db.String, nullable = False)

class Class(db.Model):
    
    __tablename__ = 'class'

    cl_id =                         db.Column(db.Integer, primary_key = True)
    cl_time =                       db.Column(db.DateTime, nullable = False)
    cl_zoom_link =                  db.Column(db.String, nullable = False)


class Attendance(db.Model):

    __tablename__ = 'attendance'
    
    a_id =                  db.Column(db.Integer, primary_key = True)
    a_class_id =            db.Column(db.Integer, db.ForeignKey('class.cl_id'), nullable = False)
    a_driver_id =           db.Column(db.Integer, db.ForeignKey('driver.d_id'), nullable = False)
    a_attended =            db.Column(db.Boolean, nullable = False)


class Report(db.Model):

    __tablename__ = 'report'

    r_id =                  db.Column(db.Integer, primary_key = True)
    r_timestamp =           db.Column(db.DateTime, nullable = False)
    r_report =              db.Column(db.LargeBinary, nullable = False)

class Industry_Partners(db.Model):
    
    __tablename = 'industry_partners'

    ip_id =                 db.Column(db.Integer, primary_key = True)
    ip_name =               db.Column(db.String, nullable = False)
    ip_type =               db.Column(db.String, nullable = False)
    ip_address_line_1 =     db.Column(db.String, nullable = False)
    ip_address_line_2 =     db.Column(db.String, nullable = True)
    ip_postal_code =        db.Column(db.String(5), nullable = False)
    ip_website =            db.Column(db.String, nullable = True)
    ip_phone =              db.Column(db.String(10), nullable = False)
    ip_internal_comment =   db.Column(db.String, nullable = True)


    