from flask import Flask
from website.admin import admin
from website.user import user 
from website.main import main

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from .model import Users

db_name = "ctta_database"

def create_app():
        
        app = Flask(__name__)
        app.register_blueprint(main)
        app.register_blueprint(user, url_prefix='/users' )
        app.register_blueprint(admin, url_prefix='/admins')
   
       
        app.config['SECRET_KEY'] = 'cttaersca'
        #app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@127.0.0.1:3306/{db_name}'

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ctta_database.sqlite'
        #store the database locally in the instance folder

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        from .model import db
        
        db.init_app(app)

        



        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = 'login'
        
        
        @login_manager.user_loader
        def load_user(user_id):
            return Users.query.get(user_id)
        

        return app



 




