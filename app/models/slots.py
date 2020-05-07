from app import db, admin
from flask_admin.contrib.sqla import ModelView

class Slots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(8), nullable=False, unique=True)
    slot = db.Column(db.String)

    def __repr__(self):
        print("Slots {} {}".format(self.course_id, self.slots.split("?")))