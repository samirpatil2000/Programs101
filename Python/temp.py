import requests, json
import urllib.parse
payload={
          "add_ons": [],
          "insurer_logo": "https://general.futuregenerali.in/img/logo.png",
          "additional_cover": {},
          "registration_date": "01/01/2018",
          "idv": 0,
          "manufacturing_year": "2018",
          "product_type": None,
          "registration_no": "DL-01-AC-1234",
          "businessid": 5,
          "make": "9106",
          "previous_policy_claim": "N",
          "previous_policy_end_date": "29/07/2021",
          "previous_insurer": "Bajaj Allianz General Insurance",
          "insurance_name": "TATA AIG Motor Insurance",
          "is_vehicle_new": 0,
          "model": "25287",
          "previous_policy_start_date": "30/07/2020",
          "rto": "DL01",
          "previous_policy_type": "CO",
          "unique_identifier": "dfea4d8312c5ad541984146b69b2fa1e",
          "ncb": "20",
          "request_id": "4455843ac099a96d569d53e90f8c1edb",
          "variant": "30336",
          "loan": 0,
          "policy_type": "CO",
          "category": 4,
          "insurer_code": "TIG4W",
          "owner_type": "Individual"
        }
request_data = {
      "functionality": "validatequote",
      "supporttag": "genvalidatequote",
      "vehicle": {
        "bank_response": "",
        "quotation_no": "",
        "segment_code": "3",
        "segment_name": "Mid Size",
        "cc": "1498",
        "sc": "5",
        "FP_FLAG": "N",
        "sol_id": "1001",
        "lead_id": "user123",
        "mobile_no": "7710843777",
        "email_id": "madhura.nucsoft@tataaig.com",
        "emp_email_id": "",
        "customer_type": "Individual",
        "product_code": "3121",
        "product_name": "Private Car",
        "subproduct_code": "45",
        "subproduct_name": "Private Car",
        "subclass_code": "",
        "subclass_name": "",
        "misclass_code": "",
        "misclass_name": "",
        "covertype_code": "1",
        "covertype_name": "Package",
        "btype_code": "2",
        "btype_name": "Roll Over",
        "risk_startdate": "20210821",
        "risk_enddate": "20220822",
        "purchase_date": "20180703",
        "regi_date": "",
        "veh_age": "1",
        "manf_year": "2020",
        "make_code": "158",
        "make_name": "HONDA",
        "model_code": "1023492",
        "model_name": "NEW JAZZ",
        "variant_code": "1023497",
        "variant_name": "1.5 VX I DTEC",
        "model_parent_code": "1023492",
        "fuel_code": "2",
        "fuel_name": "Diesel",
        "gvw": "0",
        "age": "1",
        "miscdtype_code": "",
        "bodytype_id": "34",
        "idv": "720560",
        "revised_idv": "720560",
        "regno_1": "ap",
        "regno_2": "16",
        "regno_3": "ff",
        "regno_4": "5655",
        "rto_loc_code": "6360",
        "rto_loc_name": "Vijayawada AP-16",
        "rtolocationgrpcd": "2",
        "rto_zone": "B",
        "rating_logic": "Campaign",
        "campaign_id": 200072,
        "fleet_id": 10729,
        "discount_perc": "10",
        "pp_covertype_code": "1",
        "pp_covertype_name": "Package",
        "pp_enddate": "20210615",
        "pp_claim_yn": "0",
        "pp_prev_ncb": "20",
        "pp_curr_ncb": "25",
        "addon_plan_code": "P1",
        "addon_choice_code": "CHOICE1",
        "cust_name": "",
        "ab_cust_id": "",
        "ab_emp_id": "",
        "usr_name": "user123",
        "grp_name": "CANARA",
        "producer_code": "0015455000",
        "pup_check": "N",
        "pos_panNo": "",
        "pos_aadharNo": "",
        "is_cust_JandK": "NO",
        "cust_pincode": "401107",
        "cust_gstin": "",
        "tenure": "1",
        "uw_discount": "0",
        "Uw_DisDb": "",
        "uw_load": "",
        "uw_loading_discount": "0",
        "uw_loading_discount_flag": "D",
        "engine_no": "",
        "chasis_no": "",
        "rating_zone": "B",
        "veh_cng_lpg_insured": "N",
        "veh_type": "",
        "bodytype_desc": "",
        "veh_sub_body": "",
        "goods_normally_carry": "",
        "odometer_reading": "",
        "trailer_under_tow": "",
        "towed_by": "",
        "bus_type": "",
        "type_of_body": "",
        "basis_of_rating": "Underwriting Discount",
        "external_built": "",
        "trailer_idv": "",
        "driver_nominee_name": "",
        "driver_nominee_age": "",
        "driver_nominee_relation": "Select",
        "driver_declaration": "ODD01",
        "fb_lead_gen_code": "",
        "fb_lead_con_id": "",
        "is_ivehicle": "N",
        "ac_opted_in_pp": "N",
        "baserate": "",
        "lower_baserate": "",
        "upper_baserate": "",
        "los_code": "",
        "hdb_last_edit": "Status Search",
        "tppolicytype": "",
        "tppolicytenure": "",
        "business_location": "",
        "src": "CANARA",
        "axisuserid": "",
        "part_empcode": "",
        "verifier_id": "",
        "can_sso_roletype": None,
        "can_sso_batchid": "",
        "account_number": "",
        "option_for_calc": "Yearly",
        "pre_policy_start_date": ""
      },
      "cover": {
        "C1": {
          "opted": "Y"
        },
        "C2": {
          "opted": "Y"
        },
        "C3": {
          "opted": "Y",
          "tenure": "1"
        },
        "C4": {
          "opted": "N",
          "SI": ""
        },
        "C5": {
          "opted": "N",
          "SI": ""
        },
        "C7": {
          "opted": "N",
          "SI": ""
        },
        "C8": {
          "opted": "N"
        },
        "C10": {
          "opted": "N",
          "SI": ""
        },
        "C11": {
          "opted": "N"
        },
        "C12": {
          "opted": "N"
        },
        "C15": {
          "opted": "Y",
          "perc": "25"
        },
        "C17": {
          "opted": "N",
          "SI": "",
          "persons": "0"
        },
        "C18": {
          "opted": "N",
          "persons": "2"
        },
        "C45": {
          "opted": "N"
        },
        "C29": {
          "opted": "N"
        },
        "C47": {
          "opted": "N"
        },
        "C39": {
          "opted": "N"
        },
        "C38": {
          "opted": "N"
        },
        "C37": {
          "opted": "N"
        },
        "C48": {
          "opted": "N",
          "SI": None
        },
        "C49": {
          "opted": "N",
          "SI": None
        },
        "C50": {
          "opted": "N",
          "SI": None
        },
        "C51": {
          "opted": "N",
          "SI": None
        },
        "C13": {
          "opted": "N"
        },
        "C14": {
          "opted": "N"
        },
        "C6": {
          "opted": "N",
          "SI": ""
        },
        "C35": {
          "opted": "N",
          "no_of_claims": "",
          "Deductibles": "0"
        },
        "C40": {
          "opted": "N"
        },
        "C26": {
          "opted": "N",
          "SI": "",
          "persons": "0"
        },
        "C25": {
          "opted": "N",
          "SI": "",
          "persons": ""
        },
        "C21": {
          "opted": "N",
          "persons": ""
        },
        "C22": {
          "opted": "N",
          "persons": ""
        },
        "C23": {
          "opted": "N",
          "persons": ""
        },
        "C32": {
          "opted": "N",
          "persons": ""
        },
        "C24": {
          "opted": "N"
        },
        "C53": {},
        "C55": {
          "opted": "N",
          "number_of_days": ""
        },
        "C56": {
          "opted": "N",
          "loan_amount": ""
        },
        "C57": {
          "opted": "N"
        },
        "C58": {
          "opted": "N"
        }
      }
}
# request_data = json.dumps(request_data)
# # request_data=urllib.parse.encode(request_data)
# url = "https://pipuat.tataaiginsurance.in/tagichubms/ws/v1/ws/tran1/quotation"
# payload = """QDATA={}&SRC=TP&T=2D9D1BC5A837E7A2741C6121317E9EE6CE1D32145CBCF7084FA4493ECDA2C2804969A5473610BC2AB4FC034359C11D55F99F8AEC736D84F0EFD531DFE24FFC74F0923F1288A83121B8045A8AAA4D9F920B4D737E3A1134B824E23B1F0561D97AEA647554A31570720BDB6E4CE3D8813A1138ABF16F2A23A8E6BAB012DD07B768019A5B583351F6D36C1F6F26B5C8D474D2F701E664A96F73806EE3A5235DEFFD76CF4106F7F074A55258D75B1DDEFD38&productid=3121""".format(request_data)
# response = requests.request("POST", url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=payload)
# print(response.text)\

