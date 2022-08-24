import json
import os
import datetime

from unittest import result
from zeep import Client

from tinydb import TinyDB, Query
import xmltodict
import sys

from zp import order_body, build_body

wsdl_url = 'https://qcs-uat.questdiagnostics.com/services/ESPService.asmx?wsdl'


username = "cli_ArtemisHealthUAT"
password = "xRq0vUf2pH05"


base_dir = os.getcwd()
dbname =  os.path.join(base_dir , "ser.db")


db = TinyDB(dbname)


client = Client(wsdl_url)


def save_db(tablename, result_ , client_id):

#clean #last updated modifications

    dict_res = xmltodict.parse(result_)
    json_res = json.dumps(dict_res)
    to_save = {
                "table": tablename,
                "client_id": client_id,
                "result" : json_res,
                "updated" : False,
                "time_added": str(datetime.datetime.now())
            }

    db.insert(to_save)




def handletestend(xmlmsg, client_id ,type_send):

    print(xmlmsg, file=sys.stderr)
    
    if type_send == 'createorder':

        result_ = client.service.CreateOrder(username,password, xmlmsg["orderXml"])
        
        save_db("createorder",result_, client_id )

        return True


    elif type_send == 'createorderbuild':

        detail = xmlmsg['orderBody']

        print(detail)
        print(detail, file=sys.stderr)


        body = build_body(
            emails= detail['emails'],
            unitcodes= detail['unitcodes'],
            FirstName= detail['firstName'],
            MiddleName= detail['middleName'],
            LastName= detail['lastName'],
            PrimaryID= detail['primaryID'],
            DOB= detail['dob'],
            PrimaryPhone= detail['primaryPhone'],
            SecondaryPhone= detail['secondaryPhone'],
            ContactName= detail['contactName'],
            TelephoneNumber= detail['telephoneNumber'],
            LabAccount= detail['labAccount'],
            CSL= detail['csl'],
            ClientReferenceID= detail['clientReferenceID'],
            DOTTest= detail['dotTest'],
            TestingAuthority= detail['testingAuthority'],
            ReasonForTestID= detail['reasonForTestID'],
            ObservedRequested= detail['observedRequested'],
            SplitSpecimenRequested= detail['splitSpecimenRequested'],
            # CSONumber= detail['csoNumber'],
            # CSOPrompt= detail['csoPrompt'],
            # CSOText= detail['csoText'],
            #ResponseUrl= detail['responseUrl']
        )

        result_ = client.service.CreateOrder(username,password, body)

        save_db("createorderbuild",result_, client_id )

        return True

    elif type_send == 'cancelorder':
        result_ = client.service.CancelOrder(
                    username, 
                    
                    password, 
        
                    xmlmsg["referenceTestId"],
                    xmlmsg["questOrderId"]

                    )
        save_db("cancelorder",result_, client_id )
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

    elif type_send ==  'processdynamicsubmissionbuild':

        detail = xmlmsg['orderBody']

        body = build_body(
            emails= detail['emails'],
            unitcodes= detail['unitcodes'],
            FirstName= detail['firstName'],
            MiddleName= detail['middleName'],
            LastName= detail['lastName'],
            PrimaryID= detail['primaryID'],
            DOB= detail['dob'],
            PrimaryPhone= detail['primaryPhone'],
            SecondaryPhone= detail['secondaryPhone'],
            ContactName= detail['contactName'],
            TelephoneNumber= detail['telephoneNumber'],
            LabAccount= detail['labAccount'],
            CSL= detail['csl'],
            ClientReferenceID= detail['clientReferenceID'],
            DOTTest= detail['dotTest'],
            TestingAuthority= detail['testingAuthority'],
            ReasonForTestID= detail['reasonForTestID'],
            ObservedRequested= detail['observedRequestedID'],
            SplitSpecimenRequested= detail['splitSpecimenRequested'],
            CSONumber= detail['csoNumber'],
            CSOPrompt= detail['csoPrompt'],
            CSOText= detail['csoText'],
            ResponseUrl= detail['responseUrl']
        )

        result_ = client.service.ProcessDynamicSubmission(body)
        save_db("processdynamicsubmissionbuild",result_, client_id )

        return True
    
    elif type_send == "updateorder":

        result_ = client.service.UpdateOrder(username, password,
        
        xmlmsg["referenceTestId"],
        xmlmsg["questOrderId"],
        xmlmsg['orderXml'] 
                    )
        save_db("updateorder",result_, client_id )

        return True

    elif type_send == "updateorderbuild":

        detail = xmlmsg['orderBody']

        body = build_body(
            emails= detail['emails'],
            unitcodes= detail['unitcodes'],
            FirstName= detail['firstName'],
            MiddleName= detail['middleName'],
            LastName= detail['lastName'],
            PrimaryID= detail['primaryID'],
            DOB= detail['dob'],
            PrimaryPhone= detail['primaryPhone'],
            SecondaryPhone= detail['secondaryPhone'],
            ContactName= detail['contactName'],
            TelephoneNumber= detail['telephoneNumber'],
            LabAccount= detail['labAccount'],
            CSL= detail['csl'],
            ClientReferenceID= detail['clientReferenceID'],
            DOTTest= detail['dotTest'],
            TestingAuthority= detail['testingAuthority'],
            ReasonForTestID= detail['reasonForTestID'],
            ObservedRequested= detail['observedRequestedID'],
            SplitSpecimenRequested= detail['splitSpecimenRequested'],
            CSONumber= detail['csoNumber'],
            CSOPrompt= detail['csoPrompt'],
            CSOText= detail['csoText'],
            ResponseUrl= detail['responseUrl']
        )

        result_ = client.service.UpdateOrder(username, password,
        
        xmlmsg["referenceTestId"],
        xmlmsg["questOrderId"],
        body
                    )
        save_db("updateorderbuild",result_, client_id )

        return True
    elif type_send == "fakesend":
        
        result_ = client.service.CreateOrder(username,password, order_body)

        save_db('fakesend', result_, client_id)
        return True

    else:
        return False
    

    