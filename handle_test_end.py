from unittest import result
from zeep import Client
import datetime

from tinydb import TinyDB, Query
import datetime
import os
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
                "time_added": datetime.datetime.now()
            }

    table.insert(to_save)


def handletestend(xmlmsg, client_id ,type_send):

    if type_send == 'createorder':

        result_ = client.service.CreateOrder(username,password, xmlmsg["orderXml"])
        
        save_db("createresult",result_, client_id )

        return True

    elif type_send == 'cancelorder':
        result_ = client.service.CancelOrder(
                    username, 
                    
                    password, 
        
                    xmlmsg["referenceTestId"],
                    xmlmsg["questOrderId"]

                    )
        save_db("cancelresult",result_, client_id )
        return True

    elif type_send == 'getdocument':
        result_ = client.service.GetDocument(username,password, xmlmsg['docxml'])

        save_db("getdocument",result_, client_id )
        return True

    elif type_send == 'getorderdetails':

        result_ = client.service.GetOrderDetails(
                    username, 
                    
                    password, 
        
                    xmlmsg["referenceTestId"],
                    xmlmsg["questOrderId"]
        )
        save_db("getorderdetails",result_, client_id )

        return True
    
    elif type_send == 'processdynamicsubmission':

        result_ = client.service.ProcessDynamicSubmission(xmlmsg['orderXml'])
        save_db("processdynamicsubmission",result_, client_id )

        return True
    
    elif type_send == "UpdateOrder":

        result_ = client.service.UpdateOrder(username, password,
        
        xmlmsg["referenceTestId"],
        xmlmsg["questOrderId"],
        xmlmsg['orderXml'] 
                    )
        save_db("updateorder",result_, client_id )

        return True
    else:
        return False
    

    