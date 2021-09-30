request_data={
    'TransactionID':"AB123456",
    'PaymentOption':"1",
    'ResponseURL':"http://abclife.com/PayRes/ResponseHandler.aspx",
    'ProposalNumber':"A0123464",
    'PremiumAmount':"3000",
    'UserIdentifier':"",
    'UserId':"Sharma1234",
    'FirstName':"Rajesh",
    'LastName':"Sharma",
    'Mobile':"9809801234",
    'Email':"test@gmail.com",
    'Vendor':"",
    'CheckSum':"ba22169f08849e9b39871d8df64241cd60e6c27108e44322ebc1fc07f84c4819"
}


def genarate_checksum(request_data:dict):
    import hashlib
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
    print(result)
    print(result.hexdigest())
    
    
    
genarate_checksum(request_data)      