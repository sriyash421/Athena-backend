import json
from app.models.slots import Slots
from app import db
slots = []
with open("scripts/slots.json","r") as fin:
    slots = json.load(fin)

for course_id, slot in slots.items():
    temp = Slots(course_id=course_id, slot="?".join(slot))
    db.create_all()
    db.session.add(temp)
    db.session.commit()