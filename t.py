import grequests
import requests
import urllib.parse
import user_generator
import json
import time
import random
import datetime 

from bs4 import BeautifulSoup
from urllib.parse import unquote
now = datetime.datetime.now()
from faker import Faker
fake = Faker('nl_NL')
class Dolphin_Cookies_Convert():

    def __init__(self):
        print("init")
    def toPython(dolphin_json_cookies_path):
        cookies_const = {}
        puths = dolphin_json_cookies_path  # cookie_list[seed]
        print("Cookie: "+puths)

      
        open_cook = open(puths, "r")

        s = open_cook.read()
        d = json.loads(s)
        
        for cookie in d:
            #print(cookie["domain"])
            if(cookie["domain"] == ".tiktok.com"):
                cookies_const[cookie["name"]] = cookie["value"]
                # print("Ok .tiktok.com")
            elif(cookie["domain"] == "ads.tiktok.com"):
                cookies_const[cookie["name"]] = cookie["value"]
                # print("Ok ads.tiktok.com")
            elif(cookie["domain"] == ".mon-va.byteoversea.com"):
                cookies_const[cookie["name"]] = cookie["value"]
                # print("Ok .mon-va.byteoversea.com")
            elif(cookie["domain"] == "feelgood-api.tiktok.com"):
                cookies_const[cookie["name"]] = cookie["value"]
                # print("Ok feelgood-api.tiktok.com")
            elif(cookie["domain"] == ".byteoversea.com"):
                cookies_const[cookie["name"]] = cookie["value"]
                # print("Ok .byteoversea.com")
       
        result_cookies =  json.dumps(cookies_const, indent = 4) 
        print("Dolphin json cookies converted to python format")
        print(result_cookies)
        return result_cookies
       
    def toAxios(dolphin_json_cookies_path):
            cookies_const = {}
            puths = dolphin_json_cookies_path  # cookie_list[seed]
            print("Cookie: "+puths)

        
            open_cook = open(puths, "r")

            s = open_cook.read()
            d = json.loads(s)
            axios_const = list()
            
            for cookie in d:
                #print(cookie["domain"])
                if(cookie["domain"] == ".tiktok.com"):
                    
                    axios_const.append(cookie["name"]+'='+cookie["value"]+';')
                    
                    # print("Ok .tiktok.com")
                elif(cookie["domain"] == "ads.tiktok.com"):
                    axios_const.append(cookie["name"]+'='+cookie["value"]+';')
                    # print("Ok ads.tiktok.com")
                elif(cookie["domain"] == ".mon-va.byteoversea.com"):
                    axios_const.append(cookie["name"]+'='+cookie["value"]+';')
                    # print("Ok .mon-va.byteoversea.com")
                elif(cookie["domain"] == "feelgood-api.tiktok.com"):
                    axios_const.append(cookie["name"]+'='+cookie["value"]+';')
                    # print("Ok feelgood-api.tiktok.com")
                elif(cookie["domain"] == ".byteoversea.com"):
                    axios_const.append(cookie["name"]+'='+cookie["value"]+';')
                    # print("Ok .byteoversea.com")
            axios_result = "".join(map(str, axios_const))
               
            result_cookies =  json.dumps(cookies_const, indent = 4) 
            print("Dolphin json cookies converted to python format")
            print('"'+axios_result+'"')
            return '"'+axios_result+'"'


class Register():
    creos = 'pt5.json'
    open_creos = open(creos, 'r')

    s = open_creos.read()
    cr = json.loads(s)
    print('Количество креотивов=')
    print(cr['data']['total'])
    a = user_generator.UserGenerator()

    COOKIES = ''
    PROXY = {"http": "socks5://dekamerontink:q7SX5nD6IT@185.212.205.232:50101",
             "https": "socks5://dekamerontink:q7SX5nD6IT@185.212.205.232:50101"}

    def __init__(self):
        print('init')

    def headers_account(self):

        cookies = self.COOKIES

        headers = {
            'Connection': 'keep-alive',
            'TRACE-LOG-USER-ID': cookies['MONITOR_WEB_ID'],
            'Accept': 'application/json, text/plain, */*',
            'AC-CSRFToken': cookies['ac_csrftoken'],
            'User-Agent': a.USER_AGENT,
            'X-CSRFToken': cookies['csrftoken'],
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/register',
            'Accept-Language': 'en-US,en',
        }
        return headers

    def headers_update(self, id, cookies):
        headers = {
            'Connection': 'keep-alive',
            'TRACE-LOG-USER-ID': id,
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'TRACE-LOG-ADV-ID': id,
            'User-Agent': a.USER_AGENT,
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/qualification_new?aadvid='+str(id),
            'Accept-Language': 'en-US,en',
        }
        return headers

    def registration(self, json_data_generate):

        cookies = self.COOKIES
        #headers = self.headers_account()
        headers = {
            'Host': 'ads.tiktok.com',


            # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="101"',
            # 'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
       
            'Accept': 'application/json, text/plain, */*',
            # 'AC-CSRFToken': cookies['csrftoken'],
            'X-CSRFToken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/register?attr_source=ttba&attr_medium=business-suite&lang=en',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,tr;q=0.5,ar;q=0.4',
        }

        params = {
            'aadvid': ''
        }

        json_data = {
            "company": fake.bs(),
            "country": "NO",
            "phonenumber":  fake.phone_number(),
            "phonenumber_country": "NO",
            "timezone": "Europe/Stockholm",
            "currency": "NOK",
            "second_industry": "290606",
            "submit_page_url_base": "https://ads.tiktok.com/i18n/register/",
            "submit_page_url_query": {
        "_source_": "ads_homepage",
        "country": "NL",
        "from": "signup",
        "ab_version": ""
    },
            "risk_info": {}
        }
       # json_data = json_data_generate
    #     proxies = { "http": "http://127.0.0.1:8080",
    # "https": "http://127.0.0.1:8080"}
    # api/v3/i18n/account/self/register/
        #response = requests.post('https://ads.tiktok.com/api/v1/self-serve/adv-account/register/?aadvid=&msToken=&X-Bogus=DFSzswSLsbz/aZuxS3JOMz4MW6cc&_signature=_02B4Z6wo00001433BOQAAIDAUcwdPaz9s.uN9whAAIIGa8', cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY,timeout=50)
        response = requests.post('https://ads.tiktok.com/api/v1/self-serve/adv-account/register/', params=params,
                                 cookies=cookies, headers=headers, proxies=self.PROXY, json=json_data, timeout=50)
        print(response.json())
        id = response.json()['data']['advertiser_id']

        return id

    def pixel(self, id):
        import random
        cookies = self.COOKIES
        headers = {

         
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/events_manager/pixel?aadvid='+str(id),
            'Accept-Encoding': 'gzip, deflate',

        }
        params = {
            'aadvid': str(id),
        }

        json_data = {
            'PixelName': 'tt2_'+str(random.randint(3, 9)),
            'GTMStatus': False,
            'EventSetupMode': 1,
        }

        #res =requests.get("https://ads.tiktok.com/api/v2/i18n/pixel/list/?aadvid="+id+"&req_src=ad_creation&promotion_website_type=1&objective_type=3&msToken=5Omc7r6-nMlvmq2XDFt6r6tkjvt8ePV_1QnKtT9TINdVhlKV6M5rxVcqOT6W6vqO8HAoingiY0zHr9msfr4RrboeVJiAmJRCXdc4euBNFamxwSYz5Rv-aFxYY0TDZqT-uY4heA==&X-Bogus=DFSzswVupHJAWKT8gyPf&_signature=_02B4Z6woxIwAAIDBX90rVSNV2cQAnsAAAGL83a", headers=headers, timeout=50, proxies=self.PROXY,  cookies=cookies, json={"PixelName":"Pixel_account_"+str(id),"GTMStatus":False,"EventSetupMode":1})
        print('pixel')
       
        #a = res.json()['data']['PixelID']

        res = requests.post('https://ads.tiktok.com/i18n/events_manager/v2/api/pixel/create', params=params,
                            cookies=cookies, headers=headers, json=json_data, verify=True, proxies=self.PROXY)
        
        
        return res.json()['data']
    def pixel_page(self, id):


        cookies = self.COOKIES
        # import random
        headers = {
        'Host': 'ads.tiktok.com',
        'Sec-Ch-Ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'Request_start_time': '1674925756485',
        'X-Ttam-Uuid': '6aa3ca3a-ae28-4895-bf11-abfb8e09bcaf',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': a.USER_AGENT,
        'Accept': 'application/json, text/plain, */*',
        'X-Ttam-Version': '1.0.1.4980',
        'X-Csrftoken': cookies['csrftoken'],
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ads.tiktok.com/i18n/creation/adgroup?aadvid=7193748650219044866&creation_type=create_new&temp_campaign_id=1756286935757825',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
        #'Cookie': '_abck=7C9E9BF37D9F0F4EA7BC501B5B814B06~-1~YAAQpHuZXvlYnsuFAQAAQoZQ+QkMaB8uV4wuyhCpNLr0ywwB1Et12OGd2Dnd2GLrsh+stz076BjZroS/Pdj2nom7x+Fc6Kg2+si0beVJDjTveAzLUPCd5eAgjL0KdrgfrZZ2jIbQOlMAXr6PTOYJu0TRP7o24vcoGU3+aSU8aJgqCHxRIE53Jiw7dY1auYbvPIOJ8guo+BcvUeanNs6xG+G/6pJhCZa03mqz87c4QJThQn7wFhAgTt0smeGf1hffm0IUadO6g0KZQG2q4Tr/Xg4s5gnRkfgPvKWHdFjFhejriAjNfQ/23/382N7D116R91/AgpuAGumqMIP2y3aWNSzQBEInwK1AfJI0rhK3dcKbjCCPHtJPyO6UwWY=~-1~-1~-1; bm_sz=765B7ADD3048C6A0642135A8EC2E4730~YAAQpHuZXvpYnsuFAQAAQoZQ+RJseRCcg5rA/RDCLJpvzTrO6foV4jXgeOkboTVyXQ/cRFFgAxuzPVIaOt1KaZnrNqDmasHBNvG4FetGxgWcLGXKpsYSEN4HlMP+6PvIBPmYag4RaOgRCF+i4AcB4f/CHde3rj5KrHwb1yuyLYcmM33MQgysAuVGAGgMrapQrkHHvkeZp7wkQw5JfoHplyRcimUOJ0ctK6tY5gSDfRre5lex7g0y053gQPBdxrezKZwckMTj2uBpU8rwXPx3wLJxxh6BoNmO4eFYXKFyYDdPNDo=~3224627~3158838; passport_csrf_token=d30df8d5c3aafdb7e170958442f37447; passport_csrf_token_default=d30df8d5c3aafdb7e170958442f37447; lang_type=en; part=stable; pre_country=UA; csrftoken=UxLosNF1GKWkhah0EgX5nQOdtkiVdw5b; tta_attr_id=0.1674925084.7193748459650826242; tta_attr_id_mirror=0.1674925084.7193748459650826242; s_v_web_id=verify_ldg75ls8_vxKT3nhn_ZVYi_4OpX_8Zd5_DB4pVQ5WDzGY; sso_auth_status_ads=52080d273562c3e8bdf811746db21476; sso_auth_status_ss_ads=52080d273562c3e8bdf811746db21476; sso_uid_tt_ads=174c1f53001e1506fdf4a829495ee56654f516b0f46eb06c8d090a7fb8fab519; sso_uid_tt_ss_ads=174c1f53001e1506fdf4a829495ee56654f516b0f46eb06c8d090a7fb8fab519; toutiao_sso_user_ads=c74bd9af633021189f25a5f4375920de; toutiao_sso_user_ss_ads=c74bd9af633021189f25a5f4375920de; sid_ucp_sso_v1_ads=1.0.0-KDdlYWRhNzY0ZDNmNTBjNTgzMzBjZDJmYmQ0ZDg2ODFmMTdiOWYwYTIKIAiCiMi00YXV6mMQyajVngYYrwwgDDDJqNWeBjgBQOwHEAEaA3NnMSIgYzc0YmQ5YWY2MzMwMjExODlmMjVhNWY0Mzc1OTIwZGU; ssid_ucp_sso_v1_ads=1.0.0-KDdlYWRhNzY0ZDNmNTBjNTgzMzBjZDJmYmQ0ZDg2ODFmMTdiOWYwYTIKIAiCiMi00YXV6mMQyajVngYYrwwgDDDJqNWeBjgBQOwHEAEaA3NnMSIgYzc0YmQ5YWY2MzMwMjExODlmMjVhNWY0Mzc1OTIwZGU; passport_auth_status_ads=c9d60767e4a21c6b45db51d767be9f9e%2C; passport_auth_status_ss_ads=c9d60767e4a21c6b45db51d767be9f9e%2C; sid_guard_ads=85b6c9b67410ecd0afee7e7409985ddc%7C1674925130%7C863999%7CTue%2C+07-Feb-2023+16%3A58%3A49+GMT; uid_tt_ads=08652b5c6c9646b1da8da44a1820d94d89270940b51bbf1cbc6b71fe06ce7266; uid_tt_ss_ads=08652b5c6c9646b1da8da44a1820d94d89270940b51bbf1cbc6b71fe06ce7266; sid_tt_ads=85b6c9b67410ecd0afee7e7409985ddc; sessionid_ads=85b6c9b67410ecd0afee7e7409985ddc; sessionid_ss_ads=85b6c9b67410ecd0afee7e7409985ddc; sid_ucp_v1_ads=1.0.0-KGVmYzE0NTQwZDU2Mzc2NzI0MGU0NGUxMjIyMzFhMmM5MjQ5YTQ0MDYKGgiCiMi00YXV6mMQyqjVngYYrwwgDDgBQOwHEAEaA3NnMSIgODViNmM5YjY3NDEwZWNkMGFmZWU3ZTc0MDk5ODVkZGM; ssid_ucp_v1_ads=1.0.0-KGVmYzE0NTQwZDU2Mzc2NzI0MGU0NGUxMjIyMzFhMmM5MjQ5YTQ0MDYKGgiCiMi00YXV6mMQyqjVngYYrwwgDDgBQOwHEAEaA3NnMSIgODViNmM5YjY3NDEwZWNkMGFmZWU3ZTc0MDk5ODVkZGM; risk_cookie_key=4c202301-e34c-424e-a690-26171cc1824e; msToken=dkAEkjqOeugKEuH4bFqhlLYQhSiW-zCBEds1u_5Fjt6MrFY8ne5N19EuRhw0aJ_RnbkVFpVcCcXIJJjOUZtf4Uegebsyc2qPCvcFf43dTAOntFX1wGFY; msToken=dkAEkjqOeugKEuH4bFqhlLYQhSiW-zCBEds1u_5Fjt6MrFY8ne5N19EuRhw0aJ_RnbkVFpVcCcXIJJjOUZtf4Uegebsyc2qPCvcFf43dTAOntFX1wGFY; odin_tt=b08b3d128a9ad1e219d4776ebed3f43d21526a4900c9f8eb6bd5604201b1243fa09f528d30f8faaf4111d2650ed52478; ttwid=1%7C6NzNYt5l9fzQbe56PzrlvvT5wDItkFZcRUhLutR2DXE%7C1674925162%7C46a45a8f5a39ddda6a5a3e7bbfdd0b644eceb65637fa1cf8e6082e65a841573e',
     }

        params = {
        'aadvid': str(id),
        'req_src': 'ad_creation',
        'promotion_website_type': '1',
        'promotion_target_type': '0',
        'objective_type': '3',
    }

        res = requests.get('https://ads.tiktok.com/api/v2/i18n/pixel/list/', params=params, headers=headers, verify=True, cookies=self.COOKIES)

        print(res.json()['data']['pixel_list'])

        return res.json()['data']['pixel_list'][0]



    def pixel_update(self, id, pixel_code):
        cookies = self.COOKIES
        headers = {

            'Content-Length': '60',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/events_manager/pixel?aadvid='+str(id),
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'uk-UA,uk;q=0.9;en-US,en;q=0.8',
        }

        params = {
            'aadvid': str(id),
        }

        json_data = {
            'EventTriggerSetting': {
                'download_start': {
                    'WebEventType': 'download_start',
                    'TriggerRules': [
                        {
                            'TriggerType': 1,
                            'Variable': 9,
                            'Operator': 1,
                            'Value': fake.name(),
                            'PageURL': '',
                        },
                    ],
                    'Currency': 'USD',
                    'Value': '0',
                    'CountingMethod': 4,
                    'EventName': '',
                    'EventTriggerType': 1,
                },
                'shopping': {
                    'WebEventType': 'shopping',
                    'TriggerRules': [
                        {
                            'TriggerType': 1,
                            'Variable': 9,
                            'Operator': 1,
                            'Value': fake.name(),
                            'PageURL': '',
                        },
                    ],
                    'Currency': 'USD',
                    'Value': '0',
                    'CountingMethod': 4,
                    'EventName': '',
                    'EventTriggerType': 1,
                },
                'button': {
                    'Currency': 'USD',
                    'Value': '',
                    'EventName': '',
                    'CountingMethod': 4,
                    'TriggerRules': [
                        {
                            'Operator': 1,
                            'PageURL': '',
                            'TriggerType': 1,
                            'Value': fake.name(),
                            'Variable': 9,
                        },
                    ],
                    'WebEventType': 'button',
                    'EventTriggerType': 1,
                },
            },
        }

        response = requests.post('https://ads.tiktok.com/i18n/events_manager/v2/api/pixel/'+pixel_code+'/update_event_trigger_setting',
                                 params=params, cookies=cookies, headers=headers, json=json_data, verify=True, proxies=self.PROXY)
        

    def update(self, json_data_generate, id):
        seed = random.randint(1000, 9999)
        cookies = self.COOKIES
        prxs = {"http": "socks5://dekamerontink:q7SX5nD6IT@185.226.107.136:51331",
                "https": "socks5://dekamerontink:q7SX5nD6IT@185.226.107.136:51331"}
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="104", "Google Chrome";v="100"',
            'trace-log-adv-id': str(id),
            'accept-language': 'uk-UA,uk',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'content-type': 'application/json;charset=UTF-8',
            'accept': 'application/json, text/plain, */*',
            'x-csrftoken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/account/complete?aadvid='+str(id),
            # Requests sorts cookies= alphabetically
            # 'Cookie': '_abck=950DD841F8B0FA9DB53DFEBC6B04AF1C~-1~YAAQ3rqaTkaU1qaBAQAAY7AxzQj3k2CHyLsZtb7bF1PKj5LEpM9g9ipqiKDxt4vcT8GxbVTnPSw7YKXtDHlJWB3/Nx4p5xocyGZGm3ZHHi8ObAuxM2Hw/9N4wjODezQYojXrj3SfLJyESIGr04owOzRSlGcqL1qV2WruD33BgLAAfvbdEU5vKurK3f2tB/e7Ddkx4zWsC2CEMBiZRMOd79fNDJHOBWeRfM7dZdEd/w14SegvuPYLohWmSU/2h7aBpuKHzRqnsVO9jn3bptKAcQ3JrfvfyL24AiWnVNy1j3K2/zsXRUWtMIcttkQoeyXpU6WmTDlCvsST/VQerPEZnkSKHh3Fxl/NFOwKtFHYnw6NIT+tZc2T/xLd7Nk=~-1~-1~-1; bm_sz=DE8EC8F4F58C8492ACEAC600F3250DFD~YAAQ3rqaTkeU1qaBAQAAY7AxzRDMLrtaK9WKA+s25XsJvAZP/94+nSsuvfpyOmlpeDNLwFnahcfho8KytYiXeGT+4+QHlNXuhBlDEM7Z6clT8cNJIW5CIrv84gg/QpMqPiEypg3kWI7tufszraR+9Vr5CDMxtbee+txNGhNOx1M3fO4ApMHVWr8DF9h4Kq+Yk03yoeDw7F7vKllzDqZ5zcN1IS2R88W3YNXMVbsC0Pb/9/wW1gP0DIa+YBx/OZxYNmReLFMsKppHC9757bjO7/cm4rb9C5AsLGEqRTQnY2ltyEY=~3486276~4469815; tt_webid=7116782218697541122; part=stable; csrftoken=Cn6IYKqlfEVbPqg1v2eHScJfR5D4Gq8j; lang_type=en; tta_attr_id=0.1657004998.7116782276033118210; tta_attr_id_mirror=0.1657004998.7116782276033118210; pre_country=UA; tt_webid=7116782218697541122; ac_csrftoken=44b65ef36cb14dcf859a68aba8c1f876; passport_csrf_token=f71f50e3a12deeda31d05fdc588e89c1; passport_csrf_token_default=f71f50e3a12deeda31d05fdc588e89c1; sso_auth_status_ads=faa14f23bafc9275dcc802fa7edb9c60; sso_auth_status_ss_ads=faa14f23bafc9275dcc802fa7edb9c60; sso_uid_tt_ads=81e9c9bf213cd2ae8740398ddadc60b9b2976424b879e126ae528fd9f48ed272; sso_uid_tt_ss_ads=81e9c9bf213cd2ae8740398ddadc60b9b2976424b879e126ae528fd9f48ed272; toutiao_sso_user_ads=694ac0977e70056f761bb54473dd7660; toutiao_sso_user_ss_ads=694ac0977e70056f761bb54473dd7660; sid_ucp_sso_v1_ads=1.0.0-KDA1OTk5NTZmZThmZGVkY2ViMjUzMzA4ZWFlOGM0NWYwYmFhNGQ1Y2QKIAiCiIyyl53p4WIQm8iPlgYYrwwgDDCayI-WBjgBQOwHEAEaA3NnMSIgNjk0YWMwOTc3ZTcwMDU2Zjc2MWJiNTQ0NzNkZDc2NjA; ssid_ucp_sso_v1_ads=1.0.0-KDA1OTk5NTZmZThmZGVkY2ViMjUzMzA4ZWFlOGM0NWYwYmFhNGQ1Y2QKIAiCiIyyl53p4WIQm8iPlgYYrwwgDDCayI-WBjgBQOwHEAEaA3NnMSIgNjk0YWMwOTc3ZTcwMDU2Zjc2MWJiNTQ0NzNkZDc2NjA; odin_tt=4462ebd2eab7a69128f2c52ebfd86a1f056e39cc309abd290b7de25877a00f2e6677d838761efdbfa38f183f6ead2e1f3674d247642ba8552b77bce110b05f6c; passport_auth_status_ads=83bfa636629ed3645967f9ec4491cf47%2C; passport_auth_status_ss_ads=83bfa636629ed3645967f9ec4491cf47%2C; sid_guard_ads=3b35a6084cc94c4151426acf1336282f%7C1657005084%7C863999%7CFri%2C+15-Jul-2022+07%3A11%3A23+GMT; uid_tt_ads=306102a62a0692b42600cdfa1da34d68a91da2ea2fc3eb247d6ac3e9b4bfd88e; uid_tt_ss_ads=306102a62a0692b42600cdfa1da34d68a91da2ea2fc3eb247d6ac3e9b4bfd88e; sid_tt_ads=3b35a6084cc94c4151426acf1336282f; sessionid_ads=3b35a6084cc94c4151426acf1336282f; sessionid_ss_ads=3b35a6084cc94c4151426acf1336282f; sid_ucp_v1_ads=1.0.0-KDBmOTU4MGU0YjQ1ZjJkY2Q0OWJhMTFjOGE0Y2U2ZTY3OTVjODJhY2EKGgiCiIyyl53p4WIQnMiPlgYYrwwgDDgBQOwHEAEaA3NnMSIgM2IzNWE2MDg0Y2M5NGM0MTUxNDI2YWNmMTMzNjI4MmY; ssid_ucp_v1_ads=1.0.0-KDBmOTU4MGU0YjQ1ZjJkY2Q0OWJhMTFjOGE0Y2U2ZTY3OTVjODJhY2EKGgiCiIyyl53p4WIQnMiPlgYYrwwgDDgBQOwHEAEaA3NnMSIgM2IzNWE2MDg0Y2M5NGM0MTUxNDI2YWNmMTMzNjI4MmY; msToken=Zegwr1KK4lA4riWxXu83xPvNQI-x5xOjJbjSI31a59XGpGEf8ck_GWy9S-BCNinKiCcBACDVGEmHr-mcIjhrxFsYOt1g_W9MvdtH97t6yb7F5bOHJAKl-QeWttVqqoFvNel0H_dUrnG-uJw=; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}; MONITOR_WEB_ID=7116783925497790465; ttwid=1%7CVwed9aInstc1Ndj4F419aLjYM0i2gI0_0w_Yp-dd5oU%7C1657005573%7Cd4afe21a05631012931a9acbd00988161bcb4486950a47e88187039af632d6d3; lang=en; _tea_utm_cache_2777=undefined; store-idc=maliva; store-country-code=ua; msToken=4WwrbWQhk5i0pGyWTdkXDxZzZTJHIHwXC3e1wmcLkvbd2-zdoxyBf_R2n-DpkDjL_zyobC_6UXPYAlJ6O08Iy65hPwTpZv0m2SkzK1fYJCGFro-hBVGHSbApXHu1x8tbOwqPBA==',
        }
        # json_data = json_data_generate
