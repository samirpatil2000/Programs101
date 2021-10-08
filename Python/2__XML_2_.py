

import json
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

import xml.etree.ElementTree as ET


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

quotation_payload=json.dumps(quotation_payload)

data = readfromstring(
    str(quotation_payload)
)
xmlstr=json2xml.Json2xml(data, item_wrap=False).to_xml()


# root = ET.fromstring(xmlstr)

# targets = root.find('all')
# root.remove(targets)
# print(ET.tostring(root))

# print(str(xmlstr).replace('all','Root'))


import requests

url = "http://fglpg001.futuregenerali.in/BO/Service.svc"


tree="""
<Root>
		<Uid>251024242366</Uid>
		<VendorCode>webagg</VendorCode>
		<VendorUserId>IINSURE</VendorUserId>
		<WinNo></WinNo>
		<ApplicationNo></ApplicationNo>
		<PolicyHeader>
			<PolicyStartDate>16/10/2021</PolicyStartDate>
			<PolicyEndDate>15/10/2023</PolicyEndDate>
			<AgentCode>60001464</AgentCode>
			<BranchCode>10</BranchCode>
			<MajorClass>HTO</MajorClass>
			<ContractType>HTO</ContractType>
			<METHOD>ENQ</METHOD>
			<PolicyIssueType>I</PolicyIssueType>
			<PolicyNo></PolicyNo>
			<ClientID></ClientID>
			<ReceiptNo></ReceiptNo>
		</PolicyHeader>
		<POS_MISP>
			<Type></Type>
			<PanNo></PanNo>
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
			<PANNo></PANNo>
			<GSTIN></GSTIN>
			<AadharNo></AadharNo>
			<CKYCNo></CKYCNo>
			<EIANo></EIANo>
			<Address1>
				<AddrLine1></AddrLine1>
				<AddrLine2></AddrLine2>
				<AddrLine3></AddrLine3>
				<Landmark></Landmark>
				<Pincode>000000</Pincode>
				<City></City>
				<State></State>
				<Country></Country>
				<AddressType></AddressType>
				<HomeTelNo></HomeTelNo>
				<OfficeTelNo></OfficeTelNo>
				<FAXNO></FAXNO>
				<MobileNo></MobileNo>
				<EmailAddr></EmailAddr>
			</Address1>
			<Address2>
				<AddrLine1></AddrLine1>
				<AddrLine2></AddrLine2>
				<AddrLine3></AddrLine3>
				<Landmark></Landmark>
				<Pincode>000000</Pincode>
				<City></City>
				<State></State>
				<Country></Country>
				<AddressType></AddressType>
				<HomeTelNo></HomeTelNo>
				<OfficeTelNo></OfficeTelNo>
				<FAXNO></FAXNO>
				<MobileNo></MobileNo>
				<EmailAddr></EmailAddr>
			</Address2>
			<VIPFlag></VIPFlag>
			<VIPCategory></VIPCategory>
		</Client>
		<Receipt>
			<UniqueTranKey></UniqueTranKey>
			<CheckType></CheckType>
			<BSBCode></BSBCode>
			<TransactionDate></TransactionDate>
			<ReceiptType>IVR</ReceiptType>
			<Amount></Amount>
			<TCSAmount></TCSAmount>
			<TranRefNo></TranRefNo>
			<TranRefNoDate></TranRefNoDate>
		</Receipt>
		<Risk>
			<PolicyType>HTF</PolicyType>
			<Duration>1</Duration>
			<Installments>FULL</Installments>
			<PaymentType>IVR</PaymentType>
			<IsFgEmployee>N</IsFgEmployee>
			<BranchReferenceID></BranchReferenceID>
			<FGBankBranchStaffID></FGBankBranchStaffID>
			<BankStaffID></BankStaffID>
			<BankCustomerID></BankCustomerID>
			<BancaChannel></BancaChannel>
			<PartnerRefNo></PartnerRefNo>
			<PayorID></PayorID>
			<PayerName></PayerName>
			<BeneficiaryDetails>
				<Member>
					<MemberId>1</MemberId>
					<InsuredName></InsuredName>
					<InsuredDob>10/10/2000</InsuredDob>
					<InsuredGender>M</InsuredGender>
					<InsuredOccpn></InsuredOccpn>
					<CoverType>VITAL</CoverType>
					<SumInsured>500000</SumInsured>
					<DeductibleDiscount></DeductibleDiscount>
					<Relation>SELF</Relation>
					<NomineeName></NomineeName>
					<NomineeRelation></NomineeRelation>
					<AnualIncome></AnualIncome>
					<Height></Height>
					<Weight></Weight>
					<NomineeAge></NomineeAge>
					<AppointeeName></AppointeeName>
					<AptRelWithominee></AptRelWithominee>
					<MedicalLoading>0</MedicalLoading>
					<PreExstDisease>N</PreExstDisease>
					<DiseaseMedicalHistoryList>
						<DiseaseMedicalHistory>
							<PreExistingDiseaseCode></PreExistingDiseaseCode>
							<MedicalHistoryDetail></MedicalHistoryDetail>
						</DiseaseMedicalHistory>
					</DiseaseMedicalHistoryList>
				</Member>
				<Member>
					<MemberId>2</MemberId>
					<InsuredName></InsuredName>
					<InsuredDob>06/06/1999</InsuredDob>
					<InsuredGender>F</InsuredGender>
					<InsuredOccpn></InsuredOccpn>
					<CoverType>VITAL</CoverType>
					<SumInsured>500000</SumInsured>
					<DeductibleDiscount></DeductibleDiscount>
					<Relation>SPOU</Relation>
					<NomineeName></NomineeName>
					<NomineeRelation></NomineeRelation>
					<AnualIncome></AnualIncome>
					<Height></Height>
					<Weight></Weight>
					<NomineeAge></NomineeAge>
					<AppointeeName></AppointeeName>
					<AptRelWithominee></AptRelWithominee>
					<MedicalLoading>0</MedicalLoading>
					<PreExstDisease>N</PreExstDisease>
					<DiseaseMedicalHistoryList>
						<DiseaseMedicalHistory>
							<PreExistingDiseaseCode></PreExistingDiseaseCode>
							<MedicalHistoryDetail></MedicalHistoryDetail>
						</DiseaseMedicalHistory>
					</DiseaseMedicalHistoryList>
				</Member>
			</BeneficiaryDetails>
		</Risk>
	</Root>"""
