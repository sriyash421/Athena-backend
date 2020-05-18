from flask import jsonify, request
from flask_socketio import send

from app import app, db, socketio
from app.models.course import Course, Message, User


@app.route("/chat", methods=['GET','POST','OPTIONS'])
def chat() :
    courses = Course.query.all()
    temp = list(set([i.course_id for i in courses]))
    return jsonify({'data':temp}), 200

@app.route("/get_chat/<subject>", methods=['GET','POST','OPTIONS'])
def get_chat(subject) :
    messages = Message.query.all()
    temp = []
    if len(messages) > 0 :
        temp = [i for i in messages if Course.query.get(i.subject).course_id == subject]
    temp = [{'content':i.content,'author':User.query.get(i.user_id).ip_address, 'id':i.user_id} for i in temp]
    print(temp)
    return jsonify({'data':temp}), 200

@socketio.on('message')
def handleMessage(data) :
    temp = data.split("?@?")
    content = temp[0]
    user_ip = temp[1]
    course_id = temp[2]
    print(temp)
    users = User.query.filter_by(ip_address=user_ip).all()
    if not (len(users)) :
        temp = User(ip_address=user_ip, status=True, downvotes=0)
        db.create_all()
        db.session.add(temp)
        db.session.commit()
    course_id = Course.query.filter_by(course_id=course_id).first().id
    user_id = User.query.filter_by(ip_address=user_ip).first().id
    message = Message(content=content, user_id=user_id, subject=course_id)
    db.session.add(message)
    db.session.commit()
    tag = "?@?"
    data = content+tag+str(user_id)+tag+user_ip
    send(data, broadcast = True)
