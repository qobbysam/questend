from distutils.log import debug
import uuid
from flask import Flask, jsonify, request
import xmltodict

import json

from handle_test_end import handletestend


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




@app.route("/getkey/", methods=['GET'])
def handgetkey():
    key_ = request.args.get("key")
    from_ = request.args.get("from")
    msg = Query()
    table = db.table(from_)

    res =  table.search(msg.client_id == key_)

    return jsonify(res)

@app.route("/alldb/", methods=['GET'])
def getall():

    table = request.args.get("table")

    if table is not None:
      table_ = db.table(table)
      return jsonify(table_.all())
    return jsonify(db.all())

'''xmlmsg data types 
  orderxml
  referenceTestId
  questOrderId
  
'''

@app.route("/testend/", methods=['GET','POST'])
def handtestend():
  xmlmsg = request.json()
  type_ = request.args.get("sendtype")
  client_id = request.args.get("clientid")

  if handletestend(xmlmsg,client_id ,type_):
    res = {'status': 200}

    return jsonify(res)

  else:
    res = {'status': 500}

    return jsonify(res)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