# data="<Root>\n\t<Uid>251024242366</Uid>\n\t<VendorCode>webagg</VendorCode>\n\t<VendorUserId>IINSURE</VendorUserId>\n\t<WinNo />\n\t<ApplicationNo />\n\t<PolicyHeader>\n\t\t<PolicyStartDate>15/10/2021</PolicyStartDate>\n\t\t<PolicyEndDate>14/10/2023</PolicyEndDate>\n\t\t<AgentCode>60001464</AgentCode>\n\t\t<BranchCode>10</BranchCode>\n\t\t<MajorClass>HTO</MajorClass>\n\t\t<ContractType>HTO</ContractType>\n\t\t<METHOD>ENQ</METHOD>\n\t\t<PolicyIssueType>I</PolicyIssueType>\n\t\t<PolicyNo />\n\t\t<ClientID></ClientID>\n\t\t<ReceiptNo />\n\t</PolicyHeader>\n\t<POS_MISP>\n\t\t<Type />\n\t\t<PanNo />\n\t</POS_MISP>\n\t<Client>\n\t\t<ClientType></ClientType>\n\t\t<CreationType></CreationType>\n\t\t<Salutation></Salutation>\n\t\t<FirstName></FirstName>\n\t\t<LastName></LastName>\n\t\t<DOB></DOB>\n\t\t<Gender></Gender>\n\t\t<MaritalStatus></MaritalStatus>\n\t\t<Occupation></Occupation>\n\t\t<PANNo />\n\t\t<GSTIN />\n\t\t<AadharNo />\n\t\t<CKYCNo />\n\t\t<EIANo />\n\t\t<Address1>\n\t\t\t<AddrLine1></AddrLine1>\n\t\t\t<AddrLine2 />\n\t\t\t<AddrLine3 />\n\t\t\t<Landmark />\n\t\t\t<Pincode>000000</Pincode>\n\t\t\t<City></City>\n\t\t\t<State></State>\n\t\t\t<Country></Country>\n\t\t\t<AddressType></AddressType>\n\t\t\t<HomeTelNo />\n\t\t\t<OfficeTelNo />\n\t\t\t<FAXNO />\n\t\t\t<MobileNo></MobileNo>\n\t\t\t<EmailAddr></EmailAddr>\n\t\t</Address1>\n\t\t<Address2>\n\t\t\t<AddrLine1 />\n\t\t\t<AddrLine2 />\n\t\t\t<AddrLine3 />\n\t\t\t<Landmark />\n\t\t\t<Pincode>000000</Pincode>\n\t\t\t<City></City>\n\t\t\t<State></State>\n\t\t\t<Country></Country>\n\t\t\t<AddressType></AddressType>\n\t\t\t<HomeTelNo />\n\t\t\t<OfficeTelNo />\n\t\t\t<FAXNO />\n\t\t\t<MobileNo></MobileNo>\n\t\t\t<EmailAddr></EmailAddr>\n\t\t</Address2>\n\t\t<VIPFlag></VIPFlag>\n\t\t<VIPCategory />\n\t</Client>\n\t<Receipt>\n\t\t<UniqueTranKey></UniqueTranKey>\n\t\t<CheckType />\n\t\t<BSBCode />\n\t\t<TransactionDate></TransactionDate>\n\t\t<ReceiptType>IVR</ReceiptType>\n\t\t<Amount></Amount>\n\t\t<TCSAmount />\n\t\t<TranRefNo></TranRefNo>\n\t\t<TranRefNoDate></TranRefNoDate>\n\t</Receipt>\n\t<Risk>\n\t\t<PolicyType>HTI</PolicyType>\n\t\t<Duration>1</Duration>\n\t\t<Installments>FULL</Installments>\n\t\t<PaymentType>IVR</PaymentType>\n\t\t<IsFgEmployee>N</IsFgEmployee>\n\t\t<BranchReferenceID />\n\t\t<FGBankBranchStaffID />\n\t\t<BankStaffID />\n\t\t<BankCustomerID />\n\t\t<BancaChannel />\n\t\t<PartnerRefNo />\n\t\t<PayorID />\n\t\t<PayerName />\n\t\t<BeneficiaryDetails>\n\t\t\t<Member>\n\t\t\t\t<MemberId>1</MemberId>\n\t\t\t\t<InsuredName></InsuredName>\n\t\t\t\t<InsuredDob>10/10/2000</InsuredDob>\n\t\t\t\t<InsuredGender></InsuredGender>\n\t\t\t\t<InsuredOccpn></InsuredOccpn>\n\t\t\t\t<CoverType>VITAL</CoverType>\n\t\t\t\t<SumInsured>300000</SumInsured>\n\t\t\t\t<DeductibleDiscount></DeductibleDiscount>\n\t\t\t\t<Relation>SELF</Relation>\n\t\t\t\t<NomineeName></NomineeName>\n\t\t\t\t<NomineeRelation></NomineeRelation>\n\t\t\t\t<AnualIncome />\n\t\t\t\t<Height></Height>\n\t\t\t\t<Weight></Weight>\n\t\t\t\t<NomineeAge></NomineeAge>\n\t\t\t\t<AppointeeName />\n\t\t\t\t<AptRelWithominee />\n\t\t\t\t<MedicalLoading>0</MedicalLoading>\n\t\t\t\t<PreExstDisease>N</PreExstDisease>\n\t\t\t\t<DiseaseMedicalHistoryList>\n\t\t\t\t\t<DiseaseMedicalHistory>\n\t\t\t\t\t\t<PreExistingDiseaseCode />\n\t\t\t\t\t\t<MedicalHistoryDetail />\n\t\t\t\t\t</DiseaseMedicalHistory>\n\t\t\t\t</DiseaseMedicalHistoryList>\n\t\t\t</Member>\n\t\t</BeneficiaryDetails>\n\t</Risk>\n</Root>"
# payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:tem=\"http://tempuri.org/\">\n    <soapenv:Header/>\n    <soapenv:Body>\n        <tem:CreatePolicy>\n            <tem:Product>HealthTotal</tem:Product>\n            <tem:XML>\n                <![CDATA["+ tree +"]]>\n</tem:XML>\n</tem:CreatePolicy>\n</soapenv:Body>\n</soapenv:Envelope>"
# payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:tem=\"http://tempuri.org/\">\n    <soapenv:Header/>\n    <soapenv:Body>\n        <tem:CreatePolicy>\n            <tem:Product>HealthTotal</tem:Product>\n            <tem:XML>\n                <![CDATA[<Root>\n\t<Uid>251024242366</Uid>\n\t<VendorCode>webagg</VendorCode>\n\t<VendorUserId>IINSURE</VendorUserId>\n\t<WinNo />\n\t<ApplicationNo />\n\t<PolicyHeader>\n\t\t<PolicyStartDate>15/10/2021</PolicyStartDate>\n\t\t<PolicyEndDate>14/10/2023</PolicyEndDate>\n\t\t<AgentCode>60001464</AgentCode>\n\t\t<BranchCode>10</BranchCode>\n\t\t<MajorClass>HTO</MajorClass>\n\t\t<ContractType>HTO</ContractType>\n\t\t<METHOD>ENQ</METHOD>\n\t\t<PolicyIssueType>I</PolicyIssueType>\n\t\t<PolicyNo />\n\t\t<ClientID></ClientID>\n\t\t<ReceiptNo />\n\t</PolicyHeader>\n\t<POS_MISP>\n\t\t<Type />\n\t\t<PanNo />\n\t</POS_MISP>\n\t<Client>\n\t\t<ClientType></ClientType>\n\t\t<CreationType></CreationType>\n\t\t<Salutation></Salutation>\n\t\t<FirstName></FirstName>\n\t\t<LastName></LastName>\n\t\t<DOB></DOB>\n\t\t<Gender></Gender>\n\t\t<MaritalStatus></MaritalStatus>\n\t\t<Occupation></Occupation>\n\t\t<PANNo />\n\t\t<GSTIN />\n\t\t<AadharNo />\n\t\t<CKYCNo />\n\t\t<EIANo />\n\t\t<Address1>\n\t\t\t<AddrLine1></AddrLine1>\n\t\t\t<AddrLine2 />\n\t\t\t<AddrLine3 />\n\t\t\t<Landmark />\n\t\t\t<Pincode>000000</Pincode>\n\t\t\t<City></City>\n\t\t\t<State></State>\n\t\t\t<Country></Country>\n\t\t\t<AddressType></AddressType>\n\t\t\t<HomeTelNo />\n\t\t\t<OfficeTelNo />\n\t\t\t<FAXNO />\n\t\t\t<MobileNo></MobileNo>\n\t\t\t<EmailAddr></EmailAddr>\n\t\t</Address1>\n\t\t<Address2>\n\t\t\t<AddrLine1 />\n\t\t\t<AddrLine2 />\n\t\t\t<AddrLine3 />\n\t\t\t<Landmark />\n\t\t\t<Pincode>000000</Pincode>\n\t\t\t<City></City>\n\t\t\t<State></State>\n\t\t\t<Country></Country>\n\t\t\t<AddressType></AddressType>\n\t\t\t<HomeTelNo />\n\t\t\t<OfficeTelNo />\n\t\t\t<FAXNO />\n\t\t\t<MobileNo></MobileNo>\n\t\t\t<EmailAddr></EmailAddr>\n\t\t</Address2>\n\t\t<VIPFlag></VIPFlag>\n\t\t<VIPCategory />\n\t</Client>\n\t<Receipt>\n\t\t<UniqueTranKey></UniqueTranKey>\n\t\t<CheckType />\n\t\t<BSBCode />\n\t\t<TransactionDate></TransactionDate>\n\t\t<ReceiptType>IVR</ReceiptType>\n\t\t<Amount></Amount>\n\t\t<TCSAmount />\n\t\t<TranRefNo></TranRefNo>\n\t\t<TranRefNoDate></TranRefNoDate>\n\t</Receipt>\n\t<Risk>\n\t\t<PolicyType>HTI</PolicyType>\n\t\t<Duration>1</Duration>\n\t\t<Installments>FULL</Installments>\n\t\t<PaymentType>IVR</PaymentType>\n\t\t<IsFgEmployee>N</IsFgEmployee>\n\t\t<BranchReferenceID />\n\t\t<FGBankBranchStaffID />\n\t\t<BankStaffID />\n\t\t<BankCustomerID />\n\t\t<BancaChannel />\n\t\t<PartnerRefNo />\n\t\t<PayorID />\n\t\t<PayerName />\n\t\t<BeneficiaryDetails>\n\t\t\t<Member>\n\t\t\t\t<MemberId>1</MemberId>\n\t\t\t\t<InsuredName></InsuredName>\n\t\t\t\t<InsuredDob>10/10/2000</InsuredDob>\n\t\t\t\t<InsuredGender></InsuredGender>\n\t\t\t\t<InsuredOccpn></InsuredOccpn>\n\t\t\t\t<CoverType>VITAL</CoverType>\n\t\t\t\t<SumInsured>300000</SumInsured>\n\t\t\t\t<DeductibleDiscount></DeductibleDiscount>\n\t\t\t\t<Relation>SELF</Relation>\n\t\t\t\t<NomineeName></NomineeName>\n\t\t\t\t<NomineeRelation></NomineeRelation>\n\t\t\t\t<AnualIncome />\n\t\t\t\t<Height></Height>\n\t\t\t\t<Weight></Weight>\n\t\t\t\t<NomineeAge></NomineeAge>\n\t\t\t\t<AppointeeName />\n\t\t\t\t<AptRelWithominee />\n\t\t\t\t<MedicalLoading>0</MedicalLoading>\n\t\t\t\t<PreExstDisease>N</PreExstDisease>\n\t\t\t\t<DiseaseMedicalHistoryList>\n\t\t\t\t\t<DiseaseMedicalHistory>\n\t\t\t\t\t\t<PreExistingDiseaseCode />\n\t\t\t\t\t\t<MedicalHistoryDetail />\n\t\t\t\t\t</DiseaseMedicalHistory>\n\t\t\t\t</DiseaseMedicalHistoryList>\n\t\t\t</Member>\n\t\t</BeneficiaryDetails>\n\t</Risk>\n</Root>]]>\n</tem:XML>\n</tem:CreatePolicy>\n</soapenv:Body>\n</soapenv:Envelope>"


