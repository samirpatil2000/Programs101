import json
import xmltodict


health_payload={'min_quote': True, 'request_id': 'b96c6d6f34defdb2deb008b2ad1a5cda', 'payload': {'adults': 1, 'unique_identifier': 'a6fe553352ba8509ed7551de498f0097', 'members': [{'pincode': 401503, 'dob_to_display': '2000-10-09T18:30:00.000Z', 'sum_insured': 500000, 'member_type': 'proposer', 'dob': '10/10/2000', 'nomineeDetails': {}, 'city_name': 'THANE', 'state_name': 'MAHARASHTRA', 'medical_history': [], 'nationality': 'Indian', 'proposer': 1, 'gender': 'M', 'type': 'adult'}], 'request_id': 'b96c6d6f34defdb2deb008b2ad1a5cda', 'insurance_name': 'religare health freedom', 'plan_type': 'INDIVIDUAL', 'insurer_code': 'RLGRFR', 'include_proposer': 0, 'insurer_logo': 'https://etimg.etb2bimg.com/thumb/msid-77869972,width-1200,resizemode-4/.jpg', 'kids': 0, 'dump_id': 94247, 'duration_years': 1}, 'unique_identifier': 'a6fe553352ba8509ed7551de498f0097'}


health_payload={
  "min_quote": True,
  "request_id": "b96c6d6f34defdb2deb008b2ad1a5cda",
  "payload": {
    "adults": 1,
    "unique_identifier": "a6fe553352ba8509ed7551de498f0097",
    "members": [
      {
        "pincode": 401503,
        "dob_to_display": "2000-10-09T18:30:00.000Z",
        "sum_insured": 500000,
        "member_type": "proposer",
        "dob": "10/10/2000",
        "nomineeDetails": {},
        "city_name": "THANE",
        "state_name": "MAHARASHTRA",
        "medical_history": [],
        "nationality": "Indian",
        "proposer": 1,
        "gender": "M",
        "type": "adult"
      }
    ],
    "request_id": "b96c6d6f34defdb2deb008b2ad1a5cda",
    "insurance_name": "religare health freedom",
    "plan_type": "INDIVIDUAL",
    "insurer_code": "RLGRFR",
    "include_proposer": 0,
    "insurer_logo": "https://etimg.etb2bimg.com/thumb/msid-77869972,width-1200,resizemode-4/.jpg",
    "kids": 0,
    "dump_id": 94247,
    "duration_years": 1
  },
  "unique_identifier": "a6fe553352ba8509ed7551de498f0097"
}


