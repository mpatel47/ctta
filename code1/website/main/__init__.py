from flask import Blueprint, render_template,render_template ,url_for, redirect, session, request, flash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from wtforms import validators as vl
from wtforms.fields import HiddenField
from flask_admin.contrib.sqla import ModelView
from functools import wraps


from ..model import Users, db





main = Blueprint('main', __name__, template_folder='templates')

bcrypt = Bcrypt()




### custom wrap to determine access level ###
def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated: #the user is not logged in
                return redirect(url_for('main.login'))

            #user = User.query.filter_by(id=current_user.id).first()

            if not current_user.allowed(access_level):
                flash('You do not have access to this resource.', 'danger')
                return redirect(url_for('main.login'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@main.route("/logout", methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))




@main.route("/", methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(u_username = form.username.data).first()
        if user:
           if bcrypt.check_password_hash(user.u_password, form.password.data):
            login_user(user)
            if user.u_role == 2:
              return redirect(url_for('admin.home'))
            elif user.u_role == 1:
              return redirect(url_for('user.userhome'))
           elif not bcrypt.check_password_hash(user.u_password, form.password.data):
              flash("Password is incorrect")
             
        else:
           flash("Username does not exist")
           
            #return redirect(url_for('student'))

    
    return render_template('login.html', form = form  )


@main.route("/register" ,methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = Users(u_username = form.username.data, u_password = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template("register.html", form = form)



class RegisterForm (FlaskForm):
  organization = StringField( [InputRequired(), Length(min = 4, max =15)],render_kw={"placeholder": "Organization"} )
  username = StringField( [InputRequired(), Length(min = 4, max =15)],render_kw={"placeholder": "Username"} )
  password = PasswordField([InputRequired()], render_kw={"placeholder": "Password"})
  submit = SubmitField("Login")

  def validate_username (self, username):
    existing_user_username = Users.query.filter_by (
        username= username.data).first()
    if existing_user_username:
        raise ValidationError ("Username already exists!")

class LoginForm (FlaskForm):
  username = StringField( [InputRequired(), Length(min = 4, max =15)],render_kw={"placeholder": "Username"} )
  password = PasswordField([InputRequired()], render_kw={"placeholder": "Password"})
  submit = SubmitField("Login")