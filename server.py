import uuid
from flask import Flask, jsonify, request
import xmltodict

import json


from tinydb import TinyDB, Query
import datetime
import os
base_dir = os.getcwd()

dbname =  os.path.join(base_dir , "ser.db")
db = TinyDB(dbname)
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"





@app.route("/results/", methods=['GET', 'POST'])
def handleresults():
    #xml_data = request.form['SomeKey']
    xml_data = '''<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <CreateOrderResponse xmlns="http://wssim.labone.com/">
      <CreateOrderResult>string</CreateOrderResult>
    </CreateOrderResponse>
  </soap12:Body>
</soap12:Envelope>'''
    content_dict = xmltodict.parse(xml_data)
    to_insert = {
    "id":  str(uuid.uuid4()),
    "time": str(datetime.datetime.now()),
    "from": "result",
    "msg" : json.dumps(content_dict)

   }
    # xml_data = request.form['SomeKey']
    # content_dict = xmltodict.parse(xml_data)

    table = db.table("results")
    table.insert(to_insert)

    res = {'status': 200}

    return jsonify(res)

    #return "result handle"



@app.route("/status/",methods=['GET', 'POST'])
def status():
    xml_data = request.form['SomeKey']
    content_dict = xmltodict.parse(xml_data)
    to_insert = {
    "id":  uuid.uuid4(),
    "time": datetime.datetime.now(),
    "from": "status",
    "msg" : jsonify(content_dict)

   }
    # xml_data = request.form['SomeKey']
    # content_dict = xmltodict.parse(xml_data)

    table = db.table("status")
    table.insert(to_insert)

    #db.insert(to_insert)

    res = {'status': 200}

    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
