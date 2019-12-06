from flask import Flask, render_template, request, jsonify
import requests,json

app = Flask(__name__)

@app.route("/health")
def health():
    return "Working!"


# @app.route("/hello/<string:name>")
# def hello(name):
#     return render_template('index.html', greeting='Hello', name=name)

@app.route("/", methods=["GET","POST"])
def index():
    # if request.method == 'POST':
    #     v1 = int(request.form['first'])
    #     v2 = int(request.form['second'])
    #     data = {"total": str(v1+v2)}
    #     return jsonify(data), 200
    return render_template('index.html')

# @app.route("/search", methods=["GET","POST"])
# def search():
#         # import ipdb;ipdb.set_trace()
#         house = request.form['house']
#         bill = request.form['billNo']
#         year = request.form['year']
#         author = request.form['author']
#         words = request.form['keywords']
#         mustConditions=[]
#         shouldConditions=[]
#         if house:
#             mustConditions.append(termCondition(name="b_house",value=house))
#         if bill:
#             mustConditions.append(termCondition(name="b_number", value=bill))
#         if year:
#             mustConditions.append(termCondition(name="year", value=year))
#         if author:
#             mustConditions.append(termCondition(name="author", value=author))
#         if words:
#             shouldConditions.append(matchCondition(name="title",value=words,boostValue=2,matchRate="20%"))
#             shouldConditions.append(matchCondition(name="content",value=words,boostValue=1,matchRate="60%"))
#
#         if not shouldConditions:
#             req ={"size":1000,"_source":["b_house","b_number","author","title","year","reference"],"track_scores": True,"sort" : [{ "year" : {"order" : "desc"}},{"b_house" : {"order" : "asc"}},{"author" : {"order" : "asc"}}],"query":{"bool":{"must":mustConditions,"should":shouldConditions}}}
#         else:
#             req ={"size":1000,"_source":["b_house","b_number","author","title","year","reference"],"query":{"bool":{"must":mustConditions,"should":shouldConditions,"minimum_should_match" : 1}}}
#         url = "https://0dce83f29ee74651b94f46cb48efbc48.us-east-1.aws.found.io:9243/chbrp_prod/report/_search"
#         elasticRequest=json.dumps(req)
#         # import ipdb;ipdb.set_trace()
#         resp = requests.get(url, data=elasticRequest,auth=('elastic','SkooIzBygV9000Ea4sUYsrBI'),headers={"Content-Type":"application/json"}).json()
#         return jsonify(resp), 200
    #return render_template('form.html')

def termCondition(name, value):
        return {"term":{name:{"value":value}}}

def matchCondition(name, value, boostValue, matchRate):
        return {"match":{name:{"query":value,"boost":boostValue, "minimum_should_match": matchRate}}}

def parseSearchParams(requestObject):

    return (house,bill,year,author,search)

if __name__ == '__main__':
    app.run(debug=True)
