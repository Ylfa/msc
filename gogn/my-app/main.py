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


class area_id(db.Model):
    area_id = Column(Integer, primary_key=True)
    area_name = Column(Text, unique=True)
    farms = relationship('farm_id', primaryjoin="area_id.area_id==farm_id.area_id")


class farm_id(db.Model):
    farm_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, ForeignKey('area_id.area_id'))
    farm_name = Column(Text, unique=False)
    area_name = Column(Text, unique=False)
    fams = relationship('family_id', primaryjoin="farm_id.farm_id==family_id.farm_id")
    area = relationship('area_id', primaryjoin="farm_id.area_id==area_id.area_id")


class family_id(db.Model):
    family_id = Column(Integer, primary_key=True)
    farm_id = Column(Integer, ForeignKey('farm_id.farm_id'))
    area_id = Column(Integer, ForeignKey('area_id.area_id'))
    area_name = Column(Text, unique=False)
    family_data = Column(Text, unique=False)
    family_year = Column(Text, unique=False)
    farm = relationship('farm_id', primaryjoin="farm_id.farm_id==family_id.farm_id")
    area = relationship('area_id', primaryjoin="and_(area_id.area_id==family_id.area_id,"
                                               "farm_id.area_id==family_id.area_id)")


db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(area_id, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(farm_id, methods=['POST', 'GET', 'DELETE', 'PUT'])
api_manager.create_api(family_id, methods=['POST', 'GET', 'DELETE', 'PUT'])

app.after_request(add_cors_header)


#app.debug = True
if __name__ == "__main__":
    app.run(debug=True)


"""
Byrja á API. Eitt skref í einu, taka út 1-7, hafa sameiginlegt. CHECK!!
Skoða: https://flask-restless.readthedocs.io/en/stable/customizing.html#custom-queries

json parse fyrir str í töflu, import json, skoða: json.dumps CHECK!!!

Lesa búta, þýða ár línur CHECK. held ég...
Spá í None bilum í ártalalista fjölskyldubúta

Skoða birtingu, loada? str í json aftur
"""