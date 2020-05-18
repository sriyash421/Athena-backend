from flask import jsonify, request

from app import app
from app.models.course_data import course_data


@app.route("/recommend", methods=['GET','POST','OPTIONS'])
def recommend():
    if request.method == "POST" :
        tags = request.get_json()['tags']
        response = run_recommend(tags)
        return jsonify({"data":response}), 200
    return "200"

def run_recommend(queries):
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
            "label":course.course_id,
            "value": j
        })
    return sorted(response, reverse=True, key = lambda x : x["value"])
