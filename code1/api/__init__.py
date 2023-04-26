from flask_restful import Api
from api.Resources.Class import Class
from api.Resources.Userapi import Userapi
from api.Resources.Driverapi import Driverapi



'''
    Guidelines:
        -When to allow request to use a json payload or url query parameter?
            Use json payloads when request are complex and leave simple task like filtering to url query parameters
'''

def create_api(app):
    
    api = Api(app)

    api.add_resource(Class, "/class")
    api.add_resource(Userapi, "/userinfo")
    api.add_resource(Driverapi, "/driver")
 



    return api