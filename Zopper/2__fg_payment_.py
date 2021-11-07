

import hashlib


request_data={
    'TransactionID':"b96c6d6f34defdb2deb008b2ad1a5cda",
    'PaymentOption':"1",
    'ResponseURL':"http://abclife.com/PayRes/ResponseHandler.aspx",
    'ProposalNumber':"b96c6d6f34defdb2deb008b2ad1a5cda",
    'PremiumAmount':"9730614299",
    'UserIdentifier':"NA",
    'UserId':"NA",
    'FirstName':"Samir",
    'LastName':"Patil",
    'Mobile':"9730614299",
    'Email':"samirspatil742099@gmail.com",
}

def genarate_checksum(request_data:dict):
    
    values="TransactionID|PaymentOption|ResponseURL|ProposalNumber|PremiumAmount|UserIdentifier|UserId|FirstName|LastName|Mobile|Email"
    values=values.split("|")
    # values=set(values)
    text=""
    print(values)
    for key in values:
        if key in request_data and request_data[key]!="":
            text+=request_data[key]+"|"
            
    print(text)
    encoded=text.encode()
    result = hashlib.sha256(encoded)
    print(result.hexdigest())
    
    text="AJ123456789|3|http://fglpg001.futuregenerali.in/ECOM_NL/WEBAPPLN/UI/Common/WebAggData.aspx|A321456987|1000|TestAgg|456|tester|tester|987654321|test@test.com|17/04/2018 11:16:14 AM |"
    print(text)
    encoded=text.encode()
    result = hashlib.sha256(encoded)
    print(result.hexdigest())
    
    
genarate_checksum(request_data)      

def checksum(data):
    final_string = "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(
            data.get('TransactionID'), data.get('PaymentOption'),
            data.get('ResponseURL'),
            data.get('ProposalNumber'), data.get('PremiumAmount'),
            data.get('UserIdentifier'),
            data.get('UserId'), data.get('FirstName'),
            data.get('LastName'), data.get('Mobile'),
            data.get('Email')
        )
    signature = hashlib.sha256(final_string.encode())
    checksum_ = signature.hexdigest()
    return checksum_

print(checksum(request_data))