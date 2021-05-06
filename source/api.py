import json
import random
import uuid, datetime
from flask import Flask, request
import jobs

app = Flask(__name__)

def get_data():
    with open("/app/pet_data.json", "r") as json_file:
        data_json = json.load(json_file)
    return data_json

test = get_data()
jsonList = test['data']


@app.route('/pets', methods=['GET'])
def get_all():
    return json.dumps(jsonList)

@app.route('/pets/dogs', methods=['GET']) #prints all of the dogs
def dogs():
    pet_dog = [x for x in jsonList if x[13] == dog]
    return json.dumps(pet_dog)

@app.route('/pets/cats', methods=['GET']) #prints all of the cats
def dogs():
    pet_cat = [x for x in jsonList if x[13] == cat]
    return json.dumps(pet_cat)

@app.route('/pets/breed', methods=['GET']) #prints all of the types of breeds
def breed():
    for x in jsonList:
        breeds = x[14]
    breed = list(breeds)
    return json.dumps(breed)

@app.route('/pets/color', methods=['GET']) #user requested color, prints all pets with that color
def color():
    c_type = request.args.get('requested_color')
    c = [x for x in jsonList if x[15] == c_type]
    return json.dumps(c)

@app.route('/pets/find', methods=['GET']) #find pet based off of being a cat or dog, and its age
def find():
    typ = request.args.get('pet_type')
    age = request.args.get('pet_age')
    look = [x for x in jsonList if (x[13] == typ and x[17] == age]
    return json.dumps(look)

@app.route('/pets/date', methods=['GET']) #find pet based off of date
def date():
    start = request.args.get('start_time')
    sdate = datetime.datetime.strptime(start, "%Y-%m-%d_%H:%M:%S.%f")
    s = datetime.datetime.strptime(x[12], "%Y-%m-%d_%H:%M:%S.%f")
    dates = [x for x in test if s == sdate]
    return json.dumps(dates)

@app.route('/jobs', methods = ['POST'])
def jobs_api():
    try:
    job = request.get_json(force=True)
    except Exception as e:
    return True, json.dumps({'status': "Error", 'message': "Invalid JSON: {}. ".format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
