import json
# x={'payload': {'insurer_code': 'RLGRFR', 'include_proposer': 0, 'dump_id': 94959, 'insurer_logo': 'https://etimg.etb2bimg.com/thumb/msid-77869972,width-1200,resizemode-4/.jpg', 'adults': 2, 'duration_years': 1, 'request_id': 'ef0ee87963a3c3e444d29847e4bb50f1', 'members': [{'medical_history': [], 'dob_to_display': '2000-10-09T18:30:00.000Z', 'nationality': 'Indian', 'dob': '10/10/2000', 'sum_insured': 500000, 'proposer': 1, 'city_name': 'THANE', 'salutation': None, 'state_name': 'MAHARASHTRA', 'marital_status': 'Married', 'nomineeDetails': {}, 'member_type': 'proposer', 'type': 'adult', 'pincode': 401503, 'gender': 'M'}, {'medical_history': [], 'dob_to_display': '1999-06-05T18:30:00.000Z', 'nationality': 'Indian', 'dob': '06/06/1999', 'sum_insured': 500000, 'proposer': 0, 'city_name': 'THANE', 'salutation': None, 'state_name': 'MAHARASHTRA', 'marital_status': 'Married', 'nomineeDetails': {}, 'member_type': 'spouse', 'type': 'adult', 'pincode': 401503, 'gender': 'F'}], 'plan_type': 'INDIVIDUAL', 'unique_identifier': '619cc6af310aa6ed83a4f4acbfefb25c', 'insurance_name': 'religare health freedom', 'kids': 0}, 'request_id': 'ef0ee87963a3c3e444d29847e4bb50f1', 'min_quote': True, 'unique_identifier': '619cc6af310aa6ed83a4f4acbfefb25c'}

# print(json.dumps(x))

quote_payload_with_family={
  "payload": {
    "insurer_code": "RLGRFR",
    "include_proposer": 0,
    "dump_id": 94959,
    "insurer_logo": "https://etimg.etb2bimg.com/thumb/msid-77869972,width-1200,resizemode-4/.jpg",
    "adults": 2,
    "duration_years": 1,
    "request_id": "ef0ee87963a3c3e444d29847e4bb50f1",
    "members": [
      {
        "medical_history": [],
        "dob_to_display": "2000-10-09T18:30:00.000Z",
        "nationality": "Indian",
        "dob": "10/10/2000",
        "sum_insured": 500000,
        "proposer": 1,
        "city_name": "THANE",
        "salutation": None,
        "state_name": "MAHARASHTRA",
        "marital_status": "Married",
        "nomineeDetails": {},
        "member_type": "proposer",
        "type": "adult",
        "pincode": 401503,
        "gender": "M"
      },
      {
        "medical_history": [],
        "dob_to_display": "1999-06-05T18:30:00.000Z",
        "nationality": "Indian",
        "dob": "06/06/1999",
        "sum_insured": 500000,
        "proposer": 0,
        "city_name": "THANE",
        "salutation": None,
        "state_name": "MAHARASHTRA",
        "marital_status": "Married",
        "nomineeDetails": {},
        "member_type": "spouse",
        "type": "adult",
        "pincode": 401503,
        "gender": "F"
      }
    ],
    "plan_type": "INDIVIDUAL",
    "unique_identifier": "619cc6af310aa6ed83a4f4acbfefb25c",
    "insurance_name": "religare health freedom",
    "kids": 0
  },
  "request_id": "ef0ee87963a3c3e444d29847e4bb50f1",
  "min_quote": True,
  "unique_identifier": "619cc6af310aa6ed83a4f4acbfefb25c"
}


