import urllib.parse


import requests
import json


client_secret='2D9D1BC5A837E7A2741C6121317E9EE6CE1D32145CBCF7084FA4493ECDA2C2804969A5473610BC2AB4FC034359C11D55F99F8AEC736D84F0EFD531DFE24FFC74F0923F1288A83121B8045A8AAA4D9F920B4D737E3A1134B824E23B1F0561D97AEA647554A31570720BDB6E4CE3D8813A1138ABF16F2A23A8E6BAB012DD07B768019A5B583351F6D36C1F6F26B5C8D474D2F701E664A96F73806EE3A5235DEFFD76CF4106F7F074A55258D75B1DDEFD38'
cookie_for_quotation="JSESSIONID=722D1410A0DBB02AA86D10ADEC119204; TS011c0d7b=0155a4f855649d53d005c7da19110096b6a81049b38df413564644ce31be0429b5336b8fc942b3f8fd2054ae252fb6377b643b270ef96414c4aae2d7d4fa6cf69a4e7e8045; BIGipServerpip_uatpool=!NCIdspdF+VCw16z7MZJp2Dgyief5yf1GLGIpodyrNZqwc68JH4DjK78jQglT6o872KielKA8gRaV; TS018f013d=0155a4f855ad80625350c22790d51904da722f2d9f858020d6a3f8e357540300f02ececb475dff8d6f5270f627b35c2da4347fb9c626971684dff684335da176e81989109c"
x={
    "make": "7223",
    "model": "23391",
    "variant": "28428",
    "product_type": None,
    "loan": 0,
    "is_vehicle_new": 0,
    "registration_date": "01/01/2019",
    "idv": 0,
    "trailer_idv": 0,
    "policy_type": "CO",
    "previous_policy_end_date": "26/07/2021",
    "previous_policy_type": "TP",
    "previous_policy_claim": "N",
    "previous_insurer": "Tata AIG General Insurance",
    "registration_no": "DL-01-ABC-1234",
    "rto": "DL01",
    "ncb": "0",
    "manufacturing_year": "2019",
    "category": 2,
    "add_ons": [],
    "owner_type": "Individual",
    "additional_cover": {}
}

request_data = {
    'QDATA': {
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
    },
    'SRC': 'TP',
    'T': client_secret,
    'productid': '3121'
}




import requests

url = "https://pipuat.tataaiginsurance.in/tagichubms/ws/v1/ws/tran1/quotation"

headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=722D1410A0DBB02AA86D10ADEC119204; TS011c0d7b=0155a4f855649d53d005c7da19110096b6a81049b38df413564644ce31be0429b5336b8fc942b3f8fd2054ae252fb6377b643b270ef96414c4aae2d7d4fa6cf69a4e7e8045; BIGipServerpip_uatpool=!NCIdspdF+VCw16z7MZJp2Dgyief5yf1GLGIpodyrNZqwc68JH4DjK78jQglT6o872KielKA8gRaV; TS018f013d=0155a4f855ad80625350c22790d51904da722f2d9f858020d6a3f8e357540300f02ececb475dff8d6f5270f627b35c2da4347fb9c626971684dff684335da176e81989109c; JSESSIONID=4F0FDEB456B8C3E7ACF407AE443D615E; TS011c0d7b=0155a4f85535b103a72ef498dff2050894365ee4278df413564644ce31be0429b5336b8fc942b3f8fd2054ae252fb6377b643b270e4c81f58193e7fd7036f11ec298326d56; TS018f013d=0155a4f85533caaa959aa430e84347b1c19622be3269ff6c82d9ec5bf096348589b26936d748123073791634e0854f3491ae203e77d05a5fd59a8a5424e068ca969d3d238f'
}


# response = requests.request("POST", url, headers=headers, data=request_data)
# print(response)
print(x["previous_policy_end_date"])