from flask import jsonify, request

from app import app, db
from app.models.course import Course, Notice, User


@app.route("/add_notice", methods=['GET','POST','OPTIONS'])
def add_notice() :
    if request.method == 'POST' :
        post = request.get_json()
        print(post)
        users = User.query.filter_by(ip_address=post['author']).all()
        if not (len(users)) :
            temp = User(ip_address=post['author'], status=True, downvotes=0)
            db.create_all()
            db.session.add(temp)
            db.session.commit()
        course_id = Course.query.filter_by(course_id=post['course']).first().id
        user_id = User.query.filter_by(ip_address=post['author']).first().id
        temp = Notice(content=post['content'], user_id=user_id, subject=course_id)
        db.create_all()
        db.session.add(temp)
        db.session.commit()
    return jsonify({"status":"Success"}), 200

@app.route("/notice", methods=['GET','POST','OPTIONS'])
def notice() :
    courses = Course.query.all()
    temp = list(set([i.course_id for i in courses]))
    return jsonify({'data':temp}), 200

@app.route("/delete_notice/<id>", methods=['GET','POST','OPTIONS'])
def delete_notice(id) :
    temp = Notice.query.get(id)
    db.session.delete(temp)
    db.session.commit()
    return {}, 200    

@app.route("/get_notice/<subject>", methods=['GET','POST','OPTIONS'])
def get_notice(subject) :
    notices = Notice.query.all()
    notices = [i for i in notices if Course.query.get(i.subject).course_id == subject]
    temp = []
    if len(notices) :
        temp = [{'id':i.id,'content':i.content,'author':User.query.get(i.user_id).ip_address, 'date':i.date_posted} for i in notices]
    return jsonify({'data':temp}), 200

@app.route("/downvote/<user_ip>", methods=['GET','POST','OPTIONS'])
def downvote(user_ip) :
    print(user_ip)
    user = User.query.filter_by(ip_address=user_ip).first()
    user.downvotes += 1
    db.session.commit()
    return jsonify({'status': 1}), 200
