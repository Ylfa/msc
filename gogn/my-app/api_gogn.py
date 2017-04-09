from flask import Flask, render_template, request
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gogn.db'
db = SQLAlchemy(app)


class farm_names(db.Model):
    id = Column(Integer, primary_key=True)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=False)
#    year_data = Column(Text, unique=False)
#    name_data = Column(Text, unique=False)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(farm_names, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/area_name', methods=['GET','POST'])
def area_name():
    area_name = request.form['area_name']
    #a = requests.get('api-slóð')
    #json_object = r.json
    #temp_k = json_object['main']['temp']
    return render_template('area_name.html',area_name)


@app.route('/') #root directory
def index():
    return 'This is the homepage.' #app.send_static_file("/Users/ylfa/msc/gogn/my-app/public/index.html")


app.debug = True
if __name__ == "__main__":
    app.run()