from flask import Flask, render_template, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gogn.db'
db = SQLAlchemy(app)


def add_cors_header(response):
    allow = 'GET'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = allow
    response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

class farm_family(db.Model):
    family_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    farm_name = Column(Text, unique=False)
    farm_id = Column(Integer, unique=False)
    family_year = Column(Text, unique=False)
    family_data = Column(Text, unique=False)
    farm_id = relationship("farm_names",
                           primaryjoin="and_(farm_names.farm_name==farm_family.farm_name,"
                           "farm_names.area_id==farm_family.area_id,"
                           "farm_names.farm_id==1)")
                    #primaryjoin="and_(User.id==Address.user_id, "
                    #    "Address.city=='Boston')")

class farm_fams1(db.Model):
    farm_id = Column(Integer, unique=False)
    family_id = Column(Integer, primary_key=True)
    farm_name = Column(Text, unique=False)
    family_year = Column(Text, unique=False)
    family_data = Column(Text, unique=False)

class farm_names(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, ForeignKey('farm_family.area_id'))
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, ForeignKey('farm_family.farm_name'))
#    year_data = Column(Text, unique=True)
#    name_data = Column(Text, unique=True)
#    farm_id = relationship('farm_id', ForeignKey('farm_family.farm_name'))


class area_id(db.Model):
    area_id = Column(Integer, primary_key=True)
    area_name = Column(Text, unique=True)

class farm_names1(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)
class farm_names2(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)
class farm_names3(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)
class farm_names4(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)
class farm_names5(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)
class farm_names6(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)
class farm_names7(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
    year_data = Column(Text, unique=True)
    name_data = Column(Text, unique=True)



db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(farm_names, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(area_id, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names1, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names2, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names3, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names4, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names5, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names6, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names7, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_family, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_fams1, methods=['POST', 'GET', 'DELETE', 'PUT'])

app.after_request(add_cors_header)



#app.debug = True
if __name__ == "__main__":
    app.run(debug=True)