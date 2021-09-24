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
data_dict = xmltodict.parse(data)

data_in_json=json.dumps(data_dict, indent=1)

print(data_in_json)


from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

data = readfromstring(
    str(data_in_json)
)
print(json2xml.Json2xml(data, item_wrap=False).to_xml())