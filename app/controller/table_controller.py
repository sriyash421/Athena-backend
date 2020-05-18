from flask import jsonify, request

from app import app
from app.models.slots import Slots


@app.route("/course_slots", methods=['GET','POST','OPTIONS'])
def slots():
    slots_info = Slots.query.all()
    response = []
    for i in slots_info:
        response.append({
            "key":i.id,
            "value":i.course_id,
            "slots": i.slot.split("?")
        })
    return jsonify({"data":response}), 200
