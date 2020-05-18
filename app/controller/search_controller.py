from flask import jsonify, request

from app import app
from app.models.course_data import course_data


@app.route("/search", methods=['GET','POST','OPTIONS'])
def search():
    if request.method == "POST" :
        tags = request.get_json()['tags']
        response = run_search(tags)
        print(response)
        return jsonify({"results":response}), 200
    return "200"

def run_search(queries):
    results = {}
    for query in queries :
        search = app.elasticsearch.search(
            index="course_info",
            body={'query': {'multi_match': {'query': query, 'fields': ['*']}}})
        ids = [int(hit['_id']) for hit in search['hits']['hits']]
        scores = [float(hit['_score']) for hit in search['hits']['hits']]
        for i,j in zip(ids, scores):
            if i in results.keys():
                results[i]+=j
            else:
                results[i]=j
    response = []
    for i, j in results.items():
        course = course_data.query.get(i)
        response.append({
            "name":course.course_name,
            "id":course.course_id,
            "credits":course.credits,
            "dep":course.department,
            "score": j
        })
    return sorted(response, reverse=True, key = lambda x : x["score"])


@app.route("/search_filters", methods=['GET','POST','OPTIONS'])
def search_filters():
    credits = sorted(list(set([i.credits for i in course_data.query.all()])))
    deps = sorted(list(set([i.department for i in course_data.query.all()])))
    return jsonify({"credits":credits,"deps":deps})


@app.route("/course/<id>", methods=['GET'])
def course(id):
    course = course_data.query.filter_by(course_id=id).first()
    return jsonify({
        "data":{
            "id":course.course_id,
            "name":course.course_name,
            "prof": course.professor,
            "dep": course.department,
            "num_credits":str(course.credits),
            "keys": course.keywords.split(" ")
        }
    }), 200
