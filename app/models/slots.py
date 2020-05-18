from flask_admin.contrib.sqla import ModelView

from app import admin, db


class Slots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(8), nullable=False, unique=True)
    slot = db.Column(db.String)

    def __repr__(self):
        print("Slots {} {}".format(self.course_id, self.slots.split("?")))

admin.add_view(ModelView(Slots, db.session))
