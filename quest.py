

'''
<LabAccount> - <UnitCode>

DOT:

11320933 - 65304N

 

SAP: (NonDOT):

11321237 - 35105N or 35190N

11321338 - 35105N or 35190N

'''


#username , password , or der string

import requests

from requests.structures import CaseInsensitiveDict


create_order_body = '''
                        <?xml version="1.0" encoding="utf-8"?>
                        <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
                            <soap12:Body>
                                <CreateOrder xmlns="http://wssim.labone.com/">
                                <username>{}</username>
                                <password>{}</password>
                                <orderXml>{}</orderXml>
                                </CreateOrder>
                            </soap12:Body>
                        </soap12:Envelope>
                     ''' 

order_xml = '''
<Order>
    <EventInfo>
        <CollectionSiteID></CollectionSiteID>
        <EmailAuthorizationAddresses>
        <EmailAddress>janedoe@gmail.com</EmailAddress>
        </EmailAuthorizationAddresses>
    <EndDateTime/>
    <!-- <EndDateTimeTimeZoneID/> -->
    </EventInfo>
    
    <DonorInfo>
        <FirstName>JANE</FirstName>
        <MiddleName></MiddleName>
        <LastName>DOE</LastName>
        <PrimaryID>KS1111111</PrimaryID>
        <DOB>08/13/1983</DOB>
        <PrimaryPhone>9135551212</PrimaryPhone>
        <SecondaryPhone>9135552222</SecondaryPhone>
    </DonorInfo>
    
    <ClientInfo>
        <ContactName>XanDER Smith</ ContactName >
        <TelephoneNumber>9139139133</ TelephoneNumber >
        <LabAccount>12345678</LabAccount>
        <CSL>001</CSL>
    </ClientInfo>
    
    <TestInfo>
        <ClientReferenceID>ORDER#1124</ClientReferenceID>
        <DOTTest>F</DOTTest>
        <!-- <TestingAuthority></TestingAuthority> -->
        <ReasonForTestID>1</ReasonForTestID>
        <ObservedRequested>N</ObservedRequested>
        <SplitSpecimenRequested>N</SplitSpecimenRequested>
        <CSOs>
        <CSO>
        <CSONumber>17</CSONumber>
        <CSOPrompt>LOCATION</CSOPrompt>
        <CSOText>KANSAS</CSOText>
        </CSO>
        </CSOs> <Screenings>
        <UnitCodes>
        <UnitCode>65105N</UnitCode>
        <UnitCode>11070N</UnitCode>
        </UnitCodes>
        </Screenings>
    </TestInfo>
    
    <ClientCustom>
    <ResponseURL></ResponseURL>
    </ClientCustom>
</Order>

            '''

class Quest:
    username = "cli_ArtemisHealthUAT"
    password = "xRq0vUf2pH05"
    url = "https://qcs-uat.questdiagnostics.com/services/ESPService.asmx"
    token = ""
    headers = CaseInsensitiveDict()

    def __init__(self) -> None:
        pass

    def authourize(self):
        '''build ahourize and build header'''

        self.headers["Content-Type"] = "application/soap+xml"


    def sendrequest(self, action, msg):

        self.authourize()

        if action == 'post':
            resp = requests.post(self.url, headers=self.headers, data=msg)
            print("request sent")
            return resp


        

    def createOrder(self, order):

        result = self.handleResponse(self.sendrequest("post", order))
        print("finish sending order")
        return result



    def getOrderDetails(self):
        pass

    
    def orderStatus(self):
        pass

    def orderResult(self):
        pass
    
    def handleResponse(self, resp):
        pass


    def sendOrder(self):
        order = self.buildOrder()

        result = self.createOrder(order)



        print(result)

        return result
    
    def buildOrder(self):

        order = create_order_body.format(self.username,self.password, order_xml)

        print("finish building order")
        return order