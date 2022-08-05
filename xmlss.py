

'''
POST /services/ESPService.asmx HTTP/1.1
Host: qcs-uat.questdiagnostics.com
Content-Type: application/soap+xml; charset=utf-8
Content-Length: length

<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <CreateOrder xmlns="http://wssim.labone.com/">
      <username>string</username>
      <password>string</password>
      <orderXml>string</orderXml>
    </CreateOrder>
  </soap12:Body>
</soap12:Envelope>

'''



'''
HTTP/1.1 200 OK
Content-Type: application/soap+xml; charset=utf-8
Content-Length: length

<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <CreateOrderResponse xmlns="http://wssim.labone.com/">
      <CreateOrderResult>string</CreateOrderResult>
    </CreateOrderResponse>
  </soap12:Body>
</soap12:Envelope>


'''




'''

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