data="""<Root>
	<Uid>251024242366</Uid>
	<VendorCode>webagg</VendorCode>
	<VendorUserId>IINSURE</VendorUserId>
	<WinNo />
	<ApplicationNo />
	<PolicyHeader>
		<PolicyStartDate>15/10/2021</PolicyStartDate>
		<PolicyEndDate>14/10/2023</PolicyEndDate>
		<AgentCode>60001464</AgentCode>
		<BranchCode>10</BranchCode>
		<MajorClass>HTO</MajorClass>
		<ContractType>HTO</ContractType>
		<METHOD>ENQ</METHOD>
		<PolicyIssueType>I</PolicyIssueType>
		<PolicyNo />
		<ClientID></ClientID>
		<ReceiptNo />
	</PolicyHeader>
	<POS_MISP>
		<Type />
		<PanNo />
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
		<PANNo />
		<GSTIN />
		<AadharNo />
		<CKYCNo />
		<EIANo />
		<Address1>
			<AddrLine1></AddrLine1>
			<AddrLine2 />
			<AddrLine3 />
			<Landmark />
			<Pincode>000000</Pincode>
			<City></City>
			<State></State>
			<Country></Country>
			<AddressType></AddressType>
			<HomeTelNo />
			<OfficeTelNo />
			<FAXNO />
			<MobileNo></MobileNo>
			<EmailAddr></EmailAddr>
		</Address1>
		<Address2>
			<AddrLine1 />
			<AddrLine2 />
			<AddrLine3 />
			<Landmark />
			<Pincode>000000</Pincode>
			<City></City>
			<State></State>
			<Country></Country>
			<AddressType></AddressType>
			<HomeTelNo />
			<OfficeTelNo />
			<FAXNO />
			<MobileNo></MobileNo>
			<EmailAddr></EmailAddr>
		</Address2>
		<VIPFlag></VIPFlag>
		<VIPCategory />
	</Client>
	<Receipt>
		<UniqueTranKey></UniqueTranKey>
		<CheckType />
		<BSBCode />
		<TransactionDate></TransactionDate>
		<ReceiptType>IVR</ReceiptType>
		<Amount></Amount>
		<TCSAmount />
		<TranRefNo></TranRefNo>
		<TranRefNoDate></TranRefNoDate>
	</Receipt>
	<Risk>
		<PolicyType>HTF</PolicyType>
		<Duration>1</Duration>
		<Installments>FULL</Installments>
		<PaymentType>IVR</PaymentType>
		<IsFgEmployee>N</IsFgEmployee>
		<BranchReferenceID />
		<FGBankBranchStaffID />
		<BankStaffID />
		<BankCustomerID />
		<BancaChannel />
		<PartnerRefNo />
		<PayorID />
		<PayerName />
		<BeneficiaryDetails>
			<Member>
				<MemberId>1</MemberId>
				<InsuredName></InsuredName>
				<InsuredDob>10/10/2000</InsuredDob>
				<InsuredGender></InsuredGender>
				<InsuredOccpn></InsuredOccpn>
				<CoverType>VITAL</CoverType>
				<SumInsured>300000</SumInsured>
				<DeductibleDiscount></DeductibleDiscount>
				<Relation>SELF</Relation>
				<NomineeName></NomineeName>
				<NomineeRelation></NomineeRelation>
				<AnualIncome />
				<Height></Height>
				<Weight></Weight>
				<NomineeAge></NomineeAge>
				<AppointeeName />
				<AptRelWithominee />
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
				<InsuredName></InsuredName>
				<InsuredDob>06/06/1999</InsuredDob>
				<InsuredGender></InsuredGender>
				<InsuredOccpn></InsuredOccpn>
				<CoverType>VITAL</CoverType>
				<SumInsured>300000</SumInsured>
				<DeductibleDiscount></DeductibleDiscount>
				<Relation>SPOU</Relation>
				<NomineeName></NomineeName>
				<NomineeRelation></NomineeRelation>
				<AnualIncome />
				<Height></Height>
				<Weight></Weight>
				<NomineeAge></NomineeAge>
				<AppointeeName />
				<AptRelWithominee />
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

data_2="""<?xml version="1.0" encoding="UTF-8" ?>
<root>
	<Uid>251024242366</Uid>
	<VendorCode>webagg</VendorCode>
	<VendorUserId>IINSURE</VendorUserId>
	<WinNo></WinNo>
	<ApplicationNo></ApplicationNo>
	<PolicyHeader>
		<PolicyStartDate>16/10/2021</PolicyStartDate>
		<PolicyEndDate>15/10/2023</PolicyEndDate>
		<AgentCode>60001464</AgentCode>
		<BranchCode>10</BranchCode>
		<MajorClass>HTO</MajorClass>
		<ContractType>HTO</ContractType>
		<METHOD>ENQ</METHOD>
		<PolicyIssueType>I</PolicyIssueType>
		<PolicyNo></PolicyNo>
		<ClientID></ClientID>
		<ReceiptNo></ReceiptNo>
	</PolicyHeader>
	<POS_MISP>
		<Type></Type>
		<PanNo></PanNo>
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
		<PANNo></PANNo>
		<GSTIN></GSTIN>
		<AadharNo></AadharNo>
		<CKYCNo></CKYCNo>
		<EIANo></EIANo>
		<Address1>
			<AddrLine1></AddrLine1>
			<AddrLine2></AddrLine2>
			<AddrLine3></AddrLine3>
			<Landmark></Landmark>
			<Pincode>000000</Pincode>
			<City></City>
			<State></State>
			<Country></Country>
			<AddressType></AddressType>
			<HomeTelNo></HomeTelNo>
			<OfficeTelNo></OfficeTelNo>
			<FAXNO></FAXNO>
			<MobileNo></MobileNo>
			<EmailAddr></EmailAddr>
		</Address1>
		<Address2>
			<AddrLine1></AddrLine1>
			<AddrLine2></AddrLine2>
			<AddrLine3></AddrLine3>
			<Landmark></Landmark>
			<Pincode>000000</Pincode>
			<City></City>
			<State></State>
			<Country></Country>
			<AddressType></AddressType>
			<HomeTelNo></HomeTelNo>
			<OfficeTelNo></OfficeTelNo>
			<FAXNO></FAXNO>
			<MobileNo></MobileNo>
			<EmailAddr></EmailAddr>
		</Address2>
		<VIPFlag></VIPFlag>
		<VIPCategory></VIPCategory>
	</Client>
	<Receipt>
		<UniqueTranKey></UniqueTranKey>
		<CheckType></CheckType>
		<BSBCode></BSBCode>
		<TransactionDate></TransactionDate>
		<ReceiptType>IVR</ReceiptType>
		<Amount></Amount>
		<TCSAmount></TCSAmount>
		<TranRefNo></TranRefNo>
		<TranRefNoDate></TranRefNoDate>
	</Receipt>
	<Risk>
		<PolicyType>HTF</PolicyType>
		<Duration>1</Duration>
		<Installments>FULL</Installments>
		<PaymentType>IVR</PaymentType>
		<IsFgEmployee>N</IsFgEmployee>
		<BranchReferenceID></BranchReferenceID>
		<FGBankBranchStaffID></FGBankBranchStaffID>
		<BankStaffID></BankStaffID>
		<BankCustomerID></BankCustomerID>
		<BancaChannel></BancaChannel>
		<PartnerRefNo></PartnerRefNo>
		<PayorID></PayorID>
		<PayerName></PayerName>
		<BeneficiaryDetails>
			<Member>
				<MemberId>1</MemberId>
				<InsuredName></InsuredName>
				<InsuredDob>10/10/2000</InsuredDob>
				<InsuredGender>M</InsuredGender>
				<InsuredOccpn></InsuredOccpn>
				<CoverType>VITAL</CoverType>
				<SumInsured>500000</SumInsured>
				<DeductibleDiscount></DeductibleDiscount>
				<Relation>SELF</Relation>
				<NomineeName></NomineeName>
				<NomineeRelation></NomineeRelation>
				<AnualIncome></AnualIncome>
				<Height></Height>
				<Weight></Weight>
				<NomineeAge></NomineeAge>
				<AppointeeName></AppointeeName>
				<AptRelWithominee></AptRelWithominee>
				<MedicalLoading>0</MedicalLoading>
				<PreExstDisease>N</PreExstDisease>
				<DiseaseMedicalHistoryList>
					<DiseaseMedicalHistory>
						<PreExistingDiseaseCode></PreExistingDiseaseCode>
						<MedicalHistoryDetail></MedicalHistoryDetail>
					</DiseaseMedicalHistory>
				</DiseaseMedicalHistoryList>
			</Member>
			<Member>
				<MemberId>2</MemberId>
				<InsuredName></InsuredName>
				<InsuredDob>06/06/1999</InsuredDob>
				<InsuredGender>F</InsuredGender>
				<InsuredOccpn></InsuredOccpn>
				<CoverType>VITAL</CoverType>
				<SumInsured>500000</SumInsured>
				<DeductibleDiscount></DeductibleDiscount>
				<Relation>SPOU</Relation>
				<NomineeName></NomineeName>
				<NomineeRelation></NomineeRelation>
				<AnualIncome></AnualIncome>
				<Height></Height>
				<Weight></Weight>
				<NomineeAge></NomineeAge>
				<AppointeeName></AppointeeName>
				<AptRelWithominee></AptRelWithominee>
				<MedicalLoading>0</MedicalLoading>
				<PreExstDisease>N</PreExstDisease>
				<DiseaseMedicalHistoryList>
					<DiseaseMedicalHistory>
						<PreExistingDiseaseCode></PreExistingDiseaseCode>
						<MedicalHistoryDetail></MedicalHistoryDetail>
					</DiseaseMedicalHistory>
				</DiseaseMedicalHistoryList>
			</Member>
		</BeneficiaryDetails>
	</Risk>