#         json_data = {
#     'state': 5551752,
#     'county': -1,
#     'city': -1,
#     'payment': 2,
#     'tax_type': 3,
#     'tax_value': {},
# }
                #{"address_detail":"dsfsdf","state":325361,"county":-1,"city":308998,"post_code":"435345","tax_type":11,"tax_value":{}, "payment":2} #,

        json_data ={ 'risk_info': {
            'cookie_enabled': 'true',
            'screen_width': 1366,
            'screen_height': 768,
            'browser_language': 'es-ES',
            'browser_platform': 'Win32',
            'browser_name': 'Mozilla',
            'browser_version': a.USER_AGENT,
            'browser_online': 'true',
            'timezone_name': 'Europe/Kiev',
            'duration': 187756,
        },
        'description': 'https://dfzzsddcxvd.com',
        'company': 'Agaffdssdsdxcvsddfreeewer',
        'second_industry': '292103',
        'state': 691650,
        'post_code': '22234',
        'agency': 'true',
        'address_detail': 'cxv 12',
        'qualification_url_secret': [],
        'qualification_new_secret': [],
        'qualification_reject_reasons': {},
        'tax_type': '3',
        'tax_value': {},
        'payment': 2,
    }
        #json_data = {"risk_info":{"cookie_enabled":True,"screen_width":1366,"screen_height":768,"browser_language":"uk-UA","browser_platform":"Win32","browser_name":"Mozilla","browser_version":"5.0 (Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4144.59 Mobile/15E148 Safari/602.1","browser_online":True,"timezone_name":"Europe/Kiev","duration":97324},"description":"https://gasol.eu","company":"Gres","second_industry":"291308","state":3457415,"city":3460101,"post_code":"","agency":False,"address_detail":"onffto 23","qualification_url_secret":[],"qualification_new_secret":[],"qualification_reject_reasons":{},"tax_type":"11","tax_value":{},"payment":"2"}
       # json_data = {"risk_info":{"cookie_enabled":"true","screen_width":"1366","screen_height":"768","browser_language":"uk-UA","browser_platform":"Win32","browser_name":"Mozilla","browser_version":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36","browser_online":"true","timezone_name":"Europe/Kiev","duration":"97324"},"description":"zz.com","company":"Magnda","second_industry":"290506","state":"3457415","city":"3460101","post_code":"3244234","agency":"true","address_detail":"Maonto 23","qualification_url_secret":[],"qualification_new_secret":[],"qualification_reject_reasons":{},"tax_type":"3","tax_value":{},"payment":"2"}
        #BR
