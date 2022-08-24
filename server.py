from crypt import methods
import uuid
from flask import Flask, jsonify, request
import xmltodict

import json

from handle_test_end import handletestend
from handle_live_end import handleliveend

from msgs import statusmsg
from tinydb import TinyDB, Query
import datetime
import os

from locapp.shared.shared import pull_near_me

base_dir = os.getcwd()

dbname =  os.path.join(base_dir , "ser.db")
db = TinyDB(dbname)
app = Flask(__name__)

@app.route("/")
def home():

    status_msg = statusmsg()

    return jsonify(status_msg)





# @app.route("/results/", methods=['GET', 'POST'])
# def handleresults():
#     #xml_data = request.form['SomeKey']
#     xml_data = '''<?xml version="1.0" encoding="utf-8"?>
# <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
#   <soap12:Body>
#     <CreateOrderResponse xmlns="http://wssim.labone.com/">
#       <CreateOrderResult>string</CreateOrderResult>
#     </CreateOrderResponse>
#   </soap12:Body>
# </soap12:Envelope>'''
#     content_dict = xmltodict.parse(xml_data)
#     to_insert = {
#     "id":  str(uuid.uuid4()),
#     "time": str(datetime.datetime.now()),
#     "from": "resultsend",
#     "msg" : json.dumps(content_dict)

#    }
#     # xml_data = request.form['SomeKey']
#     # content_dict = xmltodict.parse(xml_data)

#     table = db.table("results")
#     table.insert(to_insert)

#     res = {'status': 200}

#     return jsonify(res)

#     #return "result handle"



# @app.route("/status/",methods=['GET', 'POST'])
# def status():
#     xml_data = request.form['SomeKey']
#     content_dict = xmltodict.parse(xml_data)
#     to_insert = {
#     "id":  uuid.uuid4(),
#     "time": datetime.datetime.now(),
#     "from": "status",
#     "msg" : jsonify(content_dict)

#    }
#     # xml_data = request.form['SomeKey']
#     # content_dict = xmltodict.parse(xml_data)

#     table = db.table("status")
#     table.insert(to_insert)

#     #db.insert(to_insert)

#     res = {'status': 200}

#     return jsonify(res)
from uuid import UUID
def uuid_convert(o):
        if isinstance(o, UUID):
            return o.hex

@app.route('/locations/', methods=['POST'])
def locations():
  jsonD = request.json

  try:

    res = pull_near_me(long=jsonD['long'],lat= jsonD['lat'],miles= int(jsonD['miles']))
    data = {}
    data['data'] = json.dumps([(row.as_dict()) for row in res], default=uuid_convert)
    data['status'] = 200
    
    return jsonify(data)

  except Exception as e:

    print(e)
    data = {}
    data['status'] = 400
    data['message'] = "failed with long and lat given"
    data['data'] = []

    return jsonify(data)


  



@app.route("/getkey/", methods=['GET'])
def handgetkey():
    key_ = request.args.get("key")
    #from_ = request.args.get("from")
    msg = Query()
    #table = db.ta(from_)

    res =  db.search(msg.client_id == key_)

    return jsonify(res)

@app.route("/alldb/", methods=['GET'])
def getall():

    table = request.args.get("table")

    if table is not None:
      msg = Query()
    #table = db.ta(from_)

      res =  db.search(msg.table == table)
      #table_ = db.table(table)
      return jsonify(res)
      
    return jsonify(db.all())

'''xmlmsg data types 
  orderxml
  referenceTestId
  questOrderId

'''

@app.route("/testend/", methods=['GET','POST'])
def handtestend():
  xmlmsg = request.json
  type_ = request.args.get("sendtype")
  client_id = request.args.get("clientid")

  if handletestend(xmlmsg,client_id ,type_):
    res = {'status': 200}

    return jsonify(res)

  else:
    res = {'status': 500}

    return jsonify(res)

@app.route("/liveend/", methods=['GET','POST'])
def handliveend():
  xmlmsg = request.json
  type_ = request.args.get("sendtype")
  client_id = request.args.get("clientid")

  if handleliveend(xmlmsg,client_id ,type_):
    res = {'status': 200}

    return jsonify(res)

  else:
    res = {'status': 500}

    return jsonify(res)


@app.route("/testpull/", methods=['GET','POST'])
def handletestpull():
  xmlmsg = request.json
  

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