data="""
<Root>
  <Uid>0447313</Uid>
  <VendorCode>webagg</VendorCode>
  <VendorUserId>webagg</VendorUserId>
  <PolicyHeader>
    <PolicyStartDate></PolicyStartDate>
    <PolicyEndDate></PolicyEndDate>
    <AgentCode></AgentCode>
    <BranchCode>10</BranchCode>
    <MajorClass>HTO</MajorClass>
    <ContractType>HTO</ContractType>
    <METHOD>ENQ</METHOD>
    <PolicyIssueType>I</PolicyIssueType>
    <PolicyNo />
    <ClientID />
    <ReceiptNo />
  </PolicyHeader>
  <POS_MISP>
    	<Type></Type>
	<PanNo>BJGPR3605L</PanNo>
  </POS_MISP>
  <Client>
    <ClientType></ClientType>
    <CreationType></CreationType>
    <Salutation></Salutation>
    <FirstName></FirstName>
    <LastName></LastName>
    <DOB></DOB>
    <Gender></Gender>
    <MaritalStatus></MaritalStatus>
    <Occupation></Occupation>
     <PANNo>BGJPR3605L</PANNo>
     <GSTIN />
     <AadharNo />
     <CKYCNo />
     <EIANo />
    <Address1>
      <AddrLine1 />
      <AddrLine2 />
      <AddrLine3 />
      <Landmark />
      <Pincode>000000</Pincode>
      <City />
      <State />
      <Country></Country>
      <AddressType></AddressType>
      <HomeTelNo />
      <OfficeTelNo />
      <FAXNO />
      <MobileNo />
      <EmailAddr />
    </Address1>
    <Address2>
      <AddrLine1 />
      <AddrLine2 />
      <AddrLine3 />
      <Landmark />
      <Pincode>000000</Pincode>
      <City />
      <State />
      <Country />
      <AddressType />
      <HomeTelNo />
      <OfficeTelNo />
      <FAXNO />
      <MobileNo />
      <EmailAddr />
    </Address2>
  </Client>
  <Receipt>
    <UniqueTranKey />
    <CheckType />
    <BSBCode />
    <TransactionDate />
    <ReceiptType />
    <Amount />
    <TCSAmount />
    <TranRefNo />
    <TranRefNoDate />
  </Receipt>
  <Risk>
    <PolicyType>HTI</PolicyType>
    <Duration>3</Duration>
    <Installments>HALFYEARLY</Installments>
    <IsFgEmployee>N</IsFgEmployee>
    <BeneficiaryDetails>
      <Member>
        <MemberId>1</MemberId>
        <InsuredName />
        <InsuredDob>06/09/1990</InsuredDob>
        <InsuredGender />
        <InsuredOccpn></InsuredOccpn>
        <CoverType>SUPERIOR</CoverType>
        <SumInsured>2000000</SumInsured>
        <DeductibleDiscount>75000</DeductibleDiscount>
        <Relation>SELF</Relation>
        <NomineeName />
        <NomineeRelation></NomineeRelation>
        <MedicalLoading>0</MedicalLoading>
        <PreExstDisease>N</PreExstDisease>
        <DiseaseMedicalHistoryList>
          <DiseaseMedicalHistory>
            <PreExistingDiseaseCode />
            <MedicalHistoryDetail />
          </DiseaseMedicalHistory>
        </DiseaseMedicalHistoryList>
      </Member>
      <Member>
        <MemberId>2</MemberId>
        <InsuredName />
        <InsuredDob>03/09/1991</InsuredDob>
        <InsuredGender />
        <InsuredOccpn></InsuredOccpn>
        <CoverType>VITAL</CoverType>
        <SumInsured>1000000</SumInsured>
        <DeductibleDiscount>0</DeductibleDiscount>
        <Relation>SPOU</Relation>
        <NomineeName />
        <NomineeRelation></NomineeRelation>
        <MedicalLoading>0</MedicalLoading>
        <PreExstDisease>N</PreExstDisease>
        <DiseaseMedicalHistoryList>
          <DiseaseMedicalHistory>
            <PreExistingDiseaseCode />
            <MedicalHistoryDetail />
          </DiseaseMedicalHistory>
        </DiseaseMedicalHistoryList>
      </Member>
    </BeneficiaryDetails>
  </Risk>
</Root>"""

quotation_payload={
   "Uid": "0447313",
   "VendorCode": "webagg",
   "VendorUserId": "webagg",
   "PolicyHeader": {
      "PolicyStartDate": [],
      "PolicyEndDate": [],
      "AgentCode": [],
      "BranchCode": "10",
      "MajorClass": "HTO",
      "ContractType": "HTO",
      "METHOD": "ENQ",
      "PolicyIssueType": "I",
      "PolicyNo": [],
      "ClientID": [],
      "ReceiptNo": []
   },
   "POS_MISP": {
      "Type": [],
      "PanNo": "BJGPR3605L"
   },
   "Client": {
      "ClientType": [],
      "CreationType": [],
      "Salutation": [],
      "FirstName": [],
      "LastName": [],
      "DOB": [],
      "Gender": [],
      "MaritalStatus": [],
      "Occupation": [],
      "PANNo": "BGJPR3605L",
      "GSTIN": [],
      "AadharNo": [],
      "CKYCNo": [],
      "EIANo": [],
      "Address1": {
         "AddrLine1": [],
         "AddrLine2": [],
         "AddrLine3": [],
         "Landmark": [],
         "Pincode": "000000",
         "City": [],
         "State": [],
         "Country": [],
         "AddressType": [],
         "HomeTelNo": [],
         "OfficeTelNo": [],
         "FAXNO": [],
         "MobileNo": [],
         "EmailAddr": []
      },
      "Address2": {
         "AddrLine1": [],
         "AddrLine2": [],
         "AddrLine3": [],
         "Landmark": [],
         "Pincode": "000000",
         "City": [],
         "State": [],
         "Country": [],
         "AddressType": [],
         "HomeTelNo": [],
         "OfficeTelNo": [],
         "FAXNO": [],
         "MobileNo": [],
         "EmailAddr": []
      }
   },
   "Receipt": {
      "UniqueTranKey": [],
      "CheckType": [],
      "BSBCode": [],
      "TransactionDate": [],
      "ReceiptType": [],
      "Amount": [],
      "TCSAmount": [],
      "TranRefNo": [],
      "TranRefNoDate": []
   },
   "Risk": {
      "PolicyType": "HTI",
      "Duration": "3",
      "Installments": "HALFYEARLY",
      "IsFgEmployee": "N",
      "BeneficiaryDetails": [
         {
            "MemberId": "1",
            "InsuredName": [],
            "InsuredDob": "06/09/1990",
            "InsuredGender": [],
            "InsuredOccpn": [],
            "CoverType": "SUPERIOR",
            "SumInsured": "2000000",
            "DeductibleDiscount": "75000",
            "Relation": "SELF",
            "NomineeName": [],
            "NomineeRelation": [],
            "MedicalLoading": "0",
            "PreExstDisease": "N",
            "DiseaseMedicalHistoryList": {
               "DiseaseMedicalHistory": {
                  "PreExistingDiseaseCode": [],
                  "MedicalHistoryDetail": []
               }
            }
         },
         {
            "MemberId": "2",
            "InsuredName": [],
            "InsuredDob": "03/09/1991",
            "InsuredGender": [],
            "InsuredOccpn": [],
            "CoverType": "VITAL",
            "SumInsured": "1000000",
            "DeductibleDiscount": "0",
            "Relation": "SPOU",
            "NomineeName": [],
            "NomineeRelation": [],
            "MedicalLoading": "0",
            "PreExstDisease": "N",
            "DiseaseMedicalHistoryList": {
               "DiseaseMedicalHistory": {
                  "PreExistingDiseaseCode": [],
                  "MedicalHistoryDetail": []
               }
            }
         }
      ]
   }
}
# data_dict = xmltodict.parse(data)