quote_payload_self={
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


quote_request={
  "Root": {
    "Uid": 251024242366,
    "VendorCode": "webagg",
    "VendorUserId": "IINSURE",
    "WinNo": "",
    "ApplicationNo": "",
    "PolicyHeader": {
      "PolicyStartDate": "15/10/2021",
      "PolicyEndDate": "14/10/2023",
      "AgentCode": 60001464,
      "BranchCode": 10,
      "MajorClass": "HTO",
      "ContractType": "HTO",
      "METHOD": "ENQ",
      "PolicyIssueType": "I",
      "PolicyNo": "",
      "ClientID": "",
      "ReceiptNo": ""
    },
    "POS_MISP": {
      "Type": "",
      "PanNo": ""
    },
    "Client": {
      "ClientType": "",
      "CreationType": "",
      "Salutation": "",
      "FirstName": "",
      "LastName": "",
      "DOB": "",
      "Gender": "",
      "MaritalStatus": "",
      "Occupation": "",
      "PANNo": "",
      "GSTIN": "",
      "AadharNo": "",
      "CKYCNo": "",
      "EIANo": "",
      "Address1": {
        "AddrLine1": "",
        "AddrLine2": "",
        "AddrLine3": "",
        "Landmark": "",
        "Pincode": 0,
        "City": "",
        "State": "",
        "Country": "",
        "AddressType": "",
        "HomeTelNo": "",
        "OfficeTelNo": "",
        "FAXNO": "",
        "MobileNo": "",
        "EmailAddr": ""
      },
      "Address2": {
        "AddrLine1": "",
        "AddrLine2": "",
        "AddrLine3": "",
        "Landmark": "",
        "Pincode": 0,
        "City": "",
        "State": "",
        "Country": "",
        "AddressType": "",
        "HomeTelNo": "",
        "OfficeTelNo": "",
        "FAXNO": "",
        "MobileNo": "",
        "EmailAddr": ""
      },
      "VIPFlag": "",
      "VIPCategory": ""
    },
    "Receipt": {
      "UniqueTranKey": "",
      "CheckType": "",
      "BSBCode": "",
      "TransactionDate": "",
      "ReceiptType": "IVR",
      "Amount": "",
      "TCSAmount": "",
      "TranRefNo": "",
      "TranRefNoDate": ""
    },
    "Risk": {
      "PolicyType": "HTF",
      "Duration": 1,
      "Installments": "FULL",
      "PaymentType": "IVR",
      "IsFgEmployee": "N",
      "BranchReferenceID": "",
      "FGBankBranchStaffID": "",
      "BankStaffID": "",
      "BankCustomerID": "",
      "BancaChannel": "",
      "PartnerRefNo": "",
      "PayorID": "",
      "PayerName": "",
      "BeneficiaryDetails": {
        "Member": [
          {
            "MemberId": 1,
            "InsuredName": "",
            "InsuredDob": "10/10/2000",
            "InsuredGender": "",
            "InsuredOccpn": "",
            "CoverType": "VITAL",
            "SumInsured": 300000,
            "DeductibleDiscount": "",
            "Relation": "SELF",
            "NomineeName": "",
            "NomineeRelation": "",
            "AnualIncome": "",
            "Height": "",
            "Weight": "",
            "NomineeAge": "",
            "AppointeeName": "",
            "AptRelWithominee": "",
            "MedicalLoading": 0,
            "PreExstDisease": "N",
            "DiseaseMedicalHistoryList": {
              "DiseaseMedicalHistory": {
                "PreExistingDiseaseCode": "",
                "MedicalHistoryDetail": ""
              }
            }
          },
          {
            "MemberId": 2,
            "InsuredName": "",
            "InsuredDob": "06/06/1999",
            "InsuredGender": "",
            "InsuredOccpn": "",
            "CoverType": "VITAL",
            "SumInsured": 300000,
            "DeductibleDiscount": "",
            "Relation": "SPOU",
            "NomineeName": "",
            "NomineeRelation": "",
            "AnualIncome": "",
            "Height": "",
            "Weight": "",
            "NomineeAge": "",
            "AppointeeName": "",
            "AptRelWithominee": "",
            "MedicalLoading": 0,
            "PreExstDisease": "N",
            "DiseaseMedicalHistoryList": {
              "DiseaseMedicalHistory": {
                "PreExistingDiseaseCode": "",
                "MedicalHistoryDetail": ""
              }
            }
          }
        ]
      }
    }
  }
}