from app import db, admin
from flask_admin.contrib.sqla import ModelView


class course_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(7), unique=True, nullable=False)
    course_name = db.Column(db.String(50), unique=False, nullable=False)
    keywords = db.Column(db.String(), nullable=False)
    professor = db.Column(db.String())
    credits = db.Column(db.Integer())
    department = db.Column(db.String())

    __searchable__ = ["professor","keywords","course_id","course_name","department"]

    def __repr__(self):
        return (("course_data('{}','{}','{}','{}',{}, {}, {})").format(self.id, self.course_id, self.course_name, self.credits, self.department, self.professor, self.keywords))


admin.add_view(ModelView(course_data, db.session))
