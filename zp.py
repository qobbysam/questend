from zeep import Client 


client = Client('https://qcs-uat.questdiagnostics.com/services/ESPService.asmx?wsdl')

username = "cli_ArtemisHealthUAT"
password = "xRq0vUf2pH05"
order_body = r'''

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
print(client.service.CreateOrder(username,password,order_body))