# data_dict={'Root': {'Uid': 251024242366, 'VendorCode': 'webagg', 'VendorUserId': 'IINSURE', 'WinNo': '', 'ApplicationNo': '', 'PolicyHeader': {'PolicyStartDate': '15/10/2021', 'PolicyEndDate': '14/10/2023', 'AgentCode': 60001464, 'BranchCode': 10, 'MajorClass': 'HTO', 'ContractType': 'HTO', 'METHOD': 'ENQ', 'PolicyIssueType': 'I', 'PolicyNo': '', 'ClientID': '', 'ReceiptNo': ''}, 'POS_MISP': {'Type': '', 'PanNo': ''}, 'Client': {'ClientType': '', 'CreationType': '', 'Salutation': '', 'FirstName': '', 'LastName': '', 'DOB': '', 'Gender': '', 'MaritalStatus': '', 'Occupation': '', 'PANNo': '', 'GSTIN': '', 'AadharNo': '', 'CKYCNo': '', 'EIANo': '', 'Address1': {'AddrLine1': '', 'AddrLine2': '', 'AddrLine3': '', 'Landmark': '', 'Pincode': 0, 'City': '', 'State': '', 'Country': '', 'AddressType': '', 'HomeTelNo': '', 'OfficeTelNo': '', 'FAXNO': '', 'MobileNo': '', 'EmailAddr': ''}, 'Address2': {'AddrLine1': '', 'AddrLine2': '', 'AddrLine3': '', 'Landmark': '', 'Pincode': 0, 'City': '', 'State': '', 'Country': '', 'AddressType': '', 'HomeTelNo': '', 'OfficeTelNo': '', 'FAXNO': '', 'MobileNo': '', 'EmailAddr': ''}, 'VIPFlag': '', 'VIPCategory': ''}, 'Receipt': {'UniqueTranKey': '', 'CheckType': '', 'BSBCode': '', 'TransactionDate': '', 'ReceiptType': 'IVR', 'Amount': '', 'TCSAmount': '', 'TranRefNo': '', 'TranRefNoDate': ''}, 'Risk': {'PolicyType': 'HTF', 'Duration': 1, 'Installments': 'FULL', 'PaymentType': 'IVR', 'IsFgEmployee': 'N', 'BranchReferenceID': '', 'FGBankBranchStaffID': '', 'BankStaffID': '', 'BankCustomerID': '', 'BancaChannel': '', 'PartnerRefNo': '', 'PayorID': '', 'PayerName': '', 'BeneficiaryDetails': {'Member': [{'MemberId': 1, 'InsuredName': '', 'InsuredDob': '10/10/2000', 'InsuredGender': 'M', 'InsuredOccpn': '', 'CoverType': 'VITAL', 'SumInsured': 500000, 'DeductibleDiscount': '', 'Relation': 'SELF', 'NomineeName': '', 'NomineeRelation': '', 'AnualIncome': '', 'Height': '', 'Weight': '', 'NomineeAge': '', 'AppointeeName': '', 'AptRelWithominee': '', 'MedicalLoading': 0, 'PreExstDisease': 'N', 'DiseaseMedicalHistoryList': {'DiseaseMedicalHistory': {'PreExistingDiseaseCode': '', 'MedicalHistoryDetail': ''}}}, {'MemberId': 2, 'InsuredName': '', 'InsuredDob': '06/06/1999', 'InsuredGender': 'F', 'InsuredOccpn': '', 'CoverType': 'VITAL', 'SumInsured': 500000, 'DeductibleDiscount': '', 'Relation': 'SPOU', 'NomineeName': '', 'NomineeRelation': '', 'AnualIncome': '', 'Height': '', 'Weight': '', 'NomineeAge': '', 'AppointeeName': '', 'AptRelWithominee': '', 'MedicalLoading': 0, 'PreExstDisease': 'N', 'DiseaseMedicalHistoryList': {'DiseaseMedicalHistory': {'PreExistingDiseaseCode': '', 'MedicalHistoryDetail': ''}}}]}}}}
# data_in_json=json.dumps(data_dict, indent=1)

