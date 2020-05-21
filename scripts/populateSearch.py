import json
import random

from app import app, db
from app.models.course_data import course_data


def add_to_index(index, model):
    if not app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    app.elasticsearch.index(index=index, id=model.id, body=payload)

# data = []
# dep_list = None
# with open("scripts/search_data.json", "r") as fin:
#     data = json.load(fin)
# with open("scripts/deps.json", "r") as fin:
#     dep_list = json.load(fin)
# for i in data:
#     i["keywords"]=i["keywords"].replace("\n","")
#     i["keywords"]=i["keywords"].replace("\u00e2","")
#     dep_id = i["course_id"][0:2]
#     dep = None
#     if dep_id not in dep_list.keys() :
#         x = input(dep_id+" write fullform")
#         dep_list[dep_id] =x
#     dep = dep_list[dep_id]
#     cred = random.choice(["2","3","4"])
#     temp = course_data(course_id=i["course_id"], course_name=i["course_name"],
#                        professor=i["professor"], keywords=i["keywords"], department=dep, credits=cred)
#     db.create_all()
#     db.session.add(temp)
#     db.session.commit()
data = course_data.query.all()
for i in data:
    add_to_index("course_info",i)