# today=date.today()
# # print(int(payload.get('registration_date')[-4:])-today.year)

# registration_no=payload.get("registration_no") # DL-01-ABC-1234
# if registration_no:
#     reg_no=registration_no[0:2]+registration_no[2:4] #DL01
    

#     # print (registration_no[0:2])
#     # print (registration_no[3:5])
#     # print (registration_no[6:8])
#     # state_code=registration_no[6:8]
#     # if registration_no[8]!='-':
#     #       state_code+=registration_no[8]
#     # print(state_code)
#     # print (registration_no[-4:])
    
#     	# print(roles[2],999)
# 	# print(roles[3],999)
# 	# u_roles = []  	
# 	# obj = Account.objects.get(user=request.user, is_active=True)
# 	# print(obj)
# 	# u_roles = obj.user_role.all()
#   # u_roles=[i.get_id_display() for i in u_roles]
# 	# print(u_roles,5555)
from datetime import date, timedelta
from datetime import datetime

date_=payload.get('previous_policy_end_date')
date_=date_[-4:]+"-"+date_[-7:-5]+"-"+date_[-10:-8]

date_string = date_
print(date_string)
# date_string = "2012-12-12 10:10:10"
x=datetime.fromisoformat(date_string)+timedelta(days=1)
print (str(x.date()).replace("-",""))


