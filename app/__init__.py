from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_admin import Admin
from elasticsearch import Elasticsearch

app = Flask(__name__)
cors = CORS(app)
app.config["SECRET_KEY"] = 'f9bf78b9a18ce6d46a0cd2b0b86df9da'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["ELASTICSEARCH_URL"]= "http://localhost:9200"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

admin = Admin(name='Athena')
admin.init_app(app)

app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']])

from app.controller import search_controller, rec_controller, table_controller