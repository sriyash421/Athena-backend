from datetime import datetime

from flask_admin.contrib.sqla import ModelView

from app import admin, db


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(7), nullable=False, unique=True)
    notices = db.relationship('Notice', backref='course', lazy=True)
    messages = db.relationship('Message', backref='course', lazy=True)
    def __repr__(self):
        return ("Course {}".format(self.course_id))

class User(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    ip_address = db.Column(db.String(20), unique=True,nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    downvotes = db.Column(db.Integer, nullable=False)
    notices = db.relationship('Notice',backref='author',lazy=True)
    messages = db.relationship('Message',backref='author',lazy=True)
    def __repr__(self) :
        return "User('{}','{}')".format(self.ip_address,self.status)

class Notice(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    def __repr__(self) :
        return "Notice('{}','{}')".format(self.subject,self.content)

class Message(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    def __repr__(self) :
        return "Message('{}','{}')".format(self.subject,self.content)

admin.add_view(ModelView(Course, db.session))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Notice, db.session))
admin.add_view(ModelView(Message, db.session))
