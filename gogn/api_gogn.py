from flask import Flask
from flask_restless import APIManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text

app = Flask(__name__, static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gogn.db'
db = SQLAlchemy(app)


class FarmNames(db.Model):
    id = Column(Integer, primary_key=True)
    area_name = Column(Text, unique=False)
    farm_name = Column(Text, unique=False)
#    year_data = Column(Text, unique=False)
#    name_data = Column(Text, unique=False)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(FarmNames, methods=['GET', 'POST', 'DELETE', 'PUT'])


@app.route('/')
def index():
    return app.send_static_file("index.html")

app.debug = True

if __name__ == "__main__":
    app.run()