from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_admin import Admin
from elasticsearch import Elasticsearch
from flask_socketio import SocketIO
import os

app = Flask(__name__)
cors = CORS(app)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URL")
app.config["ELASTICSEARCH_URL"]= os.environ.get("ELASTIC_SEARCH")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

admin = Admin(name='Athena')
admin.init_app(app)

app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']])
socketio = SocketIO(app, cors_allowed_origins="*")

from app.controller import search_controller, rec_controller, table_controller, \
    notice_controller, chat_controller
from app.models.course_data import *
from app.models.slots import *
from app.models.course import *
# db.create_all()
# db.session.commit()
