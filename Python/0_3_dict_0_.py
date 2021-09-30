class Solution:
    def dictStartWith(self):
        dict_={
            'samir sa':3,
            'asadsa sa':5,
            'samir sae rerg':3,
        }
        x=[k for k in dict_.keys() if k.startswith('samir')]
        print(x)
        
sol=Solution()
# print(sol.dictStartWith())

quote_payload_self={
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
        "include_proposer": 0,
    },
}

x=quote_payload_self['payload']['members']
x.append({'sam':23})
print(x)
print(quote_payload_self['payload']['members'])

