import os
from flask import Flask, render_template, url_for, json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

with open('./animals.json') as test_file:
    json_data = json.load(test_file)

# https://stackoverflow.com/questions/21133976/flask-load-local-json
@app.route("/animals", methods=['GET'])
def get_animals():
    return json.jsonify(json_data)

@app.route("/animals/head/<animal_type>", methods=['GET'])
def get_animals_1(animal_type):
    response = []
    for animal in json_data['animals']:
        if animal['head'] == animal_type.lower():
            response.append(animal)
    return json.jsonify(response)

@app.route("/animals/legs/<count>", methods=['GET'])
def get_animals_2(count):
    try:
        count = int(count)
    except: # default 5
        count = 5

    response = [x for x in json_data['animals'] if x['legs'] == count]
    return json.jsonify(response)

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=5000, debug = True) 