ADDONS_AND_COVERS={
    "ea": {
        "code": "C4",
        "opted": "Y",
        "SI": "9999"
    },
    "CNG/LPG kitcheckbox":{
        "code": "C29",
        "opted": "N",
    },
    "nea":{
        "code": "C4",
        "opted": "Y",
        "SI": "9999"
    },
    "ri":{
        "code": "C38",
        "opted": "Y"
    },
    "rsa":{
        "code": "C47",
        "opted":"Y"
    },
    "cc":{
        "code": "C37",
        "opted": "Y"
    },
    "pod":{
        "code":"C3",
        "opted": "Y",
        "tenure": "1"
    },
    "LLPD":{
        "code": "C18",
        "opted": "Y",
        "persons": "3",
    },
}

add_ons={
  "add_ons": [
        "dca",
        "ep",
        "cc",
        "rsa",
        "kr",
        "zp",
        "np",
        "ri",
        "lpb"
    ],
  "additional_cover": {
        "ea": 1000,
        "LLPD": 0,
        "pod": 0,
        "nea": 1000,
        "Fuel_od": 100,
        "CNG/LPG kitcheckbox": 0
  },
}

# for i in add_ons['additional_cover']:
#   if ADDONS_AND_COVERS.get(i):
#     i_add_on_code = ADDONS_AND_COVERS.get(i).get('code')
#     print(ADDONS_AND_COVERS.get(i))
#     for field in ADDONS_AND_COVERS.get(i):
#       if field != "code" and field != "opted":
#             print(field,add_ons['additional_cover'][i])
#       elif field == "opted":
#             print('Y')
# name="HONDA|AMAZE|ERA +|814CC"
            
# make_name,model_name,variant_name,CC=name.split("|")
# # make=name.split("|")
# print(make_name,model_name,variant_name,CC[:-2])
# # print(make)

def strip_date(date_: str, isoFormat=False) -> str:
  if isoFormat:
    return date_[-4:] + "-" + date_[-7:-5] + "-" + date_[-10:-8]
  return date_[-4:] + date_[-7:-5] + date_[-10:-8]

date_ = payload.get('previous_policy_end_date')
print(date_,"#")
date_ = date_[-4:] + "-" + date_[-7:-5] + "-" + date_[-10:-8]
x=datetime.fromisoformat(date_)+timedelta(days=1)
print(str(x.date()).replace("-",""))
