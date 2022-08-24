from unittest import result
import uuid
from zeep import Client
import datetime

from tinydb import TinyDB, Query
import datetime
import os

from zp import order_body, build_body

wsdl_url = 'https://qcs-uat.questdiagnostics.com/services/ESPService.asmx?wsdl'

wsdl_url_retrieve = 'https://qcs-uat.questdiagnostics.com/services/esservice.asmx?wsdl'
username = "cli_ArtemisHealthUAT"
password = "xRq0vUf2pH05"


base_dir = os.getcwd()
dbname =  os.path.join(base_dir , "ser_test.db")

consume = os.path.join(base_dir , "location.db")

db = TinyDB(dbname)


client = Client(wsdl_url_retrieve)

def save_db(tablename, result_ , client_id):
    table = db.table(tablename)

    to_save = {
                "client_id": client_id,
                "result" : result_,
                "time_added": str(datetime.datetime.now())
            }

    table.insert(to_save)




def run():
    
    result_ = client.service.FullRetrieveCollectionSiteDetails(username,password)
    client_id = str(uuid.uuid4().hex)
    save_db("createorder",result_, client_id )



def consume_to_db():
    
