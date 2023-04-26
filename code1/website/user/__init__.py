from flask import Blueprint, render_template
from ..main import login_required

user = Blueprint('user', __name__, template_folder='templates', static_folder='static')

@user.route("/home")
@login_required
def userhome():
    return render_template("userhome.html" )

@user.route("/userinfo")
@login_required
def userinfo():
    return render_template("userinfo.html")

@user.route("/courseregistration")
@login_required
def courseregistration():
    return render_template("courseregistration.html" )

@user.route("/coursepayment")
@login_required
def coursepayment():
    return render_template("coursepayment.html" )

@user.route("/coursesearch")
@login_required
def coursesearch():
    return render_template("coursesearch.html" )

@user.route("/searchmember")
@login_required
def searchmember():
    return render_template("searchmember.html" )

@user.route("/employeemanager")
@login_required
def employeemanager():
    return render_template("employeemanager.html" )