# print(data_in_json)


from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

# quotation_payload=json.dumps(quotation_payload)

# data = readfromstring(
#     str(quotation_payload)
# )
# print(json2xml.Json2xml(data, item_wrap=False,attr_type=False).to_xml())
tree="""
<all>
        <Root type="dict">
                <Uid type="int">251024242366</Uid>
                <VendorCode type="str">webagg</VendorCode>
                <VendorUserId type="str">IINSURE</VendorUserId>
                <WinNo type="str"/>
                <ApplicationNo type="str"/>
                <PolicyHeader type="dict">
                        <PolicyStartDate type="str">15/10/2021</PolicyStartDate>
                        <PolicyEndDate type="str">14/10/2023</PolicyEndDate>
                        <AgentCode type="int">60001464</AgentCode>
                        <BranchCode type="int">10</BranchCode>
                        <MajorClass type="str">HTO</MajorClass>
                        <ContractType type="str">HTO</ContractType>
                        <METHOD type="str">ENQ</METHOD>
                        <PolicyIssueType type="str">I</PolicyIssueType>
                        <PolicyNo type="str"/>
                        <ClientID type="str"/>
                        <ReceiptNo type="str"/>
                </PolicyHeader>
                <POS_MISP type="dict">
                        <Type type="str"/>
                        <PanNo type="str"/>
                </POS_MISP>
                <Client type="dict">
                        <ClientType type="str"/>
                        <CreationType type="str"/>
                        <Salutation type="str"/>
                        <FirstName type="str"/>
                        <LastName type="str"/>
                        <DOB type="str"/>
                        <Gender type="str"/>
                        <MaritalStatus type="str"/>
                        <Occupation type="str"/>
                        <PANNo type="str"/>
                        <GSTIN type="str"/>
                        <AadharNo type="str"/>
                        <CKYCNo type="str"/>
                        <EIANo type="str"/>
                        <Address1 type="dict">
                                <AddrLine1 type="str"/>
                                <AddrLine2 type="str"/>
                                <AddrLine3 type="str"/>
                                <Landmark type="str"/>
                                <Pincode type="int">0</Pincode>
                                <City type="str"/>
                                <State type="str"/>
                                <Country type="str"/>
                                <AddressType type="str"/>
                                <HomeTelNo type="str"/>
                                <OfficeTelNo type="str"/>
                                <FAXNO type="str"/>
                                <MobileNo type="str"/>
                                <EmailAddr type="str"/>
                        </Address1>
                        <Address2 type="dict">
                                <AddrLine1 type="str"/>
                                <AddrLine2 type="str"/>
                                <AddrLine3 type="str"/>
                                <Landmark type="str"/>
                                <Pincode type="int">0</Pincode>
                                <City type="str"/>
                                <State type="str"/>
                                <Country type="str"/>
                                <AddressType type="str"/>
                                <HomeTelNo type="str"/>
                                <OfficeTelNo type="str"/>
                                <FAXNO type="str"/>
                                <MobileNo type="str"/>
                                <EmailAddr type="str"/>
                        </Address2>
                        <VIPFlag type="str"/>
                        <VIPCategory type="str"/>
                </Client>
                <Receipt type="dict">
                        <UniqueTranKey type="str"/>
                        <CheckType type="str"/>
                        <BSBCode type="str"/>
                        <TransactionDate type="str"/>
                        <ReceiptType type="str">IVR</ReceiptType>
                        <Amount type="str"/>
                        <TCSAmount type="str"/>
                        <TranRefNo type="str"/>
                        <TranRefNoDate type="str"/>
                </Receipt>
                <Risk type="dict">
                        <PolicyType type="str">HTF</PolicyType>
                        <Duration type="int">1</Duration>
                        <Installments type="str">FULL</Installments>
                        <PaymentType type="str">IVR</PaymentType>
                        <IsFgEmployee type="str">N</IsFgEmployee>
                        <BranchReferenceID type="str"/>
                        <FGBankBranchStaffID type="str"/>
                        <BankStaffID type="str"/>
                        <BankCustomerID type="str"/>
                        <BancaChannel type="str"/>
                        <PartnerRefNo type="str"/>
                        <PayorID type="str"/>
                        <PayerName type="str"/>
                        <BeneficiaryDetails type="dict">
                                <Member type="list">
                                        <MemberId type="int">1</MemberId>
                                        <InsuredName type="str"/>
                                        <InsuredDob type="str">10/10/2000</InsuredDob>
                                        <InsuredGender type="str">M</InsuredGender>
                                        <InsuredOccpn type="str"/>
                                        <CoverType type="str">VITAL</CoverType>
                                        <SumInsured type="int">500000</SumInsured>
                                        <DeductibleDiscount type="str"/>
                                        <Relation type="str">SELF</Relation>
                                        <NomineeName type="str"/>
                                        <NomineeRelation type="str"/>
                                        <AnualIncome type="str"/>
                                        <Height type="str"/>
                                        <Weight type="str"/>
                                        <NomineeAge type="str"/>
                                        <AppointeeName type="str"/>
                                        <AptRelWithominee type="str"/>
                                        <MedicalLoading type="int">0</MedicalLoading>
                                        <PreExstDisease type="str">N</PreExstDisease>
                                        <DiseaseMedicalHistoryList type="dict">
                                                <DiseaseMedicalHistory type="dict">
                                                        <PreExistingDiseaseCode type="str"/>
                                                        <MedicalHistoryDetail type="str"/>
                                                </DiseaseMedicalHistory>
                                        </DiseaseMedicalHistoryList>
                                        <MemberId type="int">2</MemberId>
                                        <InsuredName type="str"/>
                                        <InsuredDob type="str">06/06/1999</InsuredDob>
                                        <InsuredGender type="str">F</InsuredGender>
                                        <InsuredOccpn type="str"/>
                                        <CoverType type="str">VITAL</CoverType>
                                        <SumInsured type="int">500000</SumInsured>
                                        <DeductibleDiscount type="str"/>
                                        <Relation type="str">SPOU</Relation>
                                        <NomineeName type="str"/>
                                        <NomineeRelation type="str"/>
                                        <AnualIncome type="str"/>
                                        <Height type="str"/>
                                        <Weight type="str"/>
                                        <NomineeAge type="str"/>
                                        <AppointeeName type="str"/>
                                        <AptRelWithominee type="str"/>
                                        <MedicalLoading type="int">0</MedicalLoading>
                                        <PreExstDisease type="str">N</PreExstDisease>
                                        <DiseaseMedicalHistoryList type="dict">
                                                <DiseaseMedicalHistory type="dict">
                                                        <PreExistingDiseaseCode type="str"/>
                                                        <MedicalHistoryDetail type="str"/>
                                                </DiseaseMedicalHistory>
                                        </DiseaseMedicalHistoryList>
                                </Member>
                        </BeneficiaryDetails>
                </Risk>
        </Root>
</all>"""
# import xml.etree.ElementTree as ET


from dicttoxml import dicttoxml
xml = dicttoxml(quotation_payload,attr_type=False)
print(xml)