# custom-addons/live_chat_extension/controllers/main.py

import json
from datetime import datetime
from odoo import http, fields, _
from odoo.http import request
import logging

class SellerChannel(http.Controller):
    
    def create_channel(self,auth_token):
        try:
            
            Partner = request.env["res.partner"].sudo()
            Channel = request.env["im_livechat.channel"].sudo()
            
            old_rec = Partner.search([('seller', '=', True), ('state', '!=', False), ('active', '=', True),('auth_token','=',auth_token)])
            
            channel = Channel.create({
                'name':old_rec,
                'user_ids':[(4,2)],
                'rule_ids':[(0,0,{'action':'auto_popup','auto_popup_timer':0,'regex_url':'/im_livechat/'}),
                            (0,0,{'action':'auto_popup','auto_popup_timer':0,'regex_url':'/en//im_livechat/'})]
            })
            return {
                    "status":True,
                    "message":"success",  # {error.message} is from try except 
                    'data':{
                        'message':"Channel Created"
                        }
                    }
        except Exception as e:
            return {
                    "status":False,
                    "message":"{e.message}"  # {error.message} is from try except 
                    }

    @http.route('/sellerapp/channel/', csrf=False, type='json', auth="none", methods=['POST'])
    def create_seller_channel(self, **post):
        return self.create_channel(post=post)
    
    @http.route('/sellerapp/channel/', csrf=False, type='json', auth="none", methods=['GET'])
    def get_seller_channel(self, **get):
        try:
            data = get.get("data", [])
            Partner = request.env["res.partner"].sudo()
            Channel = request.env["im_livechat.channel"].sudo()
            seller_mobile = data.get('mobile')
            old_rec = Partner.search([('seller', '=', True), ('state', '!=', False), ('active', '=', True),('phone','=',seller_mobile)])
            # if old_rec:
            channel = Channel.search([('name','=',data.get('seller',{}).get('name'))])
            if channel:
                return {
                        "status":1,
                        "message":"success",  # {error.message} is from try except 
                        "data":{
                            'chat_url': channel.web_page, 
                        }
                    }
            else:
                resuest_data={
                    
                }
                return self.create_channel()
        except Exception as e:
            return {
                    "status":0,
                    "message":"{e.message}"  # {error.message} is from try except 
                    }

def fun(x):
    try:
        if int(x):
            return x
    except Exception as e:
        print(e, "Type", type(e))
        json.dumps({
                "status":0,
                "message":e,  # {error.message} is from try except 
                })
        return {
                "status":0,
                "message":e,  # {error.message} is from try except 
                }

# print(fun("s"))

print(str(False))