from unittest import result
from zeep import Client
import datetime

from tinydb import TinyDB, Query
import datetime
import os

from zp import order_body, build_body

wsdl_url = 'https://qcs-uat.questdiagnostics.com/services/ESPService.asmx?wsdl'


username = "cli_ArtemisHealthUAT"
password = "xRq0vUf2pH05"


base_dir = os.getcwd()
dbname =  os.path.join(base_dir , "ser.db")


db = TinyDB(dbname)


client = Client(wsdl_url)

def save_db(tablename, result_ , client_id):
    table = db.table(tablename)

    to_save = {
                "client_id": client_id,
                "result" : result_,
                "time_added": str(datetime.datetime.now())
            }

    table.insert(to_save)


