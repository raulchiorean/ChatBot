#!/usr/bin/env python

import urllib
import json
import os
import pandas

from flask import Flask, jsonify
from flask import request
from flask import make_response

import csv

import pandas
import requests

# Flask app should start in global layout
app = Flask(__name__)


# we could also save every character in a csv file

# with open('employee_file2.txt', mode='w') as txt_file:
#     fieldnames = ['url','name','gender','culture','born','died','titles','aliases','father','mother','spouse','allegiances','books','povBooks','tvSeries','playedBy']
#     writer = csv.DictWriter(txt_file, fieldnames=fieldnames)

list = [{'name': "first", 'index': 0}]
for i in range(1, 16):
    r = requests.get('https://www.anapioficeandfire.com/api/characters/' + str(i))
    r_dic = r.json()

    # writer.writerow(r_dic)
    list.append(r_dic)


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    r = req.get("result")

    # fetch action from json
    action = req.get('queryResult').get('parameters').get('Characters1')

    for i in list:

        s = ""
        if action == i['name']:
            for j in i.items():
                s += str(j)
            return {'fulfillmentText':s}
    # return a fulfillment response
    return {'fulfillmentText': 'Not found'}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
