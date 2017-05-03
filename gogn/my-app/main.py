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


class farm_names(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)
#    year_data = Column(Text, unique=True)
#    name_data = Column(Text, unique=True)


class area_id(db.Model):
    area_id = Column(Integer, primary_key=True)
    area_name = Column(Text, unique=True)
#    farms = db.relationship('farm_names')

class farm_names_one(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)

class farm_names_two(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, unique=False)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=True)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(farm_names, methods=['GET', 'POST', 'DELETE', 'PUT'])
api_manager.create_api(area_id, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names_one, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_names_two, methods=['POST', 'GET', 'DELETE', 'PUT'])

app.after_request(add_cors_header)


"""""
@app.route('/area_name', methods=['GET','POST'])
def area_name():
    area_name = request.form['area_name']
    #a = requests.get('api-slóð')
    #json_object = r.json
    #temp_k = json_object['main']['temp']
    return 'This is area_name return' #app.send_static_file('/public/area_name.html')


@app.route('/') #root directory
def index():
    return 'Hello app' #app.send_static_file('/Users/ylfa/msc/gogn/my-app/public/index.html')
"""""

#app.debug = True
if __name__ == "__main__":
    app.run(debug=True)