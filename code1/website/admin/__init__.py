from flask import Blueprint, render_template, jsonify, url_for
from website.main import requires_access_level, login_required
from ..model import ACCESS, db

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')


@admin.route("/home", methods = ['GET'])
@login_required
@requires_access_level(ACCESS['admin'])
def home():
    s = """select c_name , c_location, m_membership_tier, m_user_id,
CASE 
when s.m_membership_expiration > date('now') then 'Active'
else 'Expired'
end as expstatus
from 
(Select c_name, c_location, m_membership_tier, m_membership_expiration, m_user_id
           from member 
           inner join company 
           where m_company_id = c_id) as s;"""
    data = db.engine.execute(s)
    result=[]
    for row in data:
        companyinformation = {}
        companyinformation['name'] = row[0]
        companyinformation['association'] = row[1]
        companyinformation['tier'] = row[2]
        companyinformation['userid'] = row[3]
        companyinformation['status'] = row[4]
        result.append(companyinformation)
    #return jsonify(result)

    return render_template("adminhome.html", companyinfo = result)

@admin.route("/admin/<int:user_id>")
@login_required
@requires_access_level(ACCESS['admin'])
def adminviewuserinfo(user_id):
    userid = user_id
    return render_template("memberinfo.html")



@admin.route("/courseinfo")
@login_required
@requires_access_level(ACCESS['admin'])
def courseinfo():
    return render_template("courseinfo.html")

@admin.route("/memberinfo")
@login_required
@requires_access_level(ACCESS['admin'])
def adminviewmemberinfo():
    return render_template("memberinfo.html")

@admin.route("/passwordreset")
@login_required
@requires_access_level(ACCESS['admin'])
def adminviewpasswordreset():
    return render_template("passwordreset.html")

@admin.route("/report")
@login_required
@requires_access_level(ACCESS['admin'])
def adminviewreport():
    
    return render_template("report.html")