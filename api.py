# -*- coding: UTF-8 -*-
import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
app.after_request(after_request)

# City Data 1
city1 = {
    "citylist": [
        {
            "city_name": "台北", 
            "country_name": "Taiwan", 
            "id": 0
        }, 
        {
            "city_name": "New York", 
            "country_name": "United States", 
            "id": 1
        }, 
        {
            "city_name": "London", 
            "country_name": "United Kingdom", 
            "id": 2
        }
    ]
}

# City Data 2
city2 = [
    {
        "id": 0,
        "city_name": "Taipei", 
        "country_name": "台灣", 
    },
    {
        "id": 1,
        "city_name": "New York", 
        "country_name": "United States", 
    },
    {
        "id": 2,
        "city_name": "London", 
        "country_name": "United Kingdom", 
    }
]

# 首頁
@app.route("/", methods=['GET'])
def home():
    return "<h1>Hello Quien!</h1>"

# 顯示 City List 1
@app.route("/citylist1", methods=['GET'])
def citylist1():
    return jsonify(city1)

# 顯示 City List 2
@app.route("/citylist2", methods=['GET'])
def citylist2():
    return jsonify(city2)

# 單獨取得 Case List 2 其中一個項目
# 例如：http://127.0.0.1:5000/citylist2/item?city_name=Taipei
@app.route('/citylist2/item', methods=['GET'])
def city2_name():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
    else:
        return "Error: No city_name provided. Please specify a city_name."
    results = []

    for city in city2:
        if city['city_name'] == city_name:
            results.append(city)

    return jsonify(results)

app.run()