#         json_data = {
#     'address_detail': 'ASDASD',
#     'state': 3407762,
#     'county': -1,
#     'city': 6319494,
#     'post_code': '345345',
#     'payment': 2,
#     'tax_type': 3,
#     'tax_value': {
#         'cpnj': '13.813.352/0001-08',
#     },
# }
        
        
        response = requests.post('https://ads.tiktok.com/api/v1/self-serve/adv-account/update_account_first_time/?aadvid=' +
                                 id+'&msToken=&X-Bogus=&_signature=', cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY)
        # print(response.json())
        return response.json()

    def ticket(self):
        cookies = self.COOKIES

        headers = {
            'Host': 'ads.tiktok.com',
            'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'ru',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            # 'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'csrftoken=APcdQuzPjEIr5SxkhUSl0D6ZZHxBujae; tta_attr_id=0.1657785239.7120133387309826050; tta_attr_id_mirror=0.1657785239.7120133387309826050; pre_country=DE; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}; passport_csrf_token=5274d4c1f85a9ad13d5751d961c5238c; passport_csrf_token_default=5274d4c1f85a9ad13d5751d961c5238c; store-country-code=nl; store-idc=maliva; _gcl_au=1.1.111872515.1658558611; _ga=GA1.2.558692242.1658558612; _gid=GA1.2.106132314.1658558612; _gat_UA-143770054-3=1; tta_attr_ga_cid=558692242.1658558612; _rdt_uuid=1658558612109.510f3289-4abc-45fb-a8c9-2e93e9aea428; _fbp=fb.1.1658558624965.671577458; _tt_enable_cookie=1; _ttp=2CKkNu7L0Vsz7QZgB94ndNsOh1M; _hjSessionUser_2525957=eyJpZCI6ImIwNGNmOTgyLWM3ZmYtNTQ5YS04ZjdiLWMwOGVkNDJiN2JlMSIsImNyZWF0ZWQiOjE2NTg1NTg2MjUyOTMsImV4aXN0aW5nIjp0cnVlfQ==; tt_csrf_token=B8Ak81zX-NZKsO4LeVMYzA1UBTdyrELl3H-A; lang_type=ru; lang=ru; gftoken=MjU3MDc0MTIyM3wxNjU5ODY0OTQwNDJ8fDAGBgYGBgY; i18next=ru; tt_webid=7130559518644405762; tt_webid=7130559518644405762; lang_type_ttp=ru; s_v_web_id=verify_l6w9bwxa_gVEqHmnl_IQ7R_4N0M_BPeq_OmSuKuHIav40; d_ticket_ads=675fcb4b18afad6b0c9f594dd7e97aa09e2f3; sso_auth_status_ads=d7b6db24a8d90b9d143f1ffdd432185a; sso_auth_status_ss_ads=d7b6db24a8d90b9d143f1ffdd432185a; sso_uid_tt_ads=de5e551bd4e59e46a11563cfe144877bfd7f96ad3acde1d30a27bca8a76fb8e1; sso_uid_tt_ss_ads=de5e551bd4e59e46a11563cfe144877bfd7f96ad3acde1d30a27bca8a76fb8e1; toutiao_sso_user_ads=909f85d33d9dc272a0b6d9d7466a2d4f; toutiao_sso_user_ss_ads=909f85d33d9dc272a0b6d9d7466a2d4f; sid_ucp_sso_v1_ads=1.0.0-KDgwYjQ2OTllYjg1NzRkZDYyODZmYTViYjcxZGYzZDFlZmIwZWQwM2IKIAiBiIOE_Yjd52IQhMnulwYYrwwgDDDbl7-WBjgBQOsHEAEaA3NnMSIgOTA5Zjg1ZDMzZDlkYzI3MmEwYjZkOWQ3NDY2YTJkNGY; ssid_ucp_sso_v1_ads=1.0.0-KDgwYjQ2OTllYjg1NzRkZDYyODZmYTViYjcxZGYzZDFlZmIwZWQwM2IKIAiBiIOE_Yjd52IQhMnulwYYrwwgDDDbl7-WBjgBQOsHEAEaA3NnMSIgOTA5Zjg1ZDMzZDlkYzI3MmEwYjZkOWQ3NDY2YTJkNGY; current_tcpp_partner_id=; msToken=Gt8yp0XSY3qfz1l6u-ur8Lf3bWB0X7ik0kkin3umT37eAhAhWGTHmyhdsKNqxrb8rZ4pVClzHEt9hzAah5mlPIeMPCCUkXr4e0jOZ04x5ryY6-oaEFpbW5ky1Mm-fTa62wlF8TC9gvXQKfIn; odin_tt=979df5d0984bbde402cd490eaa4c68fd3251fbc78cfdd592d16ddc1b1a67553af9730aac622243413bfede05d4a0bf3027155fb33c547c4754131061b0c3aca5; passport_auth_status_ads=f25fc4e72a8712d13eec3cb25a3c02fd%2C5ff2fc2c1531b5ab3661497a303fc51b; passport_auth_status_ss_ads=f25fc4e72a8712d13eec3cb25a3c02fd%2C5ff2fc2c1531b5ab3661497a303fc51b; uid_tt_ads=c76ea20839bb8aacd414e836fddbf3bcb5ded520c414ee37df3fb3f84356043d; uid_tt_ss_ads=c76ea20839bb8aacd414e836fddbf3bcb5ded520c414ee37df3fb3f84356043d; sid_tt_ads=3f5634e2be61118463db658fc2e1c2ba; sessionid_ads=3f5634e2be61118463db658fc2e1c2ba; sessionid_ss_ads=3f5634e2be61118463db658fc2e1c2ba; _gat_UA-143770054-2=1; _tea_utm_cache_4031=undefined; MONITOR_WEB_ID=7133170624133922817; store-country-code-src=uid; part=stable; ttwid=1%7CDBMn9b6w3m6TOj7QSuB98DoOstrFom-ekKtOk-AutYU%7C1661093970%7Cc7d405ce53f34ccc9b6043ce15450c584eddc2d1130c08dd3f900fbf618b3d71; _tea_utm_cache_1583={%22creative_id%22:1741866731558962}; _tea_utm_cache_4697={%22creative_id%22:1741866731558962}; _tea_utm_cache_224013={%22creative_id%22:1741866731558962}; _tea_utm_cache_345918={%22creative_id%22:1741866731558962}; _uetsid=f562cf40216111edb567459931893252; _uetvid=c4c932400a5211ed952e394105e20bc2; msToken=l5n0IjciRnsEaGguKl17_hz4TBWbqsoBuSgkEyH8vc-Stt0pMqxPpeWHa2anrYLcnylvxgHERbHG1Pnszew34Be_uzDYC3xm9TQoV416lvgHNzNDK6S1; _abck=EDFE101660A78A9D81D91C45CF4C331A~-1~YAAQ1bqaTuytkryCAQAA2+3vzwjpCAXjQj6a3gBxUNW8JuEiPGWoxnXVHcZSzF9I7KoV6+ZQMFftKk6II/Jf4cuO1cWG1molHIf/ZMtepcAFy8d5r4FT2cYJC1xF8Ud+6pG+te5lPVCymkhIhUDqjlR8bt8zvl3LExhfDe6p4S52KeP692qZT3WpnOK54yIfUjExYAqjRKDTAM8oMionXqND5pQihe+msLZFH0euWg/KbUHIKiFk56f2sXzfin4HPk+kyADR2O3eIB4joRIxrr8oyb9B4VtrwDrRc+2sWrfvHlLbE+hBw18HCeS20LXOopEphxrLO2PnNehXW4v+8bjKbkxxvt9bcf9Wm3r103mS8IYDWef56ABzl/MBt1xFDZdciOXMCy4o/w==~-1~-1~-1; bm_sz=6455EA0752A925799F6136284B993EC7~YAAQ1bqaTu2tkryCAQAA2+3vzxCnPEqIE7XFtFzvDrrReLJbWr2Eu2Dra+sQvhnGQhoJ4sCG0dGH4nUXFiY5pMuHqJhpZxOno5XZMiE842xUVCwWDlOWR1btZCOIGwU2yDj8j5LBQK/KNAeyTEbkBibq0hWd8C7tvWNgZXl0DVm0FKNecmyEierUabssV1X+sfduym+uYjzbym588roHJcGZNENrhmrYbMBfjqY2MP2iHaSC8GINfkCa63Fp10BtBs2UrkrD10qrBlsQB6tUuFiOWKd9Z1lM2POEEGoniz47DFk=~3556665~3552567; sid_guard_ads=3f5634e2be61118463db658fc2e1c2ba%7C1661345986%7C864000%7CSat%2C+03-Sep-2022+12%3A59%3A46+GMT; sid_ucp_v1_ads=1.0.0-KDY1OGUwYmE3ZmMzZTU2Y2FiOGE0Mzc3MDJmOTc2ZmRhZGI4NWZjNWYKGgiBiIOE_Yjd52IQwsGYmAYYrwwgDDgBQOsHEAEaA3NnMSIgM2Y1NjM0ZTJiZTYxMTE4NDYzZGI2NThmYzJlMWMyYmE; ssid_ucp_v1_ads=1.0.0-KDY1OGUwYmE3ZmMzZTU2Y2FiOGE0Mzc3MDJmOTc2ZmRhZGI4NWZjNWYKGgiBiIOE_Yjd52IQwsGYmAYYrwwgDDgBQOsHEAEaA3NnMSIgM2Y1NjM0ZTJiZTYxMTE4NDYzZGI2NThmYzJlMWMyYmE',
        }

        params = {
            'aid': '1583',
        }

        response = requests.get('https://ads.tiktok.com/passport/auth/login_authorize/',
                                params=params, cookies=cookies, headers=headers, proxies=self.PROXY)
        print(response.json())
        token = response.json()['data']['token']
        print(token)
        return str(token)

    def nonce(self, vcpo):
        cookies = self.COOKIES

        headers = {
            'Host': 'ads.tiktok.com',
            'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'ru',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            # 'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'csrftoken=APcdQuzPjEIr5SxkhUSl0D6ZZHxBujae; tta_attr_id=0.1657785239.7120133387309826050; tta_attr_id_mirror=0.1657785239.7120133387309826050; pre_country=DE; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}; passport_csrf_token=5274d4c1f85a9ad13d5751d961c5238c; passport_csrf_token_default=5274d4c1f85a9ad13d5751d961c5238c; store-country-code=nl; store-idc=maliva; _gcl_au=1.1.111872515.1658558611; _ga=GA1.2.558692242.1658558612; _gid=GA1.2.106132314.1658558612; _gat_UA-143770054-3=1; tta_attr_ga_cid=558692242.1658558612; _rdt_uuid=1658558612109.510f3289-4abc-45fb-a8c9-2e93e9aea428; _fbp=fb.1.1658558624965.671577458; _tt_enable_cookie=1; _ttp=2CKkNu7L0Vsz7QZgB94ndNsOh1M; _hjSessionUser_2525957=eyJpZCI6ImIwNGNmOTgyLWM3ZmYtNTQ5YS04ZjdiLWMwOGVkNDJiN2JlMSIsImNyZWF0ZWQiOjE2NTg1NTg2MjUyOTMsImV4aXN0aW5nIjp0cnVlfQ==; tt_csrf_token=B8Ak81zX-NZKsO4LeVMYzA1UBTdyrELl3H-A; lang_type=ru; lang=ru; gftoken=MjU3MDc0MTIyM3wxNjU5ODY0OTQwNDJ8fDAGBgYGBgY; i18next=ru; tt_webid=7130559518644405762; tt_webid=7130559518644405762; lang_type_ttp=ru; s_v_web_id=verify_l6w9bwxa_gVEqHmnl_IQ7R_4N0M_BPeq_OmSuKuHIav40; d_ticket_ads=675fcb4b18afad6b0c9f594dd7e97aa09e2f3; sso_auth_status_ads=d7b6db24a8d90b9d143f1ffdd432185a; sso_auth_status_ss_ads=d7b6db24a8d90b9d143f1ffdd432185a; sso_uid_tt_ads=de5e551bd4e59e46a11563cfe144877bfd7f96ad3acde1d30a27bca8a76fb8e1; sso_uid_tt_ss_ads=de5e551bd4e59e46a11563cfe144877bfd7f96ad3acde1d30a27bca8a76fb8e1; toutiao_sso_user_ads=909f85d33d9dc272a0b6d9d7466a2d4f; toutiao_sso_user_ss_ads=909f85d33d9dc272a0b6d9d7466a2d4f; sid_ucp_sso_v1_ads=1.0.0-KDgwYjQ2OTllYjg1NzRkZDYyODZmYTViYjcxZGYzZDFlZmIwZWQwM2IKIAiBiIOE_Yjd52IQhMnulwYYrwwgDDDbl7-WBjgBQOsHEAEaA3NnMSIgOTA5Zjg1ZDMzZDlkYzI3MmEwYjZkOWQ3NDY2YTJkNGY; ssid_ucp_sso_v1_ads=1.0.0-KDgwYjQ2OTllYjg1NzRkZDYyODZmYTViYjcxZGYzZDFlZmIwZWQwM2IKIAiBiIOE_Yjd52IQhMnulwYYrwwgDDDbl7-WBjgBQOsHEAEaA3NnMSIgOTA5Zjg1ZDMzZDlkYzI3MmEwYjZkOWQ3NDY2YTJkNGY; current_tcpp_partner_id=; msToken=Gt8yp0XSY3qfz1l6u-ur8Lf3bWB0X7ik0kkin3umT37eAhAhWGTHmyhdsKNqxrb8rZ4pVClzHEt9hzAah5mlPIeMPCCUkXr4e0jOZ04x5ryY6-oaEFpbW5ky1Mm-fTa62wlF8TC9gvXQKfIn; odin_tt=979df5d0984bbde402cd490eaa4c68fd3251fbc78cfdd592d16ddc1b1a67553af9730aac622243413bfede05d4a0bf3027155fb33c547c4754131061b0c3aca5; passport_auth_status_ads=f25fc4e72a8712d13eec3cb25a3c02fd%2C5ff2fc2c1531b5ab3661497a303fc51b; passport_auth_status_ss_ads=f25fc4e72a8712d13eec3cb25a3c02fd%2C5ff2fc2c1531b5ab3661497a303fc51b; uid_tt_ads=c76ea20839bb8aacd414e836fddbf3bcb5ded520c414ee37df3fb3f84356043d; uid_tt_ss_ads=c76ea20839bb8aacd414e836fddbf3bcb5ded520c414ee37df3fb3f84356043d; sid_tt_ads=3f5634e2be61118463db658fc2e1c2ba; sessionid_ads=3f5634e2be61118463db658fc2e1c2ba; sessionid_ss_ads=3f5634e2be61118463db658fc2e1c2ba; _gat_UA-143770054-2=1; _tea_utm_cache_4031=undefined; MONITOR_WEB_ID=7133170624133922817; store-country-code-src=uid; part=stable; _tea_utm_cache_1583={%22creative_id%22:1741866731558962}; _tea_utm_cache_4697={%22creative_id%22:1741866731558962}; _tea_utm_cache_224013={%22creative_id%22:1741866731558962}; _tea_utm_cache_345918={%22creative_id%22:1741866731558962}; sid_guard_ads=3f5634e2be61118463db658fc2e1c2ba%7C1661345986%7C864000%7CSat%2C+03-Sep-2022+12%3A59%3A46+GMT; sid_ucp_v1_ads=1.0.0-KDY1OGUwYmE3ZmMzZTU2Y2FiOGE0Mzc3MDJmOTc2ZmRhZGI4NWZjNWYKGgiBiIOE_Yjd52IQwsGYmAYYrwwgDDgBQOsHEAEaA3NnMSIgM2Y1NjM0ZTJiZTYxMTE4NDYzZGI2NThmYzJlMWMyYmE; ssid_ucp_v1_ads=1.0.0-KDY1OGUwYmE3ZmMzZTU2Y2FiOGE0Mzc3MDJmOTc2ZmRhZGI4NWZjNWYKGgiBiIOE_Yjd52IQwsGYmAYYrwwgDDgBQOsHEAEaA3NnMSIgM2Y1NjM0ZTJiZTYxMTE4NDYzZGI2NThmYzJlMWMyYmE; ttwid=1%7CDBMn9b6w3m6TOj7QSuB98DoOstrFom-ekKtOk-AutYU%7C1661359305%7Cac07b39d06d9ed5a001ef07b7b7b4d55084dab586d59c011bc7b6d94a224dc8d; _abck=EDFE101660A78A9D81D91C45CF4C331A~-1~YAAQ1bqaTuwvlryCAQAAqxH80QjAVxgFB1baPHcq9uImwh4UIxulz5SZU9Dy74tPP6k1o715CtlJYO/Cah3Tgx3DQRWNcNfdZdv27rLGHCNTDxbQZkQz6pE6M3yba6V3mSahhmE6iZdL+GW+9LGqMLzw4AYFxRLoe8epV7aOWROK3V6RmBdFAO3Dcc+Yk86MboXlqztCHeGkOkmJ0E3tYdkzCPhCAR10huXzLe1mi8KBsaFZx1QHkgMj75CLCmhOLk9fHLl5RaAI0S1sKBVHhsGQ2Jz77BR6KJ8qJxuRl3oZrarveG38bMPhUt6hy3AGhlayZHdThoqKwSEGngwy8JFObLLaEpTlXVWHO6iWAsIo/HNfQIUt93TYTiF+9GP/orltbQfw5a5xOA==~-1~-1~-1; bm_sz=70762441CCD34EE353896ACC5E49B361~YAAQ1bqaTu0vlryCAQAAqxH80RDCBmgDGRP/1js+opbIMJrhWWxcyuN92t3MYoiZLqMmi0UpSncETlGeb07RbcgpUwCqquxkAuX80ua1Lhtftb096qAGRoKh6qXdK1QMhN4rBuDYuRRlO2luwJVLn5wSTELb/ONj7038U31xYCou0R8KITazo6vUMr7KGLsA05BdrCB98WW+uuey1UGm7k0Lt6EqDctIgxekNwBrG3ICpg7YkjL4zc/i7CBUz7EHjK38R+rovqvJ374a9HRZInKkBShQqYUhK5wiX+g9VOxSUMI=~3552070~4338229; _hjSession_2525957=eyJpZCI6IjIxZWE0NTA1LWY5MzYtNDRjMi1iOWFhLTkxMzc2NWQyOWZlYSIsImNyZWF0ZWQiOjE2NjEzOTAwNjcwMjQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; msToken=5eku0oCnDXEu99xiD5PsthsB9zPNr2i3RnH7tC5ycaf8KSQrzGVI0m5Dy1hmDTGepL4dzNkQwZXM4w71GNSqlmr_lC2RTAJyc2MmOLOZShijherlK8uU1F2PJBuNamB_VGntJ3GrZ5cKE5AF; _uetsid=f562cf40216111edb567459931893252; _uetvid=c4c932400a5211ed952e394105e20bc2',
        }

        params = {
            'appId': '1583',
            'token': str(vcpo),
        }

        response = requests.get('https://ads.tiktok.com/upay/i18n/card/pipo/bind/params',
                                params=params, cookies=cookies, headers=headers, proxies=self.PROXY)
        nonce = response.json()['data']['nonce']
        print(nonce)
        return str(nonce)

    def cardId(self, vcpo, id):
        cookies = self.COOKIES

        headers = {
            'Host': 'ads.tiktok.com',
            # 'Content-Length': '1872',
            'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Accept-Language': 'ru',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': a.USER_AGENT,
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Bizaccountid': id,
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            # 'Accept-Encoding': 'gzip, deflate',
            'Connection': 'close',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'csrftoken=APcdQuzPjEIr5SxkhUSl0D6ZZHxBujae; tta_attr_id=0.1657785239.7120133387309826050; tta_attr_id_mirror=0.1657785239.7120133387309826050; pre_country=DE; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}; passport_csrf_token=5274d4c1f85a9ad13d5751d961c5238c; passport_csrf_token_default=5274d4c1f85a9ad13d5751d961c5238c; store-country-code=nl; store-idc=maliva; _gcl_au=1.1.111872515.1658558611; _ga=GA1.2.558692242.1658558612; _gid=GA1.2.106132314.1658558612; _gat_UA-143770054-3=1; tta_attr_ga_cid=558692242.1658558612; _rdt_uuid=1658558612109.510f3289-4abc-45fb-a8c9-2e93e9aea428; _fbp=fb.1.1658558624965.671577458; _tt_enable_cookie=1; _ttp=2CKkNu7L0Vsz7QZgB94ndNsOh1M; _hjSessionUser_2525957=eyJpZCI6ImIwNGNmOTgyLWM3ZmYtNTQ5YS04ZjdiLWMwOGVkNDJiN2JlMSIsImNyZWF0ZWQiOjE2NTg1NTg2MjUyOTMsImV4aXN0aW5nIjp0cnVlfQ==; tt_csrf_token=B8Ak81zX-NZKsO4LeVMYzA1UBTdyrELl3H-A; lang_type=ru; lang=ru; gftoken=MjU3MDc0MTIyM3wxNjU5ODY0OTQwNDJ8fDAGBgYGBgY; i18next=ru; tt_webid=7130559518644405762; tt_webid=7130559518644405762; lang_type_ttp=ru; s_v_web_id=verify_l6w9bwxa_gVEqHmnl_IQ7R_4N0M_BPeq_OmSuKuHIav40; d_ticket_ads=675fcb4b18afad6b0c9f594dd7e97aa09e2f3; sso_auth_status_ads=d7b6db24a8d90b9d143f1ffdd432185a; sso_auth_status_ss_ads=d7b6db24a8d90b9d143f1ffdd432185a; sso_uid_tt_ads=de5e551bd4e59e46a11563cfe144877bfd7f96ad3acde1d30a27bca8a76fb8e1; sso_uid_tt_ss_ads=de5e551bd4e59e46a11563cfe144877bfd7f96ad3acde1d30a27bca8a76fb8e1; toutiao_sso_user_ads=909f85d33d9dc272a0b6d9d7466a2d4f; toutiao_sso_user_ss_ads=909f85d33d9dc272a0b6d9d7466a2d4f; sid_ucp_sso_v1_ads=1.0.0-KDgwYjQ2OTllYjg1NzRkZDYyODZmYTViYjcxZGYzZDFlZmIwZWQwM2IKIAiBiIOE_Yjd52IQhMnulwYYrwwgDDDbl7-WBjgBQOsHEAEaA3NnMSIgOTA5Zjg1ZDMzZDlkYzI3MmEwYjZkOWQ3NDY2YTJkNGY; ssid_ucp_sso_v1_ads=1.0.0-KDgwYjQ2OTllYjg1NzRkZDYyODZmYTViYjcxZGYzZDFlZmIwZWQwM2IKIAiBiIOE_Yjd52IQhMnulwYYrwwgDDDbl7-WBjgBQOsHEAEaA3NnMSIgOTA5Zjg1ZDMzZDlkYzI3MmEwYjZkOWQ3NDY2YTJkNGY; current_tcpp_partner_id=; _tea_utm_cache_3820=undefined; msToken=Gt8yp0XSY3qfz1l6u-ur8Lf3bWB0X7ik0kkin3umT37eAhAhWGTHmyhdsKNqxrb8rZ4pVClzHEt9hzAah5mlPIeMPCCUkXr4e0jOZ04x5ryY6-oaEFpbW5ky1Mm-fTa62wlF8TC9gvXQKfIn; odin_tt=979df5d0984bbde402cd490eaa4c68fd3251fbc78cfdd592d16ddc1b1a67553af9730aac622243413bfede05d4a0bf3027155fb33c547c4754131061b0c3aca5; passport_auth_status_ads=f25fc4e72a8712d13eec3cb25a3c02fd%2C5ff2fc2c1531b5ab3661497a303fc51b; passport_auth_status_ss_ads=f25fc4e72a8712d13eec3cb25a3c02fd%2C5ff2fc2c1531b5ab3661497a303fc51b; uid_tt_ads=c76ea20839bb8aacd414e836fddbf3bcb5ded520c414ee37df3fb3f84356043d; uid_tt_ss_ads=c76ea20839bb8aacd414e836fddbf3bcb5ded520c414ee37df3fb3f84356043d; sid_tt_ads=3f5634e2be61118463db658fc2e1c2ba; sessionid_ads=3f5634e2be61118463db658fc2e1c2ba; sessionid_ss_ads=3f5634e2be61118463db658fc2e1c2ba; sid_ucp_v1_ads=1.0.0-KDM0MmY2ZTcxNzFhZDJjNDk2MDIxZTNhZTliNWRiOWVkNzFlNGQyZDEKGgiBiIOE_Yjd52IQmID4lwYYrwwgDDgBQOsHEAEaA3NnMSIgM2Y1NjM0ZTJiZTYxMTE4NDYzZGI2NThmYzJlMWMyYmE; ssid_ucp_v1_ads=1.0.0-KDM0MmY2ZTcxNzFhZDJjNDk2MDIxZTNhZTliNWRiOWVkNzFlNGQyZDEKGgiBiIOE_Yjd52IQmID4lwYYrwwgDDgBQOsHEAEaA3NnMSIgM2Y1NjM0ZTJiZTYxMTE4NDYzZGI2NThmYzJlMWMyYmE; _gat_UA-143770054-2=1; _tea_utm_cache_4031=undefined; MONITOR_WEB_ID=7133170624133922817; store-country-code-src=uid; sid_guard_ads=3f5634e2be61118463db658fc2e1c2ba%7C1661093959%7C790727%7CTue%2C+30-Aug-2022+18%3A38%3A06+GMT; part=stable; ttwid=1%7CDBMn9b6w3m6TOj7QSuB98DoOstrFom-ekKtOk-AutYU%7C1661093970%7Cc7d405ce53f34ccc9b6043ce15450c584eddc2d1130c08dd3f900fbf618b3d71; _tea_utm_cache_1583={%22creative_id%22:1741866731558962}; _tea_utm_cache_4697={%22creative_id%22:1741866731558962}; _tea_utm_cache_224013={%22creative_id%22:1741866731558962}; _tea_utm_cache_345918={%22creative_id%22:1741866731558962}; _abck=EDFE101660A78A9D81D91C45CF4C331A~-1~YAAQ3bqaTkGqG5SCAQAAkzqnywgLB8DLc4fJ6Yz59ILwfRgD3HSuQCZIL1hd0NLQ5L/frmcVf/fDxXNprOrtumyf05XdmeRGAqBK6tQUEX9w8M3X5evM91IV6e2RAMCeiA0Vne2boNftS5qXHiCGj51S9+PvHseIDp6W/m4P90yqsC5UsVUTf1Ovz1DoqpFmrj0TiBAVPwYRAF2v+X6pX2BImZ40xEQ/WtJRMzSZ/FWrSfuQMcC+q2sT/ma0lPqZo2HVWR2EwtOUdvvR/nxy9MziALA5DGjd3Iz/om4yxADDqYFUpMJLYwrPCYG0h7UOO9olyHVDBDVJpuZVGEJALuq5U6Du+CfcCutNT8uEETP/zHMaDpGAqFLfDV7PKxaqLgrPjD1UbaNzcw==~-1~-1~-1; bm_sz=1DB307BA3C16D8C75BAC24558E4C57D5~YAAQ3bqaTkKqG5SCAQAAkzqnyxCwI+sckQzSTMAK3tsAARDqaMLzr9OV6D6H3a2ZQcUuvPpDw4zNqTfqJHCFQajVixqp95pHwovA8+9s9bpcrdyUUL6EurC0zw5yPrnCFG7XwDA/IMA9QtoJLlkDoxkor3FknwzYhRljvM6a4SgVauaTFFCFYhxJ5iUh2U5G0KbaPZzj49DkejTd9QYmZtT9CjJeHxu2ao9Xea78Gd4BYC+AW93wxfjrHiaQLMOd9qsy7VE3i56D37rMqqhM/SpzMewPqvCrScKbiFY4s8K5n9g=~3621955~3619123; _hjSession_2525957=eyJpZCI6IjAzZGI0MDIzLTcwMWMtNDFlZC1hYTNjLTkzYjRhNTE2OGFlYiIsImNyZWF0ZWQiOjE2NjEyODM5NTExMTcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _uetsid=f562cf40216111edb567459931893252; _uetvid=c4c932400a5211ed952e394105e20bc2; msToken=ij2IgfnvPXlG15-G3cVNTGIXtvdQ6mDLOfjkoycVjE_w-NTHqJQeBjIs9IxyYha93kPS1qFvatsMo5Yed_ooTqidw1XKG9vzRCpvm8c7FDbKzbp8PG5zDXeuvPAh5yuuJc0amViQ8o5kwaEu',
        }

        json_data = {
            'token': str(vcpo),
            'returnUrl': 'https://ads.tiktok.com/wpay/oversea/result?invokerID=upay_f67efed623c24dfgdfg192ee4791d777fffb045c885e40&from=createInManager&uniqueId=118dfgdfg389c6-ff3c-7282-825c-5f233555cd49_'+id,
            'terminalEquip': 4,
            'riskInfo': '',
            'riskAmount': '',
            'payWay': 99,
            'upaySessionId': '2938f251-sd02dfgdfgba-4b37-9d71asd8-42f72702f4_'+id,
            'refId': 'b2b543bc-f907-4503-8ecdsdf-asd15aa0a5f5_'+id,
            'supportRiskAmount': True,
            'paymentMethodId': 'asdasdfsdas_'+id,
        }

        response = requests.post('https://ads.tiktok.com/upay/i18n/card/bind',
                                 cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY)
        print(response.json())
        cardId = response.json()['data']['cardId']
        print(cardId)
        return str(cardId)

    def campaign_create(self, id):
        cookies = self.COOKIES
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,

            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+str(id),
            'Accept-Language': 'en-US,en',
        }
        json_data = {
            'budget_mode': -1,
            'buying_type': 1,
            'dedicate_type': 0,
            'ab_test': 0,
            'budget_optimize_switch': 0,
            'optimize_goal': 100,
            'objective_type': 1,
            'coming_source_type': 1,
            'budget': '',
            'industry_types': [],
            'smart_bid_type': 0,
            'roas_bid': 0,
            'deep_bid_type': 0,
            'campaign_name': 'Traffic20220509083522_'+str(id),
            'struct_version': 1,
            'risk_info': {
                # 'cookie_enabled': True,
                # 'screen_width': 1920,
                # 'screen_height': 1080,
                # 'browser_language': 'en-US',
                # 'browser_platform': 'Win32',
                # 'browser_name': 'Mozilla',
                # 'browser_version': a.USER_AGENT,
                # 'browser_online': True,
                # 'timezone_name': a.TIME_ZONE_NAME,
            }, }
        response = requests.post('https://ads.tiktok.com/api/v3/i18n/perf/campaign/create/?aadvid='+id+'&req_src=ad_creation&msToken=' +
                                 cookies['msToken']+'&_signature=_0AGqF93', cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        return str(response.json()['data']['campaign_id'])

    def campaign_create_conversion(self, id, nomer):
        cookies = self.COOKIES
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,

            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+str(id)+'&creation_type=create_new&temp_campaign_id=&temp_adgroup_id=',
            'Accept-Language': 'en-US,en',
        }
        json_data = {
            "budget_mode": -1,
            "buying_type": 1,
            "dedicate_type": 1,
            "ab_test": 0,
            "budget_optimize_switch": 0,
            "optimize_goal": 0,
            "objective_type": 3,
            "coming_source_type": 1,
            "budget": "",
            "industry_types": [],
            "smart_bid_type": 0,
            "roas_bid": 0,
            "deep_bid_type": 0,
            "campaign_name": "Conversion_"+str(id)+'_'+str(nomer),
            "struct_version": 1,
            "risk_info": {
                # "cookie_enabled": True,
                # "screen_width": 1366,
                # "screen_height": 768,
                # "browser_language": "uk-UA",
                # "browser_platform": "Win32",
                # "browser_name": "Mozilla",
                # "browser_version": a.USER_AGENT,
                # "browser_online": True,
                # "timezone_name": a.TIME_ZONE_NAME
            }
        }
        response = requests.post('https://ads.tiktok.com/api/v3/i18n/perf/campaign/create/?aadvid='+id+'&req_src=ad_creation&msToken=' +
                                 cookies['msToken']+'&_signature=_02B4O'+id, cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        print(str(response.json()))
        print(str(response.json()['data']['campaign_id']))
        return str(response.json()['data']['campaign_id'])

    def adgroup_create(self, id, campaign_id, pixel_d, name, country, external_action, start_time, budget):
        seed = random.randint(0, 2000)
        cookies = self.COOKIES
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,

            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+id+'&creation_type=create_new&temp_campaign_id=1732352314274&temp_adgroup_id=121025',
            'Accept-Language': 'en-US,en',
        }
        json_data = {
            'batch_info': [{
                 "num": 3,
            "name": name,
            }
            ],
            'base_info': {
                'struct_version': 1,
                'app_name': '',
                'target_device_version': 0,
                'ad_app_profile_page_type': 0,
                'shop_id': '0',
                'shop_authorized_bc': '0',
                'rf_notify_users': [],
                'flow_package_include': [],
                'action_days_v2': [],
                'roas_bid': 0,
                'targeting_expansion': {
                    'expansion_enabled': False,
                    'expansion_types': [],
                },
                'include_custom_actions': [],
                'source': '',
                'anti_discrimination': 0,
                'is_hfss': 0,
                'video_actions': [],
                'auto_open': 0,
                'ad_ref_pixel_id': pixel_d,
                'video_actions_v2': [],
                'spending_power': 2,
                'start_time': start_time,
                'ad_reach_frequency_buy_type': 0,
                'statistic_type': 0,
                'ad_tag_v2': [],
                'inventory_flow': [
                    3000,
                ],
                'external_action': external_action,  # 9, #5 click 9 download 96 comple
                'retargeting_tags': [],
                'cpa_auto': 0,
                'rf_predict_reach': 0,
                'action_scene': [
                    2,
                ],
                'num': 1,
                'name': name,
                'creative_display_mode': 0,
                'gender': 1,
                'first_frame': [],
                'ad_keywords': [],
                'operators_id': [],
                'ad_download_status': 1,
                'budget_mode': 0,
                'open_url': '',
                'campaign_id': campaign_id,
                'exclude_custom_actions': [],
                'frequency': 0,
                'pricing': 9,
                'device_type': 0,
                'cover_frequency_type': 0,
                'catalog_authorized_bc': '0',
                'android_osv': '22',
                 'language_list': [
                            'en',
                            'tr',
                         ],
                'flow_precision': 0,
                'frequency_schedule': 0,
                'ab_test_id': 0,
                'retargeting_audience_rule': {
                    'inclusions': None,
                    'exclusions': None,
                },
                'interest_keywords_i18n': [],
                'rf_estimate_key': '0',
                'end_time': '2032-10-20 21:52:58',
                'deep_cpabid': 0,
                'retargeting_tags_exclude': [],
                'brand_safety': 1,
                'shop_type': 0,
                'promotion_flow_type': 0,
                'action_track_url': [],
                'daily_retention_ratio': 0,
                'rf_predict_impression': 0,
                'package': '',
                'country': [
                    country,

                ],
                'is_open_url': 0,
                'fallback_type': 0,
                'search_delivery_type': 0,
                'external_url': '',
                'compliance_signature': '',
                'vast_moat': False,
                'automated_targeting': 0,
                'track_url': [],
                'optimize_goal': 100,
                'domain': '',
                'op_sys_filter': 0,
                'native_type': 1,
                'city': [],
                'flow_control_mode': 1,
                'platform': [
                    1,
                ],
                'particle_locations': [
                    country,
                ],
                'inventory_type': [],
                'download_url': '',
                'rf_predict_percentage': 0,
                'smart_bid_type': 7,
                'cpa_bid_type': 0,
                'app_retargeting_install': False,
                'cpv_video_duration_type': 0,
                'external_type': 102,
                'conversion_window': 0,
                'cpa_skip_first_phrase': 1,
                'ios14_quota_type': 1,
                'bid_display_mode': 0,
                'deep_bid_type': 0,
                'identity_id': '',
                'content_type': 1,
                'ios_osv': '',
                'promotion_website_type': 0,
                'is_share_disable': 0,
                'is_comment_disable': 1,
                'action_scenes_v2': [],
                'exclude_app_package_id': 0,
                'budget': budget,
                'product_source': 0,
                'districts': [],
                'household_income': [],
                'week_schedule': [
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                ],
                'product_platform_id': '0',
                'mcc_mnc': [],
                'age': [
                    [
                        25,
                        34,
                    ],
                    [
                        35,
                        44,
                    ],
                    [
                        45,
                        54,
                    ],
                    [
                        55,
                        100,
                    ],
                ],
                'contextual_tags': [],
                'ac': [],
                'in_market_tags': [],
                'last_frame': [],
                'dpa_open_url_type': 0,
                'creative_material_mode': 3,
                'cpa_bid': '',
                'app_type': 0,
                'carriers': [],
                'objective_type': 3,
                'coming_source_type': 5,
                'avatar_icon': {
                    'hash': '',
                    'url': '',
                    'uri': '',
                    'height': 100,
                    'width': 100,
                    'web_uri': '',
                },
                'dpa_retargeting_type': 0,
                'action_categories_v2': [],
                'app_retargeting_type': 0,
                'ad_category_detail': 0,
                'bid': '',
                'classify': 1,
                'province': [],
                'brand_safety_partner': 0,
                'flow_package_exclude': [],
                'interest_keywords_lang_i18n': [],
                'device_models': [],
                'ad_tag': [],
                'effective_frame': [],
                'product_set_id': '0',
                'launch_price': [],
                'identity_type': 0,
                'deep_external_action': 0,
                'params_type': 0,
                'is_rf_premium_inventory': False,
                'schedule_type': 1,
                'origin_ad_id': 0,
                'dpa_local_audience': 0,
                'ad_ref_app_id': '',
                'inventory_flow_type': 1,
                'is_drop': 0,
            },
            'risk_info': {
            },
        }

        response = requests.post('https://ads.tiktok.com/api/v2/i18n/perf/ad/create/?aadvid='+id+'&req_src=ad_creation&msToken='+cookies['msToken']+'=&X-Bogus=fgfgbgfbgf'+str(
            seed)+'&_signature='+str(seed), cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        print(response.json())
        if response.json()['msg'] == 'success':
            cc = str((response.json()['data']['ad_ids']))

            bibi = (cc.translate({ord(i): None for i in "'"}))
            bibi2 = (bibi.translate({ord(i): None for i in "[]"}))
            print("Ad_group")

            print("//////////////////////")
            print(response.json())
            print("//////////////////////")
            return bibi2
        else:
            print('None')
            return None
    
    def adgroup_create_conversion(self, id, campaign_id, pixel_d, name, country, external_action, start_time, budget):
        seed = random.randint(0,2000)
        cookies = self.COOKIES
        headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'X-CSRFToken': cookies['csrftoken'],
        'User-Agent': a.USER_AGENT,
        
        'Origin': 'https://ads.tiktok.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+id+'&creation_type=create_new&temp_campaign_id='+campaign_id,
        'Accept-Language': 'en-US,en',
        }
        json_data = {
    'base_info': {
        'struct_version': 1,
        'campaign_id': campaign_id,
          "ad_audit_status": "1",
          "primary_status": "delivery_ok",
           "ad_primary_status": "delivery_ok",
            "campaign_status": "campaign_delivery_ok",
             "ad_status": "ad_delivery_ok",

        'name': name,
        #'ad_id': '1752300155609090',
        'objective_type': 3,
        'classify': 1,
        'inventory_flow_type': 1,
        'inventory_flow': [
            3000,
        ],
        'search_delivery_type': 0,
        'creative_material_mode': 2,
        'identity_id': '',
        'identity_type': 0,
        'start_time': start_time,
        'end_time': '2032-12-15 19:10:02',
        'external_type': 102,
        'is_comment_disable': 1,
        'is_share_disable': 0,
        'ad_download_status': 1,
        'exclude_app_package_id': '',
        'ad_ref_pixel_id': pixel_d,
        'download_url': '',
        'brand_safety': 1,
        'brand_safety_partner': 0,
        'ac': [],
        'automated_targeting': 0,
        'ad_tag_v2': [],
        'in_market_tags': [],
        'action_scenes_v2': [],
        'video_actions_v2': [],
        'action_categories_v2': [],
        'action_days_v2': [],
        'interest_keywords_i18n': [],
        'interest_keywords_lang_i18n': [],
        'age': [
             
            [
                '25',
                '34',
            ],
            [
                '35',
                '44',
            ],
            [
                '45',
                '54',
            ],
            [
                '55',
                '100',
            ],
        ],
        'city': [],
        'country': [
           country
        ],
        'device_type': 0,
        'flow_package_exclude': [],
        'flow_package_include': [],
        'gender': 1,
        'spending_power_v2': [],
        'spending_power': 6,
        'is_hfss': 0,
        'household_income': [],
        'language_list': [],
        'launch_price': [],
        'carriers': [],
        'particle_locations': [
            country
        ],
        'platform': [
            1,
        ],
        'device_models': [],
        'province': [],
        'targeting_expansion': {
            'expansion_enabled': False,
            'expansion_types': [],
        },
        'exclude_custom_actions': [],
        'include_custom_actions': [],
        'retargeting_tags': [],
        'retargeting_tags_exclude': [],
        'app_retargeting_type': 0,
        'app_retargeting_install': False,
        'contextual_tags': [],
        'anti_discrimination': 0,
        'display_retargeting_tags': [],
        'display_retargeting_tags_exclude': [],
        'avatar_icon': {},
        'budget': budget,
        'budget_mode': 0,
        'period': 0,
        'week_schedule': [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ],
        'pre_fill_budget': '',
        'optimize_goal': 100,
        'cpv_video_duration_type': 0,
        'bid': 0,
        'cpa_bid': 4,
        'roas_bid': 0,
        'smart_bid_type': 0,
        'schedule_type': 1,
        'flow_control_mode': 0,
        'pricing': 9,
        'statistic_type': 0,
        'cpa_skip_first_phrase': 1,
        'frequency': 0,
        'frequency_schedule': 0,
        'cover_frequency_type': 0,
        'bid_display_mode': 0,
        'mco_attribution_type': 1,
        'external_action': external_action,
        'deep_external_action': 0,
        'deep_bid_type': 0,
        'deep_cpabid': 0,
        'daily_retention_ratio': 0,
        'ad_ref_app_id': '',
        'app_type': 0,
        'package': '',
        'promotion_website_type': 0,
        'promotion_target_type': 0,
        'product_platform_id': 0,
        'product_set_id': 0,
        'catalog_authorized_bc': '0',
        'target_device_version': 0,
        'ios14_quota_type': 1,
        'ad_app_profile_page_type': 0,
        'has_app_profile_auto_selectd': False,
        'origin_ad_id': 0,
        'ios_osv': '',
        'android_osv': 22,
        'districts': [],
        'retargeting_audience_rule': {
            'inclusions': None,
            'exclusions': None,
        },
    },
    'batch_info': [],
    'fake_campaign_id': '',
    'risk_info': {
      
    },
}
        
        
        
        response = requests.post('https://ads.tiktok.com/api/v2/i18n/perf/ad/create/?aadvid='+id, cookies=cookies, headers=headers, verify=True, json=json_data,proxies=self.PROXY,timeout=50)
        print(response.json())
        if response.json()['msg'] == 'success':
            cc = str((response.json()['data']['ad_ids']))
        
            bibi = (cc.translate({ord(i): None for i in "'"}))
            bibi2 = (bibi.translate({ord(i): None for i in "[]"}))
            print("Ad_group")
       
            print("//////////////////////")
            print(response.json())
            print("//////////////////////")
            return bibi2
        else:
            print('None')
            return None
    def adgroup_create_traffic(self, id, campaign_id, pixel_d, name, country, external_action, start_time, budget):
            seed = random.randint(0,2000)
            cookies = self.COOKIES
            headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,
            
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+id+'&creation_type=create_new&temp_campaign_id='+campaign_id,
            'Accept-Language': 'en-US,en',
            }
            json_data = {
    'base_info': {
        'struct_version': 1,
       'campaign_id': campaign_id,
        'name': name,
        'ad_id': '',
        'objective_type': 1,
        'classify': 1,
        'inventory_flow_type': 1,
        'inventory_flow': [
            3000,
        ],
        'search_delivery_type': 0,
        'creative_material_mode': 2,
        'identity_id': '',
        'identity_type': 0,
        'start_time': start_time,
        'end_time': '2032-12-23 17:23:58',
        'external_type': 102,
        'is_comment_disable': 1,
        'is_share_disable': 1,
        'ad_download_status': 1,
        'exclude_app_package_id': '',
        'ad_ref_pixel_id': pixel_d,
        'download_url': '',
        'brand_safety': 1,
        'brand_safety_partner': 0,
        'ac': [],
        'automated_targeting': 0,
        'ad_tag_v2': [],
        'in_market_tags': [],
        'action_scenes_v2': [],
        'video_actions_v2': [],
        'action_categories_v2': [],
        'action_days_v2': [],
        'interest_keywords_i18n': [],
        'interest_keywords_lang_i18n': [],
        'age': [
            [
                '18',
                '24',
            ],
            [
                '25',
                '34',
            ],
            [
                '35',
                '44',
            ],
            [
                '45',
                '54',
            ],
            [
                '55',
                '100',
            ],
        ],
        'city': [],
        'country': [
           country
        ],
        'device_type': 0,
        'flow_package_exclude': [],
        'flow_package_include': [],
        'gender': 1,
        'spending_power_v2': [],
        'is_hfss': 0,
        'household_income': [],
        'language_list': [],
        'launch_price': [],
        'carriers': [],
        'particle_locations': [
            country
        ],
        'platform': [
            1,
        ],
        'device_models': [],
        'province': [],
        'targeting_expansion': {
            'expansion_enabled': False,
            'expansion_types': [],
        },
        'exclude_custom_actions': [],
        'include_custom_actions': [],
        'retargeting_tags': [],
        'retargeting_tags_exclude': [],
        'app_retargeting_type': 0,
        'app_retargeting_install': False,
        'contextual_tags': [],
        'anti_discrimination': 0,
        'display_retargeting_tags': [],
        'display_retargeting_tags_exclude': [],
        'avatar_icon': {
            'web_uri': '',
        },
        'budget': budget,
        'budget_mode': 0,
        'period': 0,
        'week_schedule': [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ],
        'pre_fill_budget': '',
        'optimize_goal': 101,
        'cpv_video_duration_type': 0,
        'bid': 1,
        'cpa_bid': 0,
        'roas_bid': 0,
        'smart_bid_type': 0,
        'schedule_type': 1,
        'flow_control_mode': 0,
        'pricing': 2,
        'statistic_type': 0,
        'cpa_skip_first_phrase': 1,
        'frequency': 3,
        'frequency_schedule': 7,
        'cover_frequency_type': 1,
        'bid_display_mode': 0,
        'mco_attribution_type': 1,
        'external_action': external_action,
        'deep_external_action': 0,
        'deep_bid_type': 0,
        'deep_cpabid': 0,
        'daily_retention_ratio': 0,
        'ad_ref_app_id': '',
        'app_type': 0,
        'package': '',
        'promotion_website_type': 0,
        'promotion_target_type': 0,
        'product_platform_id': 0,
        'product_set_id': 0,
        'catalog_authorized_bc': '0',
        'target_device_version': 0,
        'ios14_quota_type': 1,
        'has_app_profile_auto_selectd': False,
        'ios_osv': '',
        'android_osv': 21,
        'districts': [],
        'retargeting_audience_rule': {
            'inclusions': None,
            'exclusions': None,
        },
    },
    'batch_info': [],
    'fake_campaign_id': '',
    'risk_info': {
        # 'cookie_enabled': True,
        # 'screen_width': 1536,
        # 'screen_height': 864,
        # 'browser_language': 'ca-ES',
        # 'browser_platform': 'Win32',
        # 'browser_name': 'Mozilla',
        # 'browser_version': '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        # 'browser_online': True,
        # 'timezone_name': 'Europe/Madrid',
    },
}

    def adgroup_create_page(self, id, campaign_id, pixel_d, name, country, external_action, start_time, budget):
            seed = random.randint(0,2000)
            cookies = self.COOKIES
            headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,
            
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+id+'&creation_type=create_new&temp_campaign_id='+campaign_id,
            'Accept-Language': 'en-US,en',
            }
            json_data = {
            'batch_info': [],
            'base_info': {
                'struct_version': 1,
                'app_name': '',
                'target_device_version': 0,
                'shop_id': '0',
                'shop_authorized_bc': '0',
                'rf_notify_users': [],
                'flow_package_include': [],
                'action_days_v2': [],
                'roas_bid': 0,
                'targeting_expansion': {
                    'expansion_enabled': False,
                    'expansion_types': [],
                },
                'include_custom_actions': [],
                'source': '',
                'anti_discrimination': 0,
                'is_hfss': 0,
                'video_actions': [],
                'auto_open': 0,
                'ad_ref_pixel_id': pixel_d,
                'video_actions_v2': [],
                'start_time': start_time,
                'ad_reach_frequency_buy_type': 0,
                'statistic_type': 0,
                'ad_tag_v2': [],
                'inventory_flow': [
                    3000,
                ],
                'external_action': external_action,
                'retargeting_tags': [],
                'cpa_auto': 0,
                'rf_predict_reach': 0,
                'action_scene': [
                    2,
                ],
                'household_income': [],
                'name': name,
                'creative_display_mode': 0,
                'gender': 1,
                'first_frame': [],
                'ad_keywords': [],
                'operators_id': [],
                'ad_download_status': 1,
                'budget_mode': 0,
                'open_url': '',
                'campaign_id': campaign_id,
                'exclude_custom_actions': [],
                'promotion_target_type': 0,
                'frequency': 3,
                'pricing': 9,
                'device_type': 0,
                'cover_frequency_type': 1,
                'catalog_authorized_bc': '0',
                'android_osv': '21',
                'language_list': [
                    #   'en',
                    #   'tr',
                ],
                'flow_precision': 0,
                'frequency_schedule': 7,
                'ab_test_id': 0,
                'retargeting_audience_rule': {
                    'inclusions': None,
                    'exclusions': None,
                },
                'interest_keywords_i18n': [],
                'rf_estimate_key': '0',
                'end_time': '2033-01-28 19:00:01',
                'deep_cpabid': 0,
                'retargeting_tags_exclude': [],
                'brand_safety': 1,
                'shop_type': 0,
                'promotion_flow_type': 0,
                'action_track_url': [],
                'plan_version_type': 0,
                'daily_retention_ratio': 0,
                'rf_predict_impression': 0,
                'package': '',
                'country': [
                    country
                ],
                'is_open_url': 0,
                'fallback_type': 0,
                'search_delivery_type': 0,
                'external_url': '',
                'spending_power_v2': [],
                'compliance_signature': '',
                'vast_moat': False,
                'automated_targeting': 0,
                'track_url': [],
                'optimize_goal': 100,
                'domain': '',
                'op_sys_filter': 0,
                'native_type': 1,
                'city': [],
                'flow_control_mode': 1,
                'platform': [
                    1,
                ],
                'particle_locations': [
                   country
                ],
                'inventory_type': [],
                'download_url': '',
                'rf_predict_percentage': 0,
                'smart_bid_type': 7,
                'cpa_bid_type': 0,
                'app_retargeting_install': False,
                'cpv_video_duration_type': 0,
                'external_type': 102,
                'conversion_window': 0,
                'cpa_skip_first_phrase': 1,
                'ios14_quota_type': 1,
                'bid_display_mode': 0,
                'deep_bid_type': 0,
                'identity_id': '',
                'content_type': 1,
                'ios_osv': '',
                'promotion_website_type': 1,
                'is_share_disable': 1,
                'is_comment_disable': 1,
                'action_scenes_v2': [],
                'exclude_app_package_id': 0,
                'budget': budget,
                'product_source': 0,
                'districts': [],
                'num': 1,
                'week_schedule': [
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                ],
                'product_platform_id': '0',
                'mcc_mnc': [],
                'age': [
                    [
                        25,
                        34,
                    ],
                    [
                        35,
                        44,
                    ],
                    [
                        55,
                        100,
                    ],
                    [
                        45,
                        54,
                    ],
                ],
                'contextual_tags': [],
                'ac': [],
                'in_market_tags': [],
                'last_frame': [],
                'dpa_open_url_type': 0,
                'creative_material_mode': 2,
                'cpa_bid': '',
                'app_type': 0,
                'carriers': [],
                'objective_type': 3,
                'coming_source_type': 1,
                'avatar_icon': {
                    'hash': '',
                    'url': '',
                    'uri': '',
                    'height': 100,
                    'width': 100,
                    'web_uri': '',
                },
                'dpa_retargeting_type': 0,
                'action_categories_v2': [],
                'app_retargeting_type': 0,
                'ad_category_detail': 0,
                'bid': '',
                'classify': 1,
                'province': [],
                'brand_safety_partner': 0,
                'flow_package_exclude': [],
                'interest_keywords_lang_i18n': [],
                'device_models': [],
                'ad_tag': [],
                'effective_frame': [],
                'product_set_id': '0',
                'launch_price': [],
                'identity_type': 0,
                'deep_external_action': 0,
                'params_type': 0,
                'is_rf_premium_inventory': False,
                'schedule_type': 1,
                'origin_ad_id': 0,
                'dpa_local_audience': 0,
                'ad_ref_app_id': '',
                'inventory_flow_type': 1,
                'is_drop': 0,
            },
            'ad_channel': 1,
            'risk_info': {
            
            },
            }
            
            response = requests.post('https://ads.tiktok.com/api/v2/i18n/perf/ad/create/?aadvid='+id+'&req_src=ad_creation&msToken='+cookies['msToken']+'=&X-Bogus=DFplmt'+str(seed)+'&_signature='+str(seed), cookies=cookies, headers=headers, verify=True, json=json_data,proxies=self.PROXY,timeout=50)
            print(response.json())
            if response.json()['msg'] == 'success':
                cc = str((response.json()['data']['ad_ids']))
            
                bibi = (cc.translate({ord(i): None for i in "'"}))
                bibi2 = (bibi.translate({ord(i): None for i in "[]"}))
                print("Ad_group")
        
                print("//////////////////////")
                print(response.json())
                print("//////////////////////")
                return bibi2
            else:
                print('None')
                return None

    def adgroup_update(self, id, campaign_id, pixel_d, ad_ids):
        seed = random.randint(0, 2000)
        cookies = self.COOKIES
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,

            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+id+'&creation_type=create_new&temp_campaign_id=1732352314274&temp_adgroup_id=121025',
            'Accept-Language': 'en-US,en',
        }
        json_data = {
            'batch_info': [],
            'base_info': {
                'struct_version': 1,
                'ad_id': ad_ids,
                'app_name': '',
                'target_device_version': 0,
                'ad_app_profile_page_type': 0,
                'shop_id': '0',
                'shop_authorized_bc': '0',
                'rf_notify_users': [],
                'flow_package_include': [],
                'action_days_v2': [],
                'roas_bid': 0,
                'targeting_expansion': {
                    'expansion_enabled': False,
                    'expansion_types': [],
                },
                'include_custom_actions': [],
                'source': '',
                'anti_discrimination': 0,
                'is_hfss': 0,
                'video_actions': [],
                'auto_open': 0,
                'ad_ref_pixel_id': pixel_d,
                'video_actions_v2': [],
                'spending_power': 1,
                'start_time': '2022-12-02 11:00:58',
                'ad_reach_frequency_buy_type': 0,
                'statistic_type': 0,
                'ad_tag_v2': [],
                'inventory_flow': [
                    3000,
                ],
                'external_action': 5,  # 5 click 9 download
                'retargeting_tags': [],
                'cpa_auto': 0,
                'rf_predict_reach': 0,
                'action_scene': [
                    2,
                ],
                'num': 1,
                'name': 'Ad group 20221015010325_'+str(id),
                'creative_display_mode': 0,
                'gender': 1,
                'first_frame': [],
                'ad_keywords': [],
                'operators_id': [],
                'ad_download_status': 1,
                'budget_mode': 0,
                'open_url': '',
                'campaign_id': campaign_id,
                'exclude_custom_actions': [],
                'frequency': 0,
                'pricing': 9,
                'device_type': 0,
                'cover_frequency_type': 0,
                'catalog_authorized_bc': '0',
                'android_osv': '22',
                'language_list': [],
                'flow_precision': 0,
                'frequency_schedule': 0,
                'ab_test_id': 0,
                'retargeting_audience_rule': {
                    'inclusions': None,
                    'exclusions': None,
                },
                'interest_keywords_i18n': [],
                'rf_estimate_key': '0',
                'end_time': '2032-10-20 21:52:58',
                'deep_cpabid': 0,
                'retargeting_tags_exclude': [],
                'brand_safety': 1,
                'shop_type': 0,
                'promotion_flow_type': 0,
                'action_track_url': [],
                'daily_retention_ratio': 0,
                'rf_predict_impression': 0,
                'package': '',
                'country': [
                    2264397,

                ],
                'is_open_url': 0,
                'fallback_type': 0,
                'search_delivery_type': 0,
                'external_url': '',
                'compliance_signature': '',
                'vast_moat': False,
                'automated_targeting': 0,
                'track_url': [],
                'optimize_goal': 100,
                'domain': '',
                'op_sys_filter': 0,
                'native_type': 1,
                'city': [],
                'flow_control_mode': 1,
                'platform': [
                    1,
                ],
                'particle_locations': [
                    2264397,
                ],
                'inventory_type': [],
                'download_url': '',
                'rf_predict_percentage': 0,
                'smart_bid_type': 7,
                'cpa_bid_type': 0,
                'app_retargeting_install': False,
                'cpv_video_duration_type': 0,
                'external_type': 102,
                'conversion_window': 0,
                'cpa_skip_first_phrase': 1,
                'ios14_quota_type': 1,
                'bid_display_mode': 0,
                'deep_bid_type': 0,
                'identity_id': '',
                'content_type': 1,
                'ios_osv': '',
                'promotion_website_type': 0,
                'is_share_disable': 0,
                'is_comment_disable': 1,
                'action_scenes_v2': [],
                'exclude_app_package_id': 0,
                'budget': 50000,
                'product_source': 0,
                'districts': [],
                'household_income': [],
                'week_schedule': [
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                    [],
                ],
                'product_platform_id': '0',
                'mcc_mnc': [],
                'age': [
                    [
                        25,
                        34,
                    ],
                    [
                        35,
                        44,
                    ],
                    [
                        45,
                        54,
                    ],
                    [
                        55,
                        100,
                    ],
                ],
                'contextual_tags': [],
                'ac': [],
                'in_market_tags': [],
                'last_frame': [],
                'dpa_open_url_type': 0,
                'creative_material_mode': 2,
                'cpa_bid': '',
                'app_type': 0,
                'carriers': [],
                'objective_type': 3,
                'coming_source_type': 5,
                'avatar_icon': {
                    'hash': '',
                    'url': '',
                    'uri': '',
                    'height': 100,
                    'width': 100,
                    'web_uri': '',
                },
                'dpa_retargeting_type': 0,
                'action_categories_v2': [],
                'app_retargeting_type': 0,
                'ad_category_detail': 0,
                'bid': '',
                'classify': 1,
                'province': [],
                'brand_safety_partner': 0,
                'flow_package_exclude': [],
                'interest_keywords_lang_i18n': [],
                'device_models': [],
                'ad_tag': [],
                'effective_frame': [],
                'product_set_id': '0',
                'launch_price': [],
                'identity_type': 0,
                'deep_external_action': 0,
                'params_type': 0,
                'is_rf_premium_inventory': False,
                'schedule_type': 1,
                'origin_ad_id': 0,
                'dpa_local_audience': 0,
                'ad_ref_app_id': '',
                'inventory_flow_type': 1,
                'is_drop': 0,
            },
            'risk_info': {
            },
        }

        response = requests.post('https://ads.tiktok.com/api/v2/i18n/perf/ad/update/?aadvid='+id+'&req_src=ad_creation&msToken='+cookies['msToken']+'=&X-Bogus=DFplmt'+str(
            seed)+'&_signature='+str(seed), cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        print(response.json())

    def ident(self, id):
        cookies = self.COOKIES
        seed = random.randint(0, 200)
        headers = {
            'Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'User-Agent': a.USER_AGENT,

            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',

        }
        json_data = {
            'display_name': 'Birdilan', #+str(seed),
            'profile_image': '',
            'identity_type': 1
        }

        response = requests.post('https://ads.tiktok.com/api/v3/i18n/identity/save/?aadvid='+id+'&req_src=ad_creation&msToken=' +
                                 cookies['msToken'], cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        print(response.json())
        return str(response.json()['data']['identity_info']['identity_id'])

    def page_create(self, id, nomer, url, template_id, template_url, template_text):

        cookies = self.COOKIES
        headers = {
            'Host': 'ads.tiktok.com',
            # 'Content-Length': '13619',
            'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Dnt': '1',
            'Language': 'en',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': a.USER_AGENT,
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'X-Csrftoken': cookies['csrftoken'],
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'nl-BE,nl;q=0.9,en-US;q=0.8,en;q=0.7',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'tt_webid=7120130498060600834; csrftoken=3hnIqlW6xMQWNcxdgYZd4WDl07lDGlK3; lang_type=en; tta_attr_id=0.1657784579.7120130549028487170; tta_attr_id_mirror=0.1657784579.7120130549028487170; pre_country=DE; tt_webid=7120130498060600834; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}; passport_csrf_token=91fb024fdc8400822736035e591f19f7; passport_csrf_token_default=91fb024fdc8400822736035e591f19f7; sso_auth_status_ads=e57725fd22e67fb61bd6ff15305f48d4; sso_auth_status_ss_ads=e57725fd22e67fb61bd6ff15305f48d4; sso_uid_tt_ads=a96da0ce0d490e10b33485f80302bb4e3e55333e17c0bc635fd23d8189a26d68; sso_uid_tt_ss_ads=a96da0ce0d490e10b33485f80302bb4e3e55333e17c0bc635fd23d8189a26d68; toutiao_sso_user_ads=dff8d7af930edcb19168e5aec16d2f29; toutiao_sso_user_ss_ads=dff8d7af930edcb19168e5aec16d2f29; sid_ucp_sso_v1_ads=1.0.0-KDIxMGJkZGEzZGFiNzQzOGUzNDRhMDM1ZDNlNDc3ZjI3OWE1ODUzMDMKIAiCiIvKosbb52IQtJK_lgYYrwwgDDC0kr-WBjgBQOwHEAEaA3NnMSIgZGZmOGQ3YWY5MzBlZGNiMTkxNjhlNWFlYzE2ZDJmMjk; ssid_ucp_sso_v1_ads=1.0.0-KDIxMGJkZGEzZGFiNzQzOGUzNDRhMDM1ZDNlNDc3ZjI3OWE1ODUzMDMKIAiCiIvKosbb52IQtJK_lgYYrwwgDDC0kr-WBjgBQOwHEAEaA3NnMSIgZGZmOGQ3YWY5MzBlZGNiMTkxNjhlNWFlYzE2ZDJmMjk; odin_tt=e8d7b70658c178ed00def40988886fd0ccff193281b8857eba55d8fd9d8bce938f26ca71bfeb44bb7c90a1462df3dc9d75d766ea1f88015a2f0b022ae0a6d4c1; passport_auth_status_ads=9ff38c8fb5ce1702d88e69aa4b6a285e%2C; passport_auth_status_ss_ads=9ff38c8fb5ce1702d88e69aa4b6a285e%2C; sid_guard_ads=5023399f6ce814b6eda1a6b392f07340%7C1657784629%7C863999%7CSun%2C+24-Jul-2022+07%3A43%3A48+GMT; uid_tt_ads=ac917862e968837eff974c459dd14112829134a19c9ec2b26e723e8f59cdc219; uid_tt_ss_ads=ac917862e968837eff974c459dd14112829134a19c9ec2b26e723e8f59cdc219; sid_tt_ads=5023399f6ce814b6eda1a6b392f07340; sessionid_ads=5023399f6ce814b6eda1a6b392f07340; sessionid_ss_ads=5023399f6ce814b6eda1a6b392f07340; sid_ucp_v1_ads=1.0.0-KDgyNjk4OTc1Yzc0ZTcyYjBiMGNjNjU0MjgyYTdhY2QyMmExODc5MGYKGgiCiIvKosbb52IQtZK_lgYYrwwgDDgBQOwHEAEaA3NnMSIgNTAyMzM5OWY2Y2U4MTRiNmVkYTFhNmIzOTJmMDczNDA; ssid_ucp_v1_ads=1.0.0-KDgyNjk4OTc1Yzc0ZTcyYjBiMGNjNjU0MjgyYTdhY2QyMmExODc5MGYKGgiCiIvKosbb52IQtZK_lgYYrwwgDDgBQOwHEAEaA3NnMSIgNTAyMzM5OWY2Y2U4MTRiNmVkYTFhNmIzOTJmMDczNDA; msToken=5Omc7r6-nMlvmq2XDFt6r6tkjvt8ePV_1QnKtT9TINdVhlKV6M5rxVcqOT6W6vqO8HAoingiY0zHr9msfr4RrboeVJiAmJRCXdc4euBNFamxwSYz5Rv-aFxYY0TDZqT-uY4heA==; _tea_utm_cache_2777=undefined; store-idc=maliva; store-country-code=nl; lang=en; _abck=D839DC2EF8EE2881F0D907C282B909E2~-1~YAAQT9XOF9hJy/WBAQAAXgma/AjfTyHy7SGR5UTp8ggaoyb1ELBu2ZY45pzEv+qyp9LHJ3IAMBPPvH3cYLfgFUJvCZW0Z2fyLi5F5Eoc6FdtyI3r7nsHToYmi2IKBQC4Ddn2GA/xfTr9Q5GZ3y82UP+69OwQ7eG7L9UrZlw4eg4t+T1WLtemJSomwsSbDmrag/Wk6yVUBrWMRGpx6o5LX0m1XW+tv9rbc+j2avZTNmHVwDC1pE8EEt1iHE/33uuRMOxSr0W4V2esIxLv5Xzli9agwOYSv5OioETkBFMqYDCuCWoT4pzjTZWeICu6wzB+mp2cvimHjwEZlzWkGhdQes1BCrUY8IinUb3bG0B1NlcaVf77UFvMta8ox89TY6rfpk/szsxoa1yidA==~-1~-1~-1; gftoken=OTQ5NTM5OTg4fDE2NTc4MDA4ODE2Nnx8MAcHBwcHBwc; _gcl_au=1.1.1365756755.1657800889; _ga=GA1.2.111395199.1657800893; _gid=GA1.2.494020031.1657800893; _gat_UA-143770054-3=1; tta_attr_ga_cid=111395199.1657800893; _uetvid=928a1c40036e11edbba8313829e277d8; _rdt_uuid=1657800899448.cf3d6eb8-048f-4c96-8f24-d884eeba63a3; _tt_enable_cookie=1; _hjSessionUser_2525957=eyJpZCI6ImJlYWQ2NWI1LWZhYmYtNWZlOC04M2JlLWRjMDNiMTQ0N2U2OSIsImNyZWF0ZWQiOjE2NTc4MDA5MDE5OTUsImV4aXN0aW5nIjpmYWxzZX0=; _fbp=fb.1.1657800902716.173941397; _ttp=2BvyYiLS1bGrYvyJTtdRpCr4chh; _tea_utm_cache_3820=undefined; msToken=L2B2IL0z06tAmQboGottMwrFQNuQk4xg6z8DQIRIUll7pn_fu9_cVAlqEIqeRUav5BECotlD14hyCa2iWQtYCCaVUqAJxZn2GOcbIG-Spj5o_GDoQNbRQUIXHx0xhTNt0j1EMw==; i18next=en; s_v_web_id=verify_l5l08lgc_wGapJWPM_cb5D_4ET4_BDnu_WEGFrznOEAs0; part=stable; MONITOR_WEB_ID=95dc6cbc-0e4c-44be-aa29-1a79c1b60c1c; _tea_utm_cache_1583={%22campaign_id%22:1738432680724498}; _tea_utm_cache_4697={%22campaign_id%22:1738432680724498}; _tea_utm_cache_224013={%22campaign_id%22:1738432680724498}; _tea_utm_cache_345918={%22campaign_id%22:1738432680724498}; ttwid=1%7CuNap7YHz5pPNUCZ2tcjKB1Abm_vef5sKQmQmA62L7tA%7C1657898755%7Cb62cb6266539f0be7d0c576e845f572cfeac7c9c6437034c1699c1d6c35c5fde',
        }
        
        json_data = {
            'account_id': str(id),
            'business_type': 6,
            'data': '{"map":{"meta":["meta"],"Picture":["22a949c017b4ecba"],"Button":[],"Text":[],"Header":["headerview1"],"Swiper":[],"HeaderPlaceholder":["headerplaceholder"],"HeaderPlaceholderBody":[],"Video":[],"Subpage":["fe79bfc90f034bae"],"PageContent":["pagecontentview1"],"BottomFloatView":["6ba17a96bd36acee"],"BottomPlaceholder":["bottomplaceholder"],"PixelButton":["4ec9e26b406c142e"],"ProductPackage":[],"LinkButton":[],"Coupon":[]},"data":{"meta":{"brickIndex":"meta","children":["headerview1","fe79bfc90f034bae"],"language":"ru","name":"LpPage","bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"theme":{"preset":"light","colors":{}},"version":4,"topSafeArea":false,"emitScrollEvent":true,"parent":null,"events":[],"animations":{},"converter":{"convertId":""},"externalAction":5},"headerview1":{"name":"LpHeader","brickIndex":"headerview1","parent":"meta","layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"height":44,"width":375,"version":1},"titleColor":{"type":"themeColor","color":"","themeColor":"textPrimary2","version":1},"bgColor":{"color":"rgba(0,0,0,1)","version":1,"type":"themeColor","themeColor":"bgPrimary"},"initBgAlpha":0,"initIconColor":{"color":"rgb(255,255,255)","version":1,"type":"color","themeColor":"textPrimary2"},"exitCallbackEnable":false,"dynamicEffect":{"enable":true,"fixIconColor":false,"referenceWidth":750,"referenceHeight":300},"version":0,"children":[]},"fe79bfc90f034bae":{"bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"bgImage":{"format":"jpg","height":281,"size":0,"src":"","width":375,"version":0},"bgType":"color","brickIndex":"fe79bfc90f034bae","children":["6ba17a96bd36acee","headerplaceholder","pagecontentview1","bottomplaceholder"],"name":"LpSubpage","parent":"meta","routable":true,"title":"instantPage","version":0},"6ba17a96bd36acee":{"name":"LpFloatView","children":["5f9cf1aeefe57b1a"],"bgType":"color","bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"visibility":"visible","alignItems":"center","borderRadius":0,"float":"bottom","layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"width":375,"version":1},"version":5,"brickIndex":"6ba17a96bd36acee","parent":"fe79bfc90f034bae","flexDirection":"column","justifyContent":"normal","boxShadow":[],"animations":{},"bgGradient":{"value":""},"flexWrap":"nowrap","events":[]},"5f9cf1aeefe57b1a":{"name":"LpButton","color":{"color":"rgba(255, 255, 255, 1)","type":"color","themeColor":"","version":1},"disabledColor":{"color":"rgba(22, 24, 35, 0.34)","version":1,"type":"color","themeColor":""},"fontSize":15,"fontStyle":["bold"],"bgType":"color","bgColor":{"type":"color","color":"rgba(254, 44, 85, 1)","themeColor":"","version":1},"disabledBgColor":{"color":"rgba(22, 24, 35, 0.06)","version":1,"type":"color","themeColor":""},"bgImage":{"src":"","width":343,"height":44,"size":0,"format":"jpg","version":0},"borderColor":{"type":"color","color":"rgba(0,0,0,0)","themeColor":"","version":1},"borderWidth":0,"borderRadius":2,"link":{"linkType":"url","scheme":"","subpage":"","url":"'+url+'","appDownload":{},"deeplink":{"enable":false,"url":""},"version":3,"redirectUrl":""},"layout":{"height":44,"width":343,"margin":{"bottom":12,"left":16,"right":16,"top":12},"position":"normal","version":1},"convertInfo":{"logType":"normalClick","normalClickArg":{"eventType":"ClickButton","eventValue":{}},"version":0},"content":{"type":"text","text":"'+template_text+'","i18nKey":"shop_now","slots":{},"version":2,"date":{"timestamp":-1,"locale":"","format":""}},"version":1,"brickIndex":"5f9cf1aeefe57b1a","children":[],"parent":"6ba17a96bd36acee","events":[],"aliasName":"Button"},"headerplaceholder":{"name":"LpView","brickIndex":"headerplaceholder","parent":"fe79bfc90f034bae","children":[],"bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"center","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"version":1},"boxShadow":[],"version":5,"flexDirection":"column","justifyContent":"flex-start","borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"events":[],"animations":{"initCard":{"duration":0,"endAt":{"height":0,"opacity":0}},"cardToPage":{"duration":500,"endAt":{"height":44,"opacity":1}}},"flexWrap":"nowrap","bgGradient":{"value":""}},"pagecontentview1":{"name":"LpView","brickIndex":"pagecontentview1","parent":"fe79bfc90f034bae","children":["4ec9e26b406c142e","22a949c017b4ecba"],"bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"center","borderRadius":0,"layout":{"position":"normal","margin":{"top":-4,"left":0,"right":0,"bottom":0},"version":1},"boxShadow":[],"version":5,"flexDirection":"column","justifyContent":"flex-start","borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"events":[],"animations":{"cardToPage":{"duration":500,"endAt":{"top":-4}},"initCard":{"duration":0,"endAt":{"top":8}}},"flexWrap":"nowrap","bgGradient":{"value":""}},"4ec9e26b406c142e":{"name":"LpView","children":[],"bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"stretch","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"version":1},"version":5,"brickIndex":"4ec9e26b406c142e","parent":"pagecontentview1","flexDirection":"column","justifyContent":"normal","boxShadow":[],"borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"flexWrap":"nowrap","events":[],"animations":{},"bgGradient":{"value":""},"aliasName":"Button"},"22a949c017b4ecba":{"name":"LpView","children":["5caf7400808e075e"],"bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"stretch","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"version":1},"version":5,"brickIndex":"22a949c017b4ecba","parent":"pagecontentview1","flexDirection":"column","justifyContent":"normal","boxShadow":[],"borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"flexWrap":"nowrap","events":[],"animations":{},"bgGradient":{"value":""},"aliasName":"Image"},"5caf7400808e075e":{"name":"LpPicture","src":{"format":"png","height":1280,"size":1537470,"src":"'+template_url+'","width":756},"borderRadius":0,"link":{"linkType":"url","url":"","scheme":"","subpage":"","appDownload":{},"redirectUrl":"","deeplink":{"enable":false,"url":""},"version":3},"layout":{"position":"normal","margin":{"top":0,"right":0,"bottom":0,"left":0},"height":635,"width":375,"version":1},"version":2,"mode":"aspectFit","brickIndex":"5caf7400808e075e","children":[],"parent":"22a949c017b4ecba","events":[],"animations":{},"aliasName":"Image"},"bottomplaceholder":{"name":"LpView","brickIndex":"bottomplaceholder","parent":"fe79bfc90f034bae","children":[],"bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"stretch","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"width":375,"height":68,"version":1},"version":5,"flexDirection":"column","justifyContent":"normal","boxShadow":[],"borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"flexWrap":"nowrap","events":[],"animations":{},"bgGradient":{"value":""}}}}',
            'template_id': '7174303714692432129',  #  7080536318425497857
            'title': 'Untitled page 7/17/22, 10:1 PM',
            # tos-alisg-i-375lmtcpo0-sg/8df7329a9fdf47bc890c76f3182e74e5
            'thumbnail_uri': str(template_id),


           
        }


#         json_data = {
#     'business_type': 6,
#     'data': '{"map":{"meta":["meta"],"Picture":[],"Button":[],"Text":[],"Header":["headerview1"],"Swiper":[],"HeaderPlaceholder":["headerplaceholder"],"HeaderPlaceholderBody":[],"Video":["adaff64550b09e30"],"Subpage":["fe79bfc90f034bae"],"PageContent":["pagecontentview1"],"BottomFloatView":["b8e97365cea8ddd8"],"BottomPlaceholder":["bottomplaceholder"],"PixelButton":["8926505f6a03e149"],"ProductPackage":[],"LinkButton":[],"Coupon":[]},"data":{"meta":{"brickIndex":"meta","children":["headerview1","fe79bfc90f034bae"],"language":"en","name":"LpPage","bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"theme":{"preset":"light","colors":{}},"version":4,"topSafeArea":false,"emitScrollEvent":true,"parent":null,"events":[],"animations":{},"converter":{"convertId":""},"externalAction":5},"headerview1":{"name":"LpHeader","brickIndex":"headerview1","parent":"meta","layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"height":44,"width":375,"version":1},"titleColor":{"type":"themeColor","color":"","themeColor":"textPrimary2","version":1},"bgColor":{"color":"rgba(0,0,0,1)","version":1,"type":"themeColor","themeColor":"bgPrimary"},"initBgAlpha":0,"initIconColor":{"color":"rgb(255,255,255)","version":1,"type":"color","themeColor":"textPrimary2"},"exitCallbackEnable":false,"dynamicEffect":{"enable":true,"fixIconColor":false,"referenceWidth":750,"referenceHeight":300},"version":1,"children":[],"dynamicTitle":{"path":[],"version":0},"feedbackHidden":false},"fe79bfc90f034bae":{"bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"bgImage":{"format":"jpg","height":281,"size":0,"src":"","width":375,"version":0},"bgType":"color","brickIndex":"fe79bfc90f034bae","children":["b8e97365cea8ddd8","headerplaceholder","pagecontentview1","bottomplaceholder"],"name":"LpSubpage","parent":"meta","routable":true,"title":"instantPage","version":0},"b8e97365cea8ddd8":{"name":"LpFloatView","children":["46539f2033840f08"],"bgType":"color","bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"visibility":"visible","alignItems":"center","borderRadius":0,"float":"bottom","layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"width":375,"version":1},"version":5,"brickIndex":"b8e97365cea8ddd8","parent":"fe79bfc90f034bae","flexDirection":"column","justifyContent":"normal","boxShadow":[],"animations":{},"bgGradient":{"value":""},"flexWrap":"nowrap","events":[]},"46539f2033840f08":{"name":"LpButton","color":{"color":"rgba(255, 255, 255, 1)","type":"color","themeColor":"","version":1},"disabledColor":{"color":"rgba(22, 24, 35, 0.34)","version":1,"type":"color","themeColor":""},"fontSize":15,"fontStyle":["bold"],"bgType":"color","bgColor":{"type":"color","color":"rgba(254, 44, 85, 1)","themeColor":"","version":1},"disabledBgColor":{"color":"rgba(22, 24, 35, 0.06)","version":1,"type":"color","themeColor":""},"bgImage":{"src":"","width":343,"height":44,"size":0,"format":"jpg","version":0},"borderColor":{"type":"color","color":"rgba(0,0,0,0)","themeColor":"","version":1},"borderWidth":0,"borderRadius":2,"link":{"linkType":"url","scheme":"","subpage":"","url":"'+"https://trafgambl.fun/W49232gP?creo="+str(id)+str(self.cr['data']['material_infos'][nomer]['base_info']['material_name'])+'","appDownload":{},"deeplink":{"enable":false,"url":""},"version":3,"redirectUrl":""},"layout":{"height":44,"width":343,"margin":{"bottom":12,"left":16,"right":16,"top":12},"position":"normal","version":1},"convertInfo":{"logType":"normalClick","normalClickArg":{"eventType":"ClickButton","eventValue":{}},"version":0},"content":{"type":"text","text":"Instalar","i18nKey":"shop_now","slots":{},"version":2,"date":{"timestamp":-1,"locale":"","format":""}},"version":1,"brickIndex":"46539f2033840f08","children":[],"parent":"b8e97365cea8ddd8","events":[],"aliasName":"Кнопка"},"headerplaceholder":{"name":"LpView","brickIndex":"headerplaceholder","parent":"fe79bfc90f034bae","children":[],"bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"center","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"version":1},"boxShadow":[],"version":5,"flexDirection":"column","justifyContent":"flex-start","borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"events":[],"animations":{"initCard":{"duration":0,"endAt":{"height":0,"opacity":0}},"cardToPage":{"duration":500,"endAt":{"height":44,"opacity":1}}},"flexWrap":"nowrap","bgGradient":{"value":""}},"pagecontentview1":{"name":"LpView","brickIndex":"pagecontentview1","parent":"fe79bfc90f034bae","children":["8926505f6a03e149","adaff64550b09e30"],"bgColor":{"type":"themeColor","color":"","themeColor":"bgPrimary","version":1},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"center","borderRadius":0,"layout":{"position":"normal","margin":{"top":-4,"left":0,"right":0,"bottom":0},"version":1},"boxShadow":[],"version":5,"flexDirection":"column","justifyContent":"flex-start","borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"events":[],"animations":{"cardToPage":{"duration":500,"endAt":{"top":-4}},"initCard":{"duration":0,"endAt":{"top":8}}},"flexWrap":"nowrap","bgGradient":{"value":""}},"8926505f6a03e149":{"name":"LpView","children":[],"bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"stretch","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"version":1},"version":5,"brickIndex":"8926505f6a03e149","parent":"pagecontentview1","flexDirection":"column","justifyContent":"normal","boxShadow":[],"borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"flexWrap":"nowrap","events":[],"animations":{},"bgGradient":{"value":""},"aliasName":"Кнопка"},"adaff64550b09e30":{"name":"LpView","children":["1930b81764293cab"],"bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"stretch","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"version":1},"version":5,"brickIndex":"adaff64550b09e30","parent":"pagecontentview1","flexDirection":"column","justifyContent":"normal","boxShadow":[],"borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"flexWrap":"nowrap","events":[],"animations":{},"bgGradient":{"value":""},"aliasName":"Видео"},"1930b81764293cab":{"name":"LpVideo","videoSrc":{"vid":"v10dbbg50000cc9526rc77uefl6bkhl0","title":"ssstik.io_1662144475343.mp4","size":679822,"poster":{"format":"jpg","src":"https://p16-lp-sg.ibyteimg.com/tos-alisg-v-93bf3d-sg/a4d794b8642545ff92ef75c6033f92fa~tplv-noop.image","width":576,"height":1024,"size":0,"version":0}},"layout":{"position":"normal","margin":{"top":0,"right":0,"bottom":0,"left":0},"height":230,"width":375,"version":1},"media":{"autoplay":true,"muted":true,"global":true},"version":1,"brickIndex":"1930b81764293cab","children":[],"parent":"adaff64550b09e30","aliasName":"Видео"},"bottomplaceholder":{"name":"LpView","brickIndex":"bottomplaceholder","parent":"fe79bfc90f034bae","children":[],"bgColor":{"color":"","version":1,"type":"themeColor","themeColor":"bgPrimary"},"bgImage":{"src":"","width":0,"height":0,"size":0,"format":"jpg","version":0},"bgType":"color","visibility":"visible","alignItems":"stretch","borderRadius":0,"layout":{"position":"normal","margin":{"top":0,"left":0,"right":0,"bottom":0},"width":375,"height":68,"version":1},"version":5,"flexDirection":"column","justifyContent":"normal","boxShadow":[],"borderColor":{"type":"color","color":"rgba(255,255,255,0)","themeColor":"","version":1},"borderStyle":"solid","borderWidth":0,"flexWrap":"nowrap","events":[],"animations":{},"bgGradient":{"value":""}}}}',
#     'template_id': '7080536318425497857',
#     'title': 'Страница без названия 9/2/22, 9:53 PM',
#     'thumbnail_uri': 'tos-alisg-i-375lmtcpo0-sg/3cd9479c85cc49538b8591142f653ffc',
#     'account_id': str(id),
# }

        response = requests.post('https://ads.tiktok.com/instant_page/api/v1/create/',
                                 cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY)
        print('page_create')
        print(response.json())
        print(response.json()['data']['page_id'])
        return response.json()['data']['page_id']

    def page_publish(self, id, page_id):
        cookies = self.COOKIES
        headers = {
            'Host': 'ads.tiktok.com',
            # 'Content-Length': '36',
            'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'Dnt': '1',
            'Language': 'en',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': a.USER_AGENT,
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'X-Csrftoken': cookies['csrftoken'],
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/instant_page/editor/main?advid='+id+'&app_id=&business_type=6&external_action=5&lang=en&objective_type=3&page_id=&regions=PL&site_type=1&type=create&template_name=instantPage',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'nl-BE,nl;q=0.9,en-US;q=0.8,en;q=0.7',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'tt_webid=7120130498060600834; csrftoken=3hnIqlW6xMQWNcxdgYZd4WDl07lDGlK3; lang_type=en; tta_attr_id=0.1657784579.7120130549028487170; tta_attr_id_mirror=0.1657784579.7120130549028487170; pre_country=DE; tt_webid=7120130498060600834; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22version%22:%22v8%22}; passport_csrf_token=91fb024fdc8400822736035e591f19f7; passport_csrf_token_default=91fb024fdc8400822736035e591f19f7; sso_auth_status_ads=e57725fd22e67fb61bd6ff15305f48d4; sso_auth_status_ss_ads=e57725fd22e67fb61bd6ff15305f48d4; sso_uid_tt_ads=a96da0ce0d490e10b33485f80302bb4e3e55333e17c0bc635fd23d8189a26d68; sso_uid_tt_ss_ads=a96da0ce0d490e10b33485f80302bb4e3e55333e17c0bc635fd23d8189a26d68; toutiao_sso_user_ads=dff8d7af930edcb19168e5aec16d2f29; toutiao_sso_user_ss_ads=dff8d7af930edcb19168e5aec16d2f29; sid_ucp_sso_v1_ads=1.0.0-KDIxMGJkZGEzZGFiNzQzOGUzNDRhMDM1ZDNlNDc3ZjI3OWE1ODUzMDMKIAiCiIvKosbb52IQtJK_lgYYrwwgDDC0kr-WBjgBQOwHEAEaA3NnMSIgZGZmOGQ3YWY5MzBlZGNiMTkxNjhlNWFlYzE2ZDJmMjk; ssid_ucp_sso_v1_ads=1.0.0-KDIxMGJkZGEzZGFiNzQzOGUzNDRhMDM1ZDNlNDc3ZjI3OWE1ODUzMDMKIAiCiIvKosbb52IQtJK_lgYYrwwgDDC0kr-WBjgBQOwHEAEaA3NnMSIgZGZmOGQ3YWY5MzBlZGNiMTkxNjhlNWFlYzE2ZDJmMjk; odin_tt=e8d7b70658c178ed00def40988886fd0ccff193281b8857eba55d8fd9d8bce938f26ca71bfeb44bb7c90a1462df3dc9d75d766ea1f88015a2f0b022ae0a6d4c1; passport_auth_status_ads=9ff38c8fb5ce1702d88e69aa4b6a285e%2C; passport_auth_status_ss_ads=9ff38c8fb5ce1702d88e69aa4b6a285e%2C; sid_guard_ads=5023399f6ce814b6eda1a6b392f07340%7C1657784629%7C863999%7CSun%2C+24-Jul-2022+07%3A43%3A48+GMT; uid_tt_ads=ac917862e968837eff974c459dd14112829134a19c9ec2b26e723e8f59cdc219; uid_tt_ss_ads=ac917862e968837eff974c459dd14112829134a19c9ec2b26e723e8f59cdc219; sid_tt_ads=5023399f6ce814b6eda1a6b392f07340; sessionid_ads=5023399f6ce814b6eda1a6b392f07340; sessionid_ss_ads=5023399f6ce814b6eda1a6b392f07340; sid_ucp_v1_ads=1.0.0-KDgyNjk4OTc1Yzc0ZTcyYjBiMGNjNjU0MjgyYTdhY2QyMmExODc5MGYKGgiCiIvKosbb52IQtZK_lgYYrwwgDDgBQOwHEAEaA3NnMSIgNTAyMzM5OWY2Y2U4MTRiNmVkYTFhNmIzOTJmMDczNDA; ssid_ucp_v1_ads=1.0.0-KDgyNjk4OTc1Yzc0ZTcyYjBiMGNjNjU0MjgyYTdhY2QyMmExODc5MGYKGgiCiIvKosbb52IQtZK_lgYYrwwgDDgBQOwHEAEaA3NnMSIgNTAyMzM5OWY2Y2U4MTRiNmVkYTFhNmIzOTJmMDczNDA; msToken=5Omc7r6-nMlvmq2XDFt6r6tkjvt8ePV_1QnKtT9TINdVhlKV6M5rxVcqOT6W6vqO8HAoingiY0zHr9msfr4RrboeVJiAmJRCXdc4euBNFamxwSYz5Rv-aFxYY0TDZqT-uY4heA==; _tea_utm_cache_2777=undefined; store-idc=maliva; store-country-code=nl; lang=en; _abck=D839DC2EF8EE2881F0D907C282B909E2~-1~YAAQT9XOF9hJy/WBAQAAXgma/AjfTyHy7SGR5UTp8ggaoyb1ELBu2ZY45pzEv+qyp9LHJ3IAMBPPvH3cYLfgFUJvCZW0Z2fyLi5F5Eoc6FdtyI3r7nsHToYmi2IKBQC4Ddn2GA/xfTr9Q5GZ3y82UP+69OwQ7eG7L9UrZlw4eg4t+T1WLtemJSomwsSbDmrag/Wk6yVUBrWMRGpx6o5LX0m1XW+tv9rbc+j2avZTNmHVwDC1pE8EEt1iHE/33uuRMOxSr0W4V2esIxLv5Xzli9agwOYSv5OioETkBFMqYDCuCWoT4pzjTZWeICu6wzB+mp2cvimHjwEZlzWkGhdQes1BCrUY8IinUb3bG0B1NlcaVf77UFvMta8ox89TY6rfpk/szsxoa1yidA==~-1~-1~-1; gftoken=OTQ5NTM5OTg4fDE2NTc4MDA4ODE2Nnx8MAcHBwcHBwc; _gcl_au=1.1.1365756755.1657800889; _ga=GA1.2.111395199.1657800893; _gid=GA1.2.494020031.1657800893; _gat_UA-143770054-3=1; tta_attr_ga_cid=111395199.1657800893; _uetvid=928a1c40036e11edbba8313829e277d8; _rdt_uuid=1657800899448.cf3d6eb8-048f-4c96-8f24-d884eeba63a3; _tt_enable_cookie=1; _hjSessionUser_2525957=eyJpZCI6ImJlYWQ2NWI1LWZhYmYtNWZlOC04M2JlLWRjMDNiMTQ0N2U2OSIsImNyZWF0ZWQiOjE2NTc4MDA5MDE5OTUsImV4aXN0aW5nIjpmYWxzZX0=; _fbp=fb.1.1657800902716.173941397; _ttp=2BvyYiLS1bGrYvyJTtdRpCr4chh; _tea_utm_cache_3820=undefined; msToken=L2B2IL0z06tAmQboGottMwrFQNuQk4xg6z8DQIRIUll7pn_fu9_cVAlqEIqeRUav5BECotlD14hyCa2iWQtYCCaVUqAJxZn2GOcbIG-Spj5o_GDoQNbRQUIXHx0xhTNt0j1EMw==; i18next=en; s_v_web_id=verify_l5l08lgc_wGapJWPM_cb5D_4ET4_BDnu_WEGFrznOEAs0; part=stable; MONITOR_WEB_ID=95dc6cbc-0e4c-44be-aa29-1a79c1b60c1c; _tea_utm_cache_1583={%22campaign_id%22:1738432680724498}; _tea_utm_cache_4697={%22campaign_id%22:1738432680724498}; _tea_utm_cache_224013={%22campaign_id%22:1738432680724498}; _tea_utm_cache_345918={%22campaign_id%22:1738432680724498}; ttwid=1%7CuNap7YHz5pPNUCZ2tcjKB1Abm_vef5sKQmQmA62L7tA%7C1657898755%7Cb62cb6266539f0be7d0c576e845f572cfeac7c9c6437034c1699c1d6c35c5fde',
        }

        json_data = {
            'account_id': str(id),
        }
        response = requests.post('https://ads.tiktok.com/instant_page/api/v1/publish/' +
                                 page_id+'/', cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY)
        print(response.json())

    def vcpo(self, id):
        cookies = self.COOKIES
        seed = random.randint(0, 20)
        headers = {
            'Connection': 'close',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'TRACE-LOG-ADV-ID': str(id),
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Content-Type': 'application/json',
            'TRACE-LOG-USER-ID': str(id),
            'Accept': 'application/json, text/plain, */*',
            'AC-CSRFToken': cookies['ac_csrftoken'],
            'X-CSRFToken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+id+'&creation_type=create_new&temp_campaign_id=17274sdf15286340609&temp_adgroup_id=1727416882766849',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'uk-UA,uk;q=0.9;en-US,en;q=0.8',
        }
        json_data = {
            "185.212.205.232": 1,
            "risk_info": {
     
            }
        }

        response = requests.post("https://ads.tiktok.com/api/v3/i18n/payment/card/?aadvid="+id+"&req_src=ad_creatio",
                                 cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        slovo = str(response.json()['data']['manager_url'])
        print(response.json())
        vcp = slovo.split('=')[6]
        url = unquote(vcp)
        print(url)
        return url

    def agreement(self, id, vcpo):
        cookies = self.COOKIES
        seed = random.randint(0, 20)
        headers = {
            'Connection': 'close',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'TRACE-LOG-ADV-ID': str(id),
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Content-Type': 'application/json',
            'TRACE-LOG-USER-ID': str(id),
            'Accept': 'application/json, text/plain, */*',
            'AC-CSRFToken': cookies['ac_csrftoken'],
            'X-CSRFToken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'uk-UA,uk;q=0.9;en-US,en;q=0.8', }
        json_data = {"appId": "1583", "token": "" +
                     vcpo+"", "protocolIds": [5001, 5002]}

        response = requests.post("https://ads.tiktok.com/upay/i18n/protocol/authorize_init",
                                 cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        print('Agreement')
        AgreementId = str(response.json()['data']['agreementId'])
        print(AgreementId)
        return str(AgreementId)

    def paypal_link(self, id, vcpo, agreement):
        cookies = self.COOKIES
        seed = random.randint(0, 20)
        headers = {
            'Connection': 'close',
            'Content-Length': '1082',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'TRACE-LOG-ADV-ID': str(id),
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Content-Type': 'application/json',
            'TRACE-LOG-USER-ID': str(id),
            'Accept': 'application/json, text/plain, */*',
            'AC-CSRFToken': cookies['ac_csrftoken'],
            'X-CSRFToken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ads.tiktok.com/i18n/creation/creative?aadvid='+str(id)+'&creation_type=create_new&temp_campaign_id=1727415286340609&temp_adgroup_id=1727416882766849',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'uk-UA,uk;q=0.9;en-US,en;q=0.8', }
        json_data = {"token": ""+vcpo+"", "upaySessionId": "a5993ce7-6a0d-4534-bc12-"+id, "refId": "2880071e-cd51-47af-"+id, "returnUrl": "https://ads.tiktok.com/wpay/oversea/result?invokerID=upay_f67efed623c241dsf7fffb045c885e40&from=createInManager&uniqueId=df9e12d5-db04-97a9-9237-"+id, "payWay": 31, "agreementId": ""+agreement+"", "riskInfo": "{\"uid\":\""+id+"\",\"aid\":\"1583\",\"app_id\":\"1583\",\"app_name\":\"tiktokads\",\"did\":\"1267211990472438274\",\"ip_address\":\"38.155.113.17\",\"forwarded\":\"\",\"device_platform\":\"web\",\"session_aid\":\"1583\",\"priority_region\":\""+a.COUNTRY+"\",\"user_agent\":\""+a.USER_AGENT+"\",\"referer\":\"https://business.tiktok.com/\",\"cookie_enabled\":true,\"screen_width\":1366,\"screen_height\":768,\"browser_language\":\"en-EN\",\"browser_platform\":\"Win32\",\"browser_name\":\"Mozilla\",\"browser_version\":\"" +
                     a.USER_AGENT+"\",\"browser_online\":true,\"timezone_name\":\""+a.TIME_ZONE_NAME+"\",\"device_fingerprint_id\":\"bdff09f5-64d6-45b0-a0ac-194d73c01caf"+str(id)+"\",\"pay_type\":\"2\",\"ads_type\":\"1\",\"account_id\":\"7060480403647234050"+id+"\",\"account_create_days\":\"140\",\"first_pay_success_days\":\"36\",\"pay_three_month_ago\":\"FALSE\",\"last_pay_success_days\":\"1\",\"merchant_user_country\":\""+a.COUNTRY+"\",\"target\":\"704041919010\",\"target_type\":\"0\",\"carrier_region\":\""+a.COUNTRY+"\",\"app_region\":\""+a.COUNTRY+"\",\"sys_region\":\""+a.COUNTRY+"\",\"app_language\":\""+a.COUNTRY+"\",\"sys_language\":\""+a.COUNTRY+"\"}", "riskAmount": "", "cardType": 1, "terminalEquip": 4, "currency":"UAH"}


#         json_data = {
#     'token': vcpo,
#     'upaySessionId': '7df23c1b-e217-4945-a5f6-263340242bef',
#     'refId': '4a99bfc9-e464-4403-a83e-1e9381d6a4d6',
#     'returnUrl': 'https://ads.tiktok.com/wpay/oversea/result?invokerID=upay_f67efed623c24192ee4791d777fffb045c885e40&from=createInManager&uniqueId=76a0f363-1479-0ac1-0d34-352a9f1a0055',
#     'payWay': 31,
#     'agreementId': agreement,
#     'riskInfo': '{"uid":"7116713158793954306","aid":"1583","app_id":"1583","app_name":"tiktokads","did":"7116782218697541122","ip_address":"46.211.87.60","forwarded":"46.211.87.60, 2.18.29.103, 23.193.97.45,10.245.100.84","device_platform":"web","session_aid":"1583","priority_region":"VN","user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36","referer":"","cookie_enabled":true,"screen_width":1360,"screen_height":768,"browser_language":"uk-UA","browser_platform":"Win32","browser_name":"Mozilla","browser_version":"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36","browser_online":true,"timezone_name":"Europe/Kiev","device_fingerprint_id":"b7dd9fd3-9ba0-403f-8e63-87e963061f07","pay_type":"2","ads_type":"1","account_id":"7117371004665544705","account_create_days":"0","first_pay_success_days":null,"pay_three_month_ago":"FALSE","last_pay_success_days":null,"merchant_user_country":"VN","target":"7116713158793954306","target_type":"0","carrier_region":"VN","app_region":"VN","sys_region":"VN","app_language":"en","sys_language":"en","account_last_modified":"2022-07-06T21:15:56Z","unique_account_identifier":"7117371004665544705","account_registration_date":"2022-07-06T21:15:56Z","webid":"1%7CVwed9aInstc1Ndj4F419aLjYM0i2gI0_0w_Yp-dd5oU%7C1657142272%7C18ff4fd5bb857cc103a88d8987ca95a3f46302135ec891009f12822559682305"}',
#     'riskAmount': None,
#     'cardType': 1,
#     'terminalEquip': 4,
# }

        response = requests.post("https://ads.tiktok.com/upay/i18n/protocol/bind_pay_way_authorize",
                                 cookies=cookies, headers=headers, json=json_data, proxies=self.PROXY, timeout=50)
        print('Paypal')
        print(response.json())
        paypal_url = str(response.json()['data']['url'])
        print(paypal_url)
        return paypal_url

    # def Add_Payment(self, data):
    #     res = requests.post("http://localhost:7000/api/account/paymentMethod/add/"+str(data["advertiser_id"]), json= {
    #         'advertiser_id':data["advertiser_id"],
    #         'cookies':data["cookies"],
    #         'user_agent':data["user_agent"],
    #         'proxy':data["proxy"],
    #         "cardholdername":data["cardholdername"],
    #         "number_card":data["number_card"],
    #         "cvv":data["cvv"],
    #         "expiration_month":data["expiration_month"],
    #         "expiration_year":data["expiration_year"]
    #     }
    #     )
    #     account_data["biz_id"] = res.json()["biz_id"]


    def webid(self):
        cookies = self.COOKIES
        import requests

        headers = {
            'authority': 'sgali-mcs.byteoversea.com',
            'accept': '*/*',
            'accept-language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json; charset=UTF-8',
            'origin': 'https://ads.tiktok.com',
            'referer': 'https://ads.tiktok.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': str(a.USER_AGENT),
        }

        json_data = {
            'app_id': 2740,
            'url': 'https://ads.tiktok.com/i18n/signup?redirect=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Fhome',
            'user_agent': str(a.USER_AGENT),
            'referer': 'https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Fhome',
            'user_unique_id': '',
        }

        response = requests.post('https://sgali-mcs.byteoversea.com/webid', headers=headers,
                                 verify=True, json=json_data, proxies=self.PROXY, cookies=cookies)
        print('WEBID: '+str(response.json()['web_id']))
        return str(response.json()['web_id'])

    def creative_create(self, ident_id, ad_ids, id, pixel_id, nomer, PixelCode, url, creo_text, page_id, nomer2, call_to_action):
        cookies = self.COOKIES
        headers = {
          
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'TRACE-LOG-ADV-ID': str(id),
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Content-Type': 'application/json',
            'TRACE-LOG-USER-ID': str(id),
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            'Accept-Encoding': 'gzip, deflate',
       
            }
       

        json_data = {
            'ad_ids': [
                ad_ids,
            ],
            'inventory_flow': [
                3000,
            ],
            'inventory_flow_type': 57,
         
            'objective_type': 3,
            'creative_material_mode': 2,
             'risk_info': {
              
            },
            'playable_url': '',
            'coming_source_type': 57,
            "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
            'creative_info': {
                'video_list': [
                   
    
 
                    {
                        "opt_status": 0, 
                        "status": 43,
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            "opt_status": 0, 
                        "status": 43,
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
              "opt_status": 0, 
                        "status": 43,
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'advanced_creative_type':'54',
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
                    {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    },
 
                ],
                  'ad_channel': 57,
            },
        }
        res = requests.post("https://ads.tiktok.com/api/v2/i18n/perf/creative/create/?aadvid="+id +
                            "&req_src=ad_creatio", headers=headers, proxies=self.PROXY, json=json_data, cookies=cookies, timeout=50)
        print("Creative")
        print(res.json())
        # str(res.json()['data']['ad_and_creative_ids'][0]['creative_ids'][0])
        return "null"

    def creative_check(self, ident_id, ad_ids, id, pixel_id, nomer, PixelCode, url, creo_text, page_id, nomer2, call_to_action):
        cookies = self.COOKIES
        headers = {
          
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'TRACE-LOG-ADV-ID': str(id),
            'sec-ch-ua-mobile': '?0',
            'User-Agent': a.USER_AGENT,
            'Content-Type': 'application/json',
            'TRACE-LOG-USER-ID': str(id),
            'Accept': 'application/json, text/plain, */*',
            'X-CSRFToken': cookies['csrftoken'],
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://ads.tiktok.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': '',
            'Accept-Encoding': 'gzip, deflate',
       
            }
       

        json_data = {
            'ad_ids': [
                ad_ids,
            ],
            'inventory_flow': [
                3000,
            ],
            'inventory_flow_type': 1,
         
            'objective_type': 3,
            'creative_material_mode': 2,
             'risk_info': {
              
            },
            'playable_url': '',
            'coming_source_type': 1,
            "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
            'creative_info': {
                'video_list': [
                   
    
 {
                        
                        'creative_name': self.cr['data']['material_infos'][nomer]['base_info']['material_name']+id,
                        'app_name': '',
                        'source': 'Birdilan',
                        'title': creo_text,
                        'call_to_action': call_to_action,
                        'avatar_icon': {
                            'url': '',
                            'width': 0,
                            'web_uri': '',
                            'height': 0,
                        },
                        'image_info': [
                            {
                                'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                                'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                                'web_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                                'url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            },
                        ],
                        'video_info': {
                            'name': 'video_2022-10-09_09-05-02.mp4'+str(id),
                            'size': 406502,
                            'width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'bitrate': 625254,
                            'duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'cover_url': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'pre_vid': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'status': 2,
                            'thumb_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                            'thumb_width': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['width'],
                            'thumb_height': self.cr['data']['material_infos'][nomer]['base_info']['resolution']['height'],
                            'video_id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_unique': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'video_name': 'video_2022-10-09_09-05-02.mp4',
                            'video_duration': self.cr['data']['material_infos'][nomer]['base_info']['duration'],
                            'create_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['create_time'],
                            ],
                            'businesses': [
                                1,
                            ],
                            'modify_time': [
                                self.cr['data']['material_infos'][nomer]['base_info']['modify_time'],
                            ],
                               "creative_is_viewable": "1",
             "creative_inventory_status": "1",
              "creative_explore_status": "0",
              "primary_status": "delivery_ok",
               "audit_result_type": 1,
                  "audit_status": 1,
                            'id': self.cr['data']['material_infos'][nomer]['base_info']['video_id'],
                            'md5': self.cr['data']['material_infos'][nomer]['base_info']['material_cover']+id,
                            'origin_uid': id,
                            'verify': {
                                'supported': [
                                    {
                                        'key': 3000,
                                        'icon': 'https://lf16-ttmp.byteintlstatic.com/obj/goofy-sg/biz_manager_creation/statics/images/placement-ttd6f58c00.png',
                                        'label': 'Aplikacja',
                                        'status': True,
                                        'message': [],
                                        'verify_code': 0,
                                        'verify_code_list': [],
                                    },
                                ],
                                'unsupported': [],
                                'all_pass': True,
                                'all_reject': False,
                                'all_msg': '',
                                'error_msgs': [],
                                'fix_it_synchro_list': [],
                            },
                            'play_url': '',
                            'is_player': False,
                            'video_loading': False,
                            'vidio_init_ready': False,
                        },
                        'is_creative_authorized': False,
                        'item_source': 0,
                        'struct_version': 1,
                        'image_mode': 15,
                        'identity_id': ident_id,
                        'identity_type': 1,
                        'is_open_url': 0,
                        'open_url': '',
                        'auto_open': 0,
                        'fallback_type': 0,
                        'external_url': url,
                        'schema_type': '',
                        'track_url': [],
                        'action_track_url': [],
                        'vast_moat': 0,
                        'vast_double_verify': 0,
                        'vast_ias': False,
                        'vast_url': '',
                        'brand_safety_postbid_partner': 0,
                        'external_url_domain': '',
                        'brand_safety_vast_url': '',
                        'tracking_pixel_id': '',
                        'tracking_app_id': '0',
                        'tracking_offline_event_set_ids': [],
                        'card_id': '',
                        "urls_precheck_result": {
                        "material_results": [],
                        "summary_results": [],
                        "success": True
                    },
                        'page_id': page_id,
                        'format_structure': 0,
                        'cover_uri': self.cr['data']['material_infos'][nomer]['base_info']['material_cover'],
                    }
 
                    
 
                ],
                  'ad_channel': 1,
            },
        }
        res = requests.post("https://ads.tiktok.com/api/v2/i18n/perf/creative/check/?aadvid="+id +
                            "&req_src=ad_creatio", headers=headers, proxies=self.PROXY, json=json_data, cookies=cookies, timeout=50)
        print("Creative check")
        print(res.json())
        # str(res.json()['data']['ad_and_creative_ids'][0]['creative_ids'][0])
        return "null"

def user_agent_rand():
    user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Vivaldi/4.3', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363']

    seed = random.randint(0, len(user_agent_list))
    return str(user_agent_list[seed])


def country_rand():
    country_list = ['PT', 'CH', 'AE', 'IL']
    seed = random.randint(0, len(country_list))
    return str(country_list[seed])


time_zone_list = [
    'Pacific/Wake',
    'Pacific/Apia',
    'Pacific/Apia',
    'Pacific/Honolulu',
    'America/Anchorage',
    'America/Los_Angeles',
    'America/Phoenix',
    'America/Chihuahua',
    'America/Chihuahua',
    'America/Chihuahua',
    'America/Denver',
    'America/Managua',
    'America/Chicago',
    'America/Mexico_City',
    'America/Mexico_City',
    'America/Mexico_City',
    'America/Regina',
    'America/Bogota',
    'America/New_York',
    'America/Indiana/Indianapolis',
    'America/Bogota',
    'America/Bogota',
    'America/Halifax',
    'America/Caracas',
    'America/Caracas',
    'America/Santiago',
    'America/St_Johns',
    'America/Sao_Paulo',
    'America/Argentina/Buenos_Aires',
    'America/Argentina/Buenos_Aires',
    'America/Godthab',
    'America/Noronha',
    'Atlantic/Azores',
    'Atlantic/Cape_Verde',
    'Africa/Casablanca',
    'Europe/London',
    'Europe/London',
    'Europe/London',
    'Africa/Casablanca',
    'Europe/Berlin',
    'Europe/Belgrade',
    'Europe/Sarajevo',
    'Europe/Istanbul',
    'Europe/Bucharest',
    'Asia/Baghdad',
    'Asia/Riyadh',
    'Europe/Moscow',
    'Asia/Muscat',
    'Asia/Tbilisi']


proxy_list = [{"IP": "203.176.129.79", "PORT": "33427", "ANON": "Elite", "COUNTRY": "Cambodia", "ISO": "KH", "PING": 192}, {"IP": "192.111.130.2", "PORT": "4145", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 176}, {"IP": "192.252.220.92", "PORT": "17328", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 168}, {"IP": "192.111.135.18", "PORT": "18301", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 161}, {"IP": "192.252.208.70", "PORT": "14282", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 193}, {"IP": "192.252.211.197", "PORT": "14921", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 223}, {"IP": "192.111.135.17", "PORT": "18302", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 189}, {"IP": "192.252.215.5", "PORT": "16137", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 203}, {"IP": "178.217.215.45", "PORT": "1080", "ANON": "Elite", "COUNTRY": "Ukraine", "ISO": "UA", "PING": 163}, {"IP": "62.109.18.23", "PORT": "1080", "ANON": "Elite", "COUNTRY": "Russia", "ISO": "RU", "PING": 333}, {"IP": "45.77.168.25", "PORT": "1080", "ANON": "Elite", "COUNTRY": "Singapore", "ISO": "SG", "PING": 199}, {"IP": "192.111.139.165", "PORT": "4145", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 93}, {"IP": "190.121.21.211", "PORT": "1080", "ANON": "Elite", "COUNTRY": "Chile", "ISO": "CL", "PING": 282}, {"IP": "198.8.94.170", "PORT": "4145", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 122}, {"IP": "192.111.129.145", "PORT": "16894", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 124}, {"IP": "93.177.198.114", "PORT": "5678", "ANON": "Elite", "COUNTRY": "Latvia", "ISO": "LV", "PING": 170}, {"IP": "192.111.137.35", "PORT": "4145", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 234}, {"IP": "161.97.169.216", "PORT": "1080", "ANON": "Elite", "COUNTRY": "Germany", "ISO": "DE", "PING": 304}, {
    "IP": "198.8.94.174", "PORT": "39078", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 347}, {"IP": "192.111.130.5", "PORT": "17002", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 395}, {"IP": "5.44.41.80", "PORT": "61400", "ANON": "Elite", "COUNTRY": "Russia", "ISO": "RU", "PING": 361}, {"IP": "103.250.166.12", "PORT": "6667", "ANON": "Elite", "COUNTRY": "India", "ISO": "IN", "PING": 372}, {"IP": "192.252.208.67", "PORT": "14287", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 184}, {"IP": "192.252.214.20", "PORT": "15864", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 309}, {"IP": "192.111.137.34", "PORT": "18765", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 304}, {"IP": "67.201.33.9", "PORT": "25280", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 377}, {"IP": "103.80.118.242", "PORT": "51080", "ANON": "Elite", "COUNTRY": "India", "ISO": "IN", "PING": 270}, {"IP": "192.252.209.155", "PORT": "14455", "ANON": "Elite", "COUNTRY": "Canada", "ISO": "CA", "PING": 327}, {"IP": "192.111.139.162", "PORT": "4145", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 206}, {"IP": "51.155.3.184", "PORT": "33427", "ANON": "Elite", "COUNTRY": "United Kingdom", "ISO": "GB", "PING": 281}, {"IP": "150.230.211.254", "PORT": "1080", "ANON": "Elite", "COUNTRY": "Japan", "ISO": "JP", "PING": 193}, {"IP": "31.25.92.5", "PORT": "44949", "ANON": "Elite", "COUNTRY": "Iran", "ISO": "IR", "PING": 171}, {"IP": "46.101.227.75", "PORT": "1123", "ANON": "Elite", "COUNTRY": "Germany", "ISO": "DE", "PING": 301}, {"IP": "192.111.139.163", "PORT": "19404", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 273}, {"IP": "192.111.138.29", "PORT": "4145", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 398}, {"IP": "192.111.137.37", "PORT": "18762", "ANON": "Elite", "COUNTRY": "United States", "ISO": "US", "PING": 205}]


def change_ip():
    res = requests.get(
        'http://217.77.218.120:8000/api/devices/modem/reconnect?token=c9ee166935c27b8bce127ef7ae134f65919b2888&id=165')
    time.sleep(7)
    print(res.json())


def telegram_bot_sendtext(bot_message):

    bot_token = '5304793319:AAFX8f9mvzgSNS9yq5e91dN7syd9OUC3Nxg'
    bot_chatID = '1810907603'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def EC(ba_token, cookies):

    headers = {
        'authority': 'www.paypal.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,tr;q=0.5,ar;q=0.4',
        'cache-control': 'no-cache',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'KHcl0EuY7AKSMgfvHl7J5E7hPtK=-5kveJbN5HFm6yW_zzyTqVyy8AdGgqbycXfS-2sEJ1zx1UPoaiYZKZShrpfPlbdr67FqTOoR9hThHBvS; cookie_check=yes; _gcl_au=1.1.698944521.1641948500; d_id=182b7197bedb4e3ba25728e8ebe16cc11644235631472; cookie_prefs=P%3D1%2CF%3D1%2Ctype%3Dimplicit; _ga=GA1.2.1917535482.1648927189; _gid=GA1.2.1615344086.1650033282; login_email=misterbinaao98%40gmail.com; feel_cookie=a%2013%20_merchant-hub%20b%200%20%20c%206%20webscr%20d%200%20%20e%2044%20Merchant%2fsubscriptions%2fMerchantDashBoard.xsl%20f%200%20%20g%205%20en_US%20h%200%20%20i%2044%20xpt%2fMerchant%2fsubscriptions%2fMerchantDashBoard%20j%200%20%20k%2037%20Recurring%20payments%20dashboard%20-%20PayPal%20l%200%20%20; s_pers=%20tr_p1%3Dmf%253Amerchantdashboard%7C1651972136866%3B%20s_fid%3D6194FA75B1560591-20A1AECEF51A5552%7C1715128745748%3B%20gpv_c43%3Dmf%253Amerchantdashboard%7C1651972145760%3B%20gpv_events%3Dno%2520value%7C1651972145768%3B; navlns=0.3.3.11; TfXMWj95u2_Zf1Kmv_GCUOjlGG8=d_p6oNzXCWrx0Yh9ZDh8iyC47ygaIpVgZYUgJPBF6c0N2g_mZVXXHXiYcTeaeb4AzxdhLJd2UOyiW6PKJh3wpSEsNXogw4v6PvZ-mP4JGC2eS5T45ePneNFISRRF73emPHw80PAFzEcacucSFinKJjCA2zikj6cdlVjVKcRamLhhibejoDmyw4XB2vm; ui_experience=login_type%3DEMAIL_PASSWORD%26tokenType%3Dsms_otp%26tokenIdentifier%3D93bq7LFZSsYMnN0PO0UBt41e4FgQzjFTdeorTC6yT77bpAdP162nT60T_wV87Z8fCYcm1W%26home%3D2%26login_preference%3Dpassword_login%26ota%3Dtrue%26ot_priority%3Dpaypal; TLTSID=11732606105442565710410338650823; DPz73K5mY4nlBaZpzRkjI3ZzAY3QMmrP=; AV894Kt2TSumQQrJwe-8mzmyREO=; rmuc=DGpp6jrbGoDAmedsfHLkpQhbjRl4jVemc1kt5VTtpxwKG5NyhRtAqOSvNXLpoxOJs7ag3EU5TVOShlweqgnv_gMpS8_w3XtY4y4gAjrdpG6S5aTfIRquXIUsaWUwLCABHWGx8BE_JE0mo0-nB2XmQWXx1IRIu9Sf1U7wUmDAwCrGR36evVL3gGmFlComFZgUG23BOm; nsid=s%3ATTA0jfX8AqBfN5KOwB0WwxJLael5OxqW.cRM1Vl0w1hKMKSIeuk5lMzh4XnO88cWAvJclNRUf34E; Obsh1bpwTE8slCzy4X2PwOLmhre=; LANG=en_US%3BUA; SEGM=; ts_c=vr%3Dd44d15ef17d0a788747d8d70f7ee90aa%26vt%3Ded4958e91800ad045874b66dfa18446f; fn_dt=027ef0ec44114e139d8a6d90cdfce82d; id_token=idtoken9bf1606f1cef4963b765c2d1ce4ed16a; X-PP-ADS=AToBnl5gYh4k.zflZtydJEMpzk3ewRE7Abw1c2L8RsK9gVqtOqhg85KcVq4eOwHNkYpiIxYsqCGki1pK8wCDki3Czg; l7_az=dcg13.slc; _gat_gtag_UA_53389718_12=1; HaC80bwXscjqZ7KM6VOxULOB534=nqGP8QI0LqJ4YWIXURpxYOBdx6c7FiDkViExRZVHom1FZEvmebZII0n9PWSsMs_R2QECpHZfzrifzpBCnJQf2e2RUt9WenNRpiRy9ohn-fyR3RI2Cms8lGCPWA_xgZdipkeLNG; ts=vreXpYrS%3D1747944863%26vteXpYrS%3D1653252263%26vr%3Dd44d15ef17d0a788747d8d70f7ee90aa%26vt%3Ded4958e91800ad045874b66dfa18446f%26vtyp%3Dreturn; tsrce=checkoutuinodeweb; x-pp-s=eyJ0IjoiMTY1MzI1MDQ2Mzc0NSIsImwiOiIwIiwibSI6IjAifQ',
        'pragma': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    }

    params = {
        'ba_token': ba_token,
        'billingLite': '1',
    }

    response = requests.get('https://www.paypal.com/agreements/approve',
                            params=params, cookies=cookies, headers=headers)

    # with open('pp.html') as file:
    # src = file.read()
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find_all('script')[5].string

    s = result.partition('fltk')[-1]
    b = s.partition('"})')[0]
    ec = b.split('=')[1]
    print(b.split('=')[1])
    return ec


def approve(bc, cookies, headers, card):

    # headers = {
    # 'authority': 'www.paypal.com',
    # 'accept': '*/*',
    # 'x-paypal-internal-euat': '4ZvitsBLsGkZdMpGCrHm5jX6jADs_IZRSJYf9RzrdO4dYpe-CejGZCz8SQ06zJOezipvHqElDJRhSa1iCe-SePWeK1EQHUEXwxjs9Ghtwk6bnsYPNsBOSNuqOinSsOlAupBtyG',
    # 'paypal-client-metadata-id': 'EC-66049547XN927532H',
    # 'x-app-name': 'checkoutuinodeweb',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    # # Already added when you pass json=
    # # 'content-type': 'application/json',
    # 'origin': 'https://www.paypal.com',
    # 'sec-fetch-site': 'same-origin',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-dest': 'empty',
    # 'referer': 'https://www.paypal.com/agreements/approve?ba_token=BA-58Y4396414769681P&billingLite=1',
    # 'accept-language': 'uk-UA,uk',
    # # Requests sorts cookies= alphabetically
    # # 'cookie': 'cookie_check=yes; _gcl_au=1.1.757692968.1653842199; _ga=GA1.2.775025521.1653842199; _gid=GA1.2.317834771.1653842199; KHcl0EuY7AKSMgfvHl7J5E7hPtK=6Uf0tDGBnZP1bbKj-VaixIkjXa7R9nmxWspssZO__-vNXVA90rkzk_fxp71zJXz7VVHhfUFoYGfzXjXY; TLTSID=36902179567729341886580333492381; login_email=paypal%40avtozalivtiktok.com; d_id=36d2bb65a0ee4b329ea637a2c5113ce21653844755467; ui_experience=login_type%3DEMAIL_PASSWORD%26home%3D2; rmuc=QS6tlOdoArBxiVXAT4K6OyH4fBFueQtwMwOdLxTnQDj24akKmh64fziB4P-UmYbWZvYLEKK_sF7-Ssh7XgQVBsFgEQa1p-wFLTpKTi9LF5rysJZJw__dRE3LZeIYBt2L1s9knRayl1hi6GOz3DKo6A7GhVv66LtcOmCnJqm3gVi_6ScxjJWtVYJp4uH8wiOaE_FDiW; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6Im1fUV9jLUx5T3p3SGVWT3hoVnp3ZjljcEk0eHp5UnhuNlkwWjhiMWFjSlFZZ3pac3FNR2ZTV3c2RkhSc3ZRSG9SUGZja0FFaVk4MzJlN0FjNHZyZnJkODMySmx3SHRYYVBpU0cxb3JMaXdfVXRiWE54WWhGTG0wcXpOWkZrTE9CeHlHd1hMMS1Ic2hTRmljWmE3WXYwclNkSk4xMC1xY1FBSzVlQ2RoQjVacFJPaWZpcFN1Tk80SHM2QUciLCJpYXQiOjE2NTQwNzk3NzMsImV4cCI6MTY1NDA4MzM3M30.o4xqa4t64acYpkmeLOh52GEmZSJhbs8qMKqE1B95CyY; LANG=ru_RU%3BUA; nsid=s%3AhKHknBE1NG1dV9JDuADFybOFddkd09pW.J%2BGYv%2F4olFynvhVV9S3cWK7HGRzpXVu3DkZe1eJXZk0; ts_c=vr%3D10ad1a411810a7887304ae2bf9898332%26vt%3D2b3b821a1810a7a068e88825f896f1ee; fn_dt=6459caefa6234176be851ebd8106f92c; id_token=idtoken2e716633f76b4103948927faac7db1dc; X-PP-ADS=AToBeW2aYleJe4-W3Z7PrMJslalrRqY; SEGM=bRdV1vB0ebq9RKdAb3xSHowCi6QnnlCiDOLNk8i1mAuLl1vTbzHQwWajSsMe8mvoWiJtY1GnpzN4Y-sixGy7BQ; HaC80bwXscjqZ7KM6VOxULOB534=ZzAK0IDPx6k8KyFXZty5cGXbX2hlrExGlEkb6Jm_2WfFqpMKITSMqLXhl-zHYLUioA9zahYmgLyqjHtq_arOAHh0oaOiT6MbFF-xEqs8Hd8JI9S8I2DMd0_e_i2ZTyKken25VG; l7_az=dcg14.slc; tsrce=checkoutuinodeweb; _gat_gtag_UA_53389718_12=1; x-pp-s=eyJ0IjoiMTY1NDI4ODQwNjc1MSIsImwiOiIwIiwibSI6IjAifQ; ts=vreXpYrS%3D1748982826%26vteXpYrS%3D1654290226%26vr%3D10ad1a411810a7887304ae2bf9898332%26vt%3D2b3b821a1810a7a068e88825f896f1ee%26vtyp%3Dreturn; tcs=main%3Axo%3Alite%7CconsentButton',
    # }

    json_data = [
        {
            'operationName': 'authorize',
            'variables': {
                'billingAgreementId': bc,
                'fundingPreference': {
                    'fundingOptionId': card,
                },
            },
            'query': 'mutation authorize($billingAgreementId: String!, $addressId: String, $fundingPreference: billingFundingPreferenceInput) {\n  billing {\n    authorize(\n      billingAgreementId: $billingAgreementId\n      addressId: $addressId\n      fundingPreference: $fundingPreference\n    ) {\n      billingAgreementToken\n      paymentAction\n      returnURL {\n        href\n        __typename\n      }\n      buyer {\n        userId\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
        },
    ]

    response = requests.post('https://www.paypal.com/graphql/',
                             cookies=cookies, headers=headers, json=json_data)
    # print(response.json())
    url = response.json()[
        0]['data']['billing']['authorize']['returnURL']['href']
    return str(url)


def call(token, ba, id, url, cookies):

    headers = {
        'Host': 'f-p.sgsnssdk.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,tr;q=0.5,ar;q=0.4',
        # 'Cookie': 'MONITOR_WEB_ID=fffb2911-9be1-4e4b-90e4-f01c284237a5',
        'Connection': 'close',
    }

    params = {
        'redirect_url': url,
        'collect_request_id': id,
        'channel_id': 'paypal_reference_hk01',
        'token': token,
        'ba_token': ba,
    }

    response = requests.get('http://f-p.sgsnssdk.com/callback/paypal_reference/reference_redirect',
                            params=params, cookies=cookies, headers=headers)
    print(response.text)


def finish(token, cookies):

    headers = {
        'Host': 'www.paypal.com',
        'Connection': 'close',
        # 'Content-Length': '924',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'x-app-name': 'checkoutuinodeweb',
        # Already added when you pass json=
        # 'Content-type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Accept': '*/*',
        'Origin': 'https://www.paypal.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.paypal.com/agreements/approve?ba_token=BA-0UM398768X349163F&billingLite=1',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,tr;q=0.5,ar;q=0.4',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'KHcl0EuY7AKSMgfvHl7J5E7hPtK=-5kveJbN5HFm6yW_zzyTqVyy8AdGgqbycXfS-2sEJ1zx1UPoaiYZKZShrpfPlbdr67FqTOoR9hThHBvS; cookie_check=yes; _gcl_au=1.1.698944521.1641948500; d_id=182b7197bedb4e3ba25728e8ebe16cc11644235631472; cookie_prefs=P%3D1%2CF%3D1%2Ctype%3Dimplicit; _ga=GA1.2.1917535482.1648927189; _gid=GA1.2.1615344086.1650033282; login_email=misterbinaao98%40gmail.com; feel_cookie=a%2013%20_merchant-hub%20b%200%20%20c%206%20webscr%20d%200%20%20e%2044%20Merchant%2fsubscriptions%2fMerchantDashBoard.xsl%20f%200%20%20g%205%20en_US%20h%200%20%20i%2044%20xpt%2fMerchant%2fsubscriptions%2fMerchantDashBoard%20j%200%20%20k%2037%20Recurring%20payments%20dashboard%20-%20PayPal%20l%200%20%20; s_pers=%20tr_p1%3Dmf%253Amerchantdashboard%7C1651972136866%3B%20s_fid%3D6194FA75B1560591-20A1AECEF51A5552%7C1715128745748%3B%20gpv_c43%3Dmf%253Amerchantdashboard%7C1651972145760%3B%20gpv_events%3Dno%2520value%7C1651972145768%3B; navlns=0.3.3.11; TfXMWj95u2_Zf1Kmv_GCUOjlGG8=d_p6oNzXCWrx0Yh9ZDh8iyC47ygaIpVgZYUgJPBF6c0N2g_mZVXXHXiYcTeaeb4AzxdhLJd2UOyiW6PKJh3wpSEsNXogw4v6PvZ-mP4JGC2eS5T45ePneNFISRRF73emPHw80PAFzEcacucSFinKJjCA2zikj6cdlVjVKcRamLhhibejoDmyw4XB2vm; ui_experience=login_type%3DEMAIL_PASSWORD%26tokenType%3Dsms_otp%26tokenIdentifier%3D93bq7LFZSsYMnN0PO0UBt41e4FgQzjFTdeorTC6yT77bpAdP162nT60T_wV87Z8fCYcm1W%26home%3D2%26login_preference%3Dpassword_login%26ota%3Dtrue%26ot_priority%3Dpaypal; TLTSID=11732606105442565710410338650823; DPz73K5mY4nlBaZpzRkjI3ZzAY3QMmrP=; AV894Kt2TSumQQrJwe-8mzmyREO=; rmuc=DGpp6jrbGoDAmedsfHLkpQhbjRl4jVemc1kt5VTtpxwKG5NyhRtAqOSvNXLpoxOJs7ag3EU5TVOShlweqgnv_gMpS8_w3XtY4y4gAjrdpG6S5aTfIRquXIUsaWUwLCABHWGx8BE_JE0mo0-nB2XmQWXx1IRIu9Sf1U7wUmDAwCrGR36evVL3gGmFlComFZgUG23BOm; nsid=s%3ATTA0jfX8AqBfN5KOwB0WwxJLael5OxqW.cRM1Vl0w1hKMKSIeuk5lMzh4XnO88cWAvJclNRUf34E; Obsh1bpwTE8slCzy4X2PwOLmhre=; LANG=en_US%3BUA; SEGM=; ts_c=vr%3Dd44d15ef17d0a788747d8d70f7ee90aa%26vt%3Ded4958e91800ad045874b66dfa18446f; fn_dt=027ef0ec44114e139d8a6d90cdfce82d; id_token=idtoken9bf1606f1cef4963b765c2d1ce4ed16a; X-PP-ADS=AToBnl5gYh4k.zflZtydJEMpzk3ewRE7Abw1c2L8RsK9gVqtOqhg85KcVq4eOwHNkYpiIxYsqCGki1pK8wCDki3Czg; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbiI6ImxYdTZ1MklPYmZqdF9XVUxyMjItcDQxLTcxU1lSbmlPVVBIaDVkbzRzMDV3bHplckx1MTRiWWhMZ3VjbHAyTjByOTVoZXVoQjBmOTlwaDZ2MTdvbTE3MFM3aUdkdVVMcGM0ZWlVQUhtSkFsc0x6STMxYjM3Vm9MZ1dNa1BXbzhSR19TT05NcUIyeWpfc0YxZWdsRi1jaWt4aHZlNkEtTWRFczYxX0VEZU5NX2dITjhIcVpqOGlqYml3cVk4UHZRNU5WQmdpU3hLVzE1OEk2cHQ4ZFZ5RnU2Vm10RyIsImlhdCI6MTY1MzI1NTgxMSwiZXhwIjoxNjUzMjU5NDExfQ.uzt54f-WE_vHxgWOJp1h6UDinork7XUtKHVlZIiFP8c; HaC80bwXscjqZ7KM6VOxULOB534=zc_-ofiycNy3gCV2M3HVdDK5gIYrtg71kwi4Fi0IDjKjouhpTIaZyu1ibXXYyz-woQOpbXBCsYAW-nt2Dc6taXcthQLIHBw-j3Sh78GfPn8GukIx37hc-cp8CGF_DvrZ1TIA5G; l7_az=dcg13.slc; _gat_gtag_UA_53389718_12=1; tcs=main%3Axo%3Alite%7CconsentButton; tsrce=checkoutuinodeweb; ts=vreXpYrS%3D1747951267%26vteXpYrS%3D1653258667%26vr%3Dd44d15ef17d0a788747d8d70f7ee90aa%26vt%3Ded4958e91800ad045874b66dfa18446f%26vtyp%3Dreturn; x-pp-s=eyJ0IjoiMTY1MzI1Njg2Nzc2OSIsImwiOiIwIiwibSI6IjAifQ',
    }

    json_data = {
        'events': [
            {
                'level': 'info',
                'event': 'window_unload',
                'payload': {
                    'timestamp': 1653256875147,
                    'windowID': '5d818a9d68',
                    'pageID': 'f4f0e4135d',
                    'token': token,
                    'buyer_type': 'Existinguser',
                    'context_id': token,
                    'context_type': 'EC-token',
                    'design': 'Full-Context',
                    'enrich': 'n',
                    'host_name': 'www.paypal.com',
                    'server_epoch_timestamp': 1653256858497,
                    'serverside_data_source': 'checkout',
                    'scrn_height': '625',
                    'x-paypal-fpti': {
                        'context_id': token,
                        'context_type': 'EC-token',
                        'source': 'checkoutuinodeweb',
                    },
                    'experience': 'checkoutlite',
                    'comp': 'checkoutuinodeweb',
                    'feed_name': 'checkoutuinodeweb',
                    'country': 'UA',
                    'locale': 'en',
                    'market': 'MERCHANT',
                    'planning_activity_handle': '',
                    'api_integration_type': 'standard',
                    'app_int_type': '',
                    'integration_type': 'EC',
                    'state_name': 'XO_LITE_INIT',
                    'client_elapsed': 6880,
                    'client_epoch_ts': 1653256858505,
                },
            },
        ],
        'meta': {
            'state': 'ui_init',
            'token': token,
        },
        'tracking': [],
    }

    response = requests.post('https://www.paypal.com/xoplatform/logger/api/logger/',
                             cookies=cookies, headers=headers, json=json_data)
    print(response.json())


def binding(biz_id, cookies):

    headers = {
        'Host': 'f-p.sgsnssdk.com',
        'Connection': 'close',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://f-p.sgsnssdk.com/pipo_fe/checkout/common/bind_land?biz_id=AWUAACuR0hIrSUNjiA2lGbLYK&locale=en',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,tr;q=0.5,ar;q=0.4',
        # 'Cookie': 'MONITOR_WEB_ID=fffb2911-9be1-4e4b-90e4-f01c284237a5',
    }

    params = {
        'biz_id': biz_id,
    }

    response = requests.get('https://f-p.sgsnssdk.com/pipo_fe/checkout/payment_api/payment/v1/get_binding_result',
                            params=params, cookies=cookies, headers=headers)
    print(response.text)


def card_bind(id, ticket, nonce, agreement_id, cardId, card_data, proxy):
    headers = {
        'Host': 'f-p.sgsnssdk.com',
        # 'Content-Length': '6202',
        'Sec-Ch-Ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Fp-Passport-Ticket': str(ticket),
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://ads.tiktok.com',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ads.tiktok.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    json_data = {
        "agreement_id": str(agreement_id),
        "configuration": {
            "environment": "live",
            "locale": "en",
            "origin_key": "f635b516b4768d5a9f4bc5dd68f8d06727457a0f",
            "flow": "web"
        },
        "country_or_region": card_data['billing_country_region'],
        "merchant_user_id": str(id),
        "payment_method": {
            # pm_pi_ccdc_mastercard_c_d          ##pm_pi_ccdc_visa_c_d
            "method_id": "pm_pi_ccdc_mastercard_c_d",
            "method_type": "CCDC",
            "method_params": {
                "phone_country_code": "55",
                "card_number": card_data['card_number'],
                "expiration_month": card_data['expiration_month'],
                "expiration_year": card_data['expiration_year'],
                "cvv": card_data['cvv'],
                "holder_name": card_data['holder_name'],
                "billing_country_region": card_data['billing_country_region'],
                "proxy_type": "eg_ccdc_global_proxy_type",
            },
            "payment_elements": [
                {
                    "element": "eg_ccdc_global_phone_country_code",
                    "param_name": "phone_country_code",
                    "param_value": "55",
                    "is_encrypted": False
                },
                {
                    "element": "eg_ccdc_global_card_number",
                    "param_name": "card_number",
                    "param_value": card_data['card_number'],
                    "is_encrypted": False
                },
                {
                    "element": "eg_ccdc_global_expiration_month",
                    "param_name": "expiration_month",
                    "param_value": card_data['expiration_month'],
                    "is_encrypted": False
                },
                {
                    "element": "eg_ccdc_global_expiration_year",
                    "param_name": "expiration_year",
                    "param_value": card_data['expiration_year'],
                    "is_encrypted": False
                },
                {
                    "element": "eg_ccdc_global_cvv",
                    "param_name": "cvv",
                    "param_value": card_data['cvv'],
                    "is_encrypted": False
                },
                {
                    "element": "eg_ccdc_global_holder_name",
                    "param_name": "holder_name",
                    "param_value": card_data['holder_name'],
                    "is_encrypted": False
                },
                {
                    "element": "eg_ccdc_global_billing_address_state",
                    "param_name": "billing_state"
                },
                {
                    "element": "eg_ccdc_global_billing_address_city",
                    "param_name": "billing_city"
                },
                {
                    "element": "eg_ccdc_global_billing_address_postal_code",
                    "param_name": "billing_postal_code"
                },
                {
                    "element": "eg_ccdc_global_billing_address_country_regin",
                    "param_name": "billing_country_region",
                    "param_value": card_data['billing_country_region'],
                    "is_encrypted": False
                }
            ],
            "element_params": {
                "country_code": card_data['billing_country_region'],
                "sdk_type": "go",
                "sdk_version": "10.0.0"
            }
        },
        "request_id": str(cardId),
        "return_url": "https://ads.tiktok.com/wpay/oversea/result?invokerID=fdfsdfsdf",
        "nonce": str(nonce),
        "risk_info": str(cardId),
        "request_amount": '0',
        "currency": "USD"
    }
    value_str = json.dumps(json_data)
    d = 'merchant_id=10202007S2Pa69&biz_content=' + \
        str(urllib.parse.quote(value_str))
    # print(d)
    response = requests.post(
        'https://f-p.sgsnssdk.com/agreement_deduct/v1/bind_ccdc_authorize_agreement_with_amount', headers=headers, data=d, proxies=proxy)
    js = response.json()["response"]
    print(js)
    data = json.loads(js)
    card_url = data['redirect_details']['url']
    print("LINKA")
    print(data['redirect_details']['url'])
    return card_url


def payment(id, cook, cookies, proxies):
    headers = {
        'Connection': 'close',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'TRACE-LOG-ADV-ID': id,
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'TRACE-LOG-USER-ID': id,
        'Accept': 'application/json, text/plain, */*',
        'X-CSRFToken': cookies['csrftoken'],
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ads.tiktok.com/i18n/account/payment?aadvid=7076901137089069058',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,tr;q=0.5,ar;q=0.4'}
    res = requests.get("https://ads.tiktok.com/api/v3/i18n/payment/card/info/?aadvid="+id+"&msToken=" +
                       cookies['msToken']+"&X-Bogus="+cook+"&_signature="+cook, cookies=cookies, proxies=proxies, headers=headers)
    print(res.json())

def Add_Payment_Success(data, cookies):
    res = requests.post("http://localhost:7000/api/account/paymentMethod/success/", json= {
       
        "cookies":cookies,
        "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "proxy":"socks5://dekamerontink:q7SX5nD6IT@185.212.205.232:50101",
        'biz_id':data["biz_id"]
    }
    )
    print(res.json())








if __name__ == "__main__":
    datetime.datetime.now()
   
    js_file = 'accounts/'+str(random.randint(19999, 4000000))+'.json'
    print(datetime.datetime.now())
    #cookie_list = ['cookie_7.json', 'usa_2.json', 'usa.json', 'cookie_5.json', 'cookie_1.json', 'cookie_6.json','ua_1.json','ua_2.json','ua_3.json','ua_4.json','ua_5.json']
    cookie_list = ['account11.json', 'account8.json',
                   'account5.json', 'account9.json']
    seed = random.randint(0, 3)


    cookies_parser = Dolphin_Cookies_Convert

##########################################################
    cookies_path_file = "dolphin-anty-cookies-277.txt"

##########################################################


    cookies_toPython = cookies_parser.toPython(cookies_path_file)
    cookies_toAxios = cookies_parser.toAxios(cookies_path_file)
    # puths = '53.json'  # cookie_list[seed]
    print('Cookie: '+cookies_toPython)

    seed_time_zone = random.randint(0, len(time_zone_list))
    seed_proxy_list = random.randint(0, len(proxy_list))
    prox = proxy_list[seed_proxy_list]

    # open_cook = open(puths, 'r')

    # s = open_cook.read()





    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
    a = user_generator.UserGenerator()
    a.TIME_ZONE_NAME = 'Europe/Kiev'
    a.TIMEZONE = 'Europe/Kiev'
    a.COUNTRY = 'US'
    a.CURRENCY = 'EUR'
    a.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    json_data = a.risk_info_register(1)
    json_data2 = a.risk_info_update(1)
    b = Register()
    b.COOKIES = json.loads(cookies_toPython)
    seed_tt_we = random.randint(1000, 9999)

    seed_cookie = random.randint(1000, 9999)



    card_data = {"billing_country_region": "TR", "card_number": "5374921159331226", "expiration_month": "02",
                 "expiration_year": "26", "holder_name": "Asnddda Hasnssxcdfssds", "cvv": "471", "currency": str(a.CURRENCY)}  #2

    # 11
    count = 0
    fine = 0
    account_data = {}
    #b.COOKIES['MONITOR_WEB_ID'] = b.webid()
    card_bind_proxy = {"http": "socks5://dekamerontink:q7SX5nD6IT@185.212.205.232:50101",
             "https": "socks5://dekamerontink:q7SX5nD6IT@185.212.205.232:50101"}
    while count <= fine:
        try:
        
            
            #b.COOKIES["ttwid"] = 'ZALIV_'+b.webid()
            id = b.registration(json_data)
           
            # # (2)
            campaign_id = b.campaign_create_conversion(id,1)
            # # campaign_id2 = b.campaign_create_conversion(id,2)
            # # campaign_id3 = b.campaign_create_conversion(id,3)
            # # (2)
           
            # px = b.pixel(id)
         
            # PixelID = str(px['PixelID'])
            # PixelCode = str(px['PixelCode'])
            # b.pixel_update(id, PixelCode)
            px = b.pixel_page(str(id))

            PixelID = str(px['pixel_id'])
            PixelCode = str(px['pixel_code'])
            
            # px2 = b.pixel(id)
         
            # PixelID2 = str(px2['PixelID'])
            # PixelCode2 = str(px2['PixelCode'])
            # time.sleep(3)
            # b.pixel_update(id, PixelCode)
            # b.pixel_update(id, PixelCode2)



            # adgroup_id = b.adgroup_create(id, campaign_id, PixelID, "Poland", "798544")
            
            # adgroup_id2_2 = b.adgroup_create_conversion(
            #     id, campaign_id, PixelID, "TR_"+id+'_1', "298795", '9', '2023-01-28 11:15:02', '300.00')
            
            # adgroup_id2_2 = b.adgroup_create_traffic(
            #     id, campaign_id, PixelID, "TR"+id+'_1', "298795", '9', '2023-01-28 11:15:02', '300.00')
            
            adgroup_id2_2 = b.adgroup_create_page(
                id, campaign_id, PixelID, "DE_"+id+'_1', 2921044, '5', '2023-02-18 00:15:02', '300.00')    #####!!!!!!!!!!!! 5
             

            
            # adgroup_id2_3 = b.adgroup_create_conversion(
            #     id, campaign_id, PixelID2, "PL_"+id+'_2', "798544", '9', '2023-01-28 00:15:02', '300.00')
            
            # adgroup_id2_4 = b.adgroup_create_conversion(
            #     id, campaign_id, PixelID, "PL_"+id+'_3', "798544", '9', '2023-01-28 00:15:02', '300.00')
            
            # adgroup_id2_5 = b.adgroup_create_conversion(
            #     id, campaign_id, PixelID2, "PL_"+id+'_4', "798544", '9', '2023-01-28 00:15:02', '300.00')    
            # # adgroup_id2_3 = b.adgroup_create_conversion(
            #     id, campaign_id, PixelID, "RO_"+id+'_2', "798549", '5', '2023-01-23 12:15:02', '500.00')
            

         
         

          
            # adgroup_id2_3 = b.adgroup_create_traffic(
            #     id, campaign_id2, PixelID, "DE_"+id+'_1', "2921044", '5', '2023-01-04 19:07:02', '8345.00')
            # adgroup_id2_4 = b.adgroup_create_traffic(
            #     id, campaign_id3, PixelID, "DE_"+id+'_2', "2921044", '5', '2023-01-04 19:07:02', '8345.00')
            # # adgroup_id2_3 = b.adgroup_create_traffic(
            #     id, campaign_id, PixelID, "CZ_"+id+'_2', "3077311", '5', '2023-01-03 11:08:02', '2345.00')
            # adgroup_id2_4 = b.adgroup_create_traffic(
            #     id, campaign_id, PixelID, "CZ_"+id+'_3', "3077311", '5', '2023-01-03 12:09:02', '28345.00')
            # adgroup_id2_5 = b.adgroup_create_traffic(
            #     id, campaign_id, PixelID, "CZ_"+id+'_4', "3077311", '9', '2023-01-03 11:07:02', '38345.00')
           # adgroup_id2 = b.adgroup_create(id, campaign_id, PixelID, "Spain", "2510769")
           # adgroup_id2_2 = b.adgroup_create(id, campaign_id, PixelID, "Spain_2", "2510769")
            # adgroup_id2_3 = b.adgroup_create(id, campaign_id, PixelID, "Spain_3", "2510769")
            # adgroup_id3 = b.adgroup_create(id, campaign_id, PixelID, "France", "3017382")
            # adgroup_id4 = b.adgroup_create(id, campaign_id, PixelID, "Deutch", "2921044")

            site_url = "tg://resolve?domain=aviatrmostbet&"+str(id) #tg://join?invite=+0CcUQ__Nu9I3OTdi
            template_id = 'tos-alisg-i-375lmtcpo0-sg/87a26da41ae5493ea2f2de7ebf9d9a24'
            template_url = 'https://p19-lp-sg.ibyteimg.com/tos-alisg-i-375lmtcpo0-sg/87a26da41ae5493ea2f2de7ebf9d9a24~tplv-noop.webp'
            template_text = 'TG'

            nomer = count
            nomer2 = count
            
            page_id = b.page_create(id, nomer, site_url, template_id, template_url, template_text)
            b.page_publish(id, page_id)
          
            ident_id = b.ident(id)
            
            print(b.update(json_data2, id))
           
           # time.sleep(10)
           
             
            # (1)
           
            payment_link = "https://ads.tiktok.com/i18n/account/payment?aadvid=" + \
                str(id)
            d = open('card.html', "a")
            d.write("<span>"+str(id)+" "+str(count) +
                    "</span><a target='_blank' href='"+str("card_url")+"'> Link</a>"+"\n")
            d.write("<span>"+str(id)+" "+str('PAYPAL') +
                    "</span><a target='_blank' href='"+str("paypal_link")+"'> PAYPAL</a>"+"\n")
            d.write("<a target='_blank' href='" +
                    str(payment_link)+"'> PAYMENT LINK</a>"+"\n")
            d.close()

            # ticket = b.ticket()
            # vcpo = b.vcpo(id)
            # agreement = b.agreement(id, str(vcpo))

            # nonce = b.nonce(vcpo)
            # cardId = b.cardId(vcpo, id)
            # time.sleep(2)
            # card_url = card_bind(
            #     id, ticket, nonce, agreement, cardId, card_data, card_bind_proxy)

            # biz_id = card_url.split('&')[0].split('=')[1]
           
            # account_data['biz_id'] = biz_id
            # paypal_link = b.paypal_link(id, str(vcpo), agreement)
            # Add_Payment_Success(account_data,cookies_toAxios)   
            
        
            
            
            # creative_id2_3 = b.creative_create(ident_id, adgroup_id2_2, id, '', nomer,
            #                                    'https://evo-extrime.space', PixelID, 'KURULUM', 'page_id', 0)
            creative_id2_4 = b.creative_create(ident_id, adgroup_id2_2, id, PixelID, nomer,
                                               '', '', 'Install now', page_id, 0, 'install_now')

            creative_id2_5 = b.creative_check(ident_id, adgroup_id2_2, id, PixelID, nomer,
                                               '', '', 'Install now', page_id, 0, 'install_now')

            # adgroup_id2_3 = b.adgroup_create_page(
            #     id, campaign_id, PixelID, "TR_"+id+'_2', 298795, '5', '2023-02-17 15:15:02', '300.00')    #####!!!!!!!!!!!! 5
             
            # creative_id2_4 = b.creative_create(ident_id, adgroup_id2_3, id, PixelID, nomer,
            #                                    '', '', 'Install now', page_id, 0, 'install_now')

            # creative_id2_5 = b.creative_check(ident_id, adgroup_id2_3, id, PixelID, nomer,
            #                                    '', '', 'Install now', page_id, 0, 'install_now')
            # # print('Sleep 120 seconds')
            # time.sleep(120)
            # print(b.update(json_data2, id))                                   
            # creative_id2_5 = b.creative_create(ident_id, adgroup_id2_2, id, PixelID, nomer,
            #                                    '', 'https://www.sadsdfsdfsdfsfsdfsa.com.tr/?tt_dynamic_pixel='+PixelCode, '🔥 Wpłać już za 10 PLN i otrzymaj bonus 3000 PLN + 250 FS', '', 0)
            # creative_id2_6 = b.creative_create(ident_id, adgroup_id2_5, id, PixelID2, 3,
            #                                    '', 'https://pldatixcvnggirl.click/2/?tt_dynamic_pixel='+PixelCode, 'Naciśnij instalację', "page_id", 0)
           #Descărcați, înscrieți-vă și revendicați-vă bonusul acum! 

            print('Count: '+str(count))
            count += 1

        except Exception as e:
            print(e)
            #count += 1
            continue
