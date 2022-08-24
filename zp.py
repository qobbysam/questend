from zeep import Client 




# base_url = 'https://qcs-uat.questdiagnostics.com/services/ESPService.asmx?wsdl'
# username = "cli_ArtemisHealthUAT"
# password = "xRq0vUf2pH05"


# client = Client(base_url)




def build_event_info(emails):
    r_frame = '''
        <EventInfo>
        <CollectionSiteID></CollectionSiteID>
        <EmailAuthorizationAddresses>
        {}
        </EmailAuthorizationAddresses>
        <EndDateTime/>
    <!-- <EndDateTimeTimeZoneID/> -->
    </EventInfo>
              '''
    middle_string = '<EmailAddress>{}</EmailAddress>'
    middle = ''

    for email in emails:

        copy = middle_string.format(email)

        middle = middle + copy

    
    return r_frame.format(middle)

def build_unit_codes(unitcodes):

    r_frame = '''
            <UnitCode>{}</UnitCode>
              '''

    code = ''

    for unitcode in unitcodes:

        to_add = r_frame.format(unitcode)
        code = code + to_add

    return code

def build_body(
            
            emails,unitcodes, 
            FirstName, 
            MiddleName, 
            LastName, 
            PrimaryID,
            DOB,
            PrimaryPhone,
            SecondaryPhone,
            ContactName,
            TelephoneNumber,
            LabAccount,
            CSL,
            ClientReferenceID,
            DOTTest,
            TestingAuthority,
            ReasonForTestID,
            ObservedRequested,
            SplitSpecimenRequested,
            # CSONumber,
            # CSOPrompt,
            # CSOText,
            #ResponseUrl
            ):


    event_info = build_event_info(emails=emails)

    unitcodes_ = build_unit_codes(unitcodes=unitcodes)

    order_body = '''

    <Order>

        {}
    
    <DonorInfo>
        <FirstName>{}</FirstName>
        <MiddleName>{}</MiddleName>
        <LastName>{}</LastName>
        <PrimaryID>{}</PrimaryID>
        <DOB>{}</DOB>
        <PrimaryPhone>{}</PrimaryPhone>
        <SecondaryPhone>{}</SecondaryPhone>
    </DonorInfo>
    
    <ClientInfo>
        <ContactName>{}</ContactName>
        <TelephoneNumber>{}</TelephoneNumber>
        <LabAccount>{}</LabAccount>
        <CSL>{}</CSL>
    </ClientInfo>
    
    <TestInfo>
        <ClientReferenceID>{}</ClientReferenceID>
        <DOTTest>{}</DOTTest>
        <TestingAuthority>{}</TestingAuthority>
        <ReasonForTestID>{}</ReasonForTestID>
        <ObservedRequested>{}</ObservedRequested>
        <SplitSpecimenRequested>{}</SplitSpecimenRequested>

        
        <Screenings>
            <UnitCodes>
                    {}
            </UnitCodes>
        </Screenings>
    </TestInfo>
    
    <ClientCustom>
  
    </ClientCustom>
</Order>

'''
    return order_body.format(
        event_info,
        FirstName,
        MiddleName,
        LastName,
        PrimaryID,
        DOB,
        PrimaryPhone,
        SecondaryPhone,
        ContactName,
        TelephoneNumber,
        LabAccount,
        CSL,
        ClientReferenceID,
        DOTTest,
        TestingAuthority,
        ReasonForTestID,
        ObservedRequested,
        SplitSpecimenRequested,
        # CSONumber,
        # CSOPrompt,
        # CSOText,
        unitcodes_,
        #ResponseUrl


    )


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
        <ContactName>XanDER Smith</ContactName >
        <TelephoneNumber>9139139133</TelephoneNumber >
        <LabAccount>12345678</LabAccount>
        <CSL>001</CSL>
    </ClientInfo>
    
    <TestInfo>
        <ClientReferenceID>ORDER#1124</ClientReferenceID>
        <DOTTest>F</DOTTest>
        <TestingAuthority></TestingAuthority> 
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
# print(client.service.CreateOrder(username,password,order_body))