</root>"""

from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

quotation_payload={
  "Root": {
    "Uid": 251024242366,
    "VendorCode": "webagg",
    "VendorUserId": "IINSURE",
    "WinNo": "",
    "ApplicationNo": "",
    "PolicyHeader": {
      "PolicyStartDate": "16/10/2021",
      "PolicyEndDate": "15/10/2023",
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
        "Pincode": "000000",
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
        "Pincode": "000000",
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
            "InsuredGender": "M",
            "InsuredOccpn": "",
            "CoverType": "VITAL",
            "SumInsured": 500000,
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
            "InsuredGender": "F",
            "InsuredOccpn": "",
            "CoverType": "VITAL",
            "SumInsured": 500000,
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
# quotation_payload=json.dumps(quotation_payload["Root"])

# data = readfromstring(
#     str(quotation_payload)
# )
# data_2=str(json2xml.Json2xml(data, item_wrap=False,attr_type=False).to_xml()).replace("<all>","<Root>")

from dicttoxml import dicttoxml
xml = dicttoxml(quotation_payload["Root"],attr_type=False)

data_2=str(xml).replace("<Member>","").replace("</Member>","").replace("<root>","<Root>").replace("</root>","</Root>").replace("<item>","<Member>").replace("</item>","</Member>")

data_2=data_2[23+18:-1]

payload="""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
    <soapenv:Header/>
    <soapenv:Body>
        <tem:CreatePolicy>
            <tem:Product>HealthTotal</tem:Product>
            <tem:XML>
                <![CDATA[{}]]>
            </tem:XML>
        </tem:CreatePolicy>
    </soapenv:Body>
</soapenv:Envelope>""".format(data_2)



headers = {
  'Content-Type': 'text/xml',
  'SOAPAction': 'http://tempuri.org/IService/CreatePolicy',
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)



