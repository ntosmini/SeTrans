# -*- coding: utf-8 -*- 

#기본설정

import requests
import re
import time
import os
import sys

# 실행 PC 리스트 가져오기
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from _common import *

Pc = str(Pc)

NtosTransConfigUrl = "http://mini.ntos.co.kr/_Mini_/_TransSelenium/_Trans_"+ Pc +".txt";

TransMode = ""
try :
	TransMode_ = requests.get(NtosTransConfigUrl)
	TransMode = TransMode_.text
except :
	TransMode = ""


if re.search("404 Not Found", TransMode ) or TransMode == "" :
	print("번역 미실행중 "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	time.sleep(5)
	exit()
else :
	if TransMode == "mini_de_en" :
		TransType = [
			'Google'	#Papago, Google
			, 'http://mini.ntos.co.kr/_Mini_/_TransSelenium/trans.php'	#Ntos 번역 Url
			, 'mini'		#CustId (Ntos Id)
			, 'sl=de&tl=en'	#번역사이트 언어설정
			, 'it_name'	#번역할 필드
			, 'it_name_en'	#업데이트할 필드
			]
	elif TransMode == "mini_en_ko" :
		TransType = [
			'Papago'	#Papago, Google
			, 'http://mini.ntos.co.kr/_Mini_/_TransSelenium/trans.php'	#Ntos 번역 Url
			, 'mini'		#CustId (Ntos Id)
			, 'sk=en&tk=ko'	#번역사이트 언어설정
			, 'it_name_en'	#번역할 필드
			, 'it_name_ko'	#업데이트할 필드
			]


	elif TransMode == "com_en_ko" :
		TransType = [
			'Papago'	#Papago, Google
			, 'http://amazon.ntos.co.kr/_Mini_/_TransSelenium/trans.php'	#Ntos 번역 Url
			, 'amazon'		#CustId (Ntos Id)
			, 'sk=en&tk=ko'	#번역사이트 언어설정
			, 'it_name'	#번역할 필드
			, 'it_name_ko'	#업데이트할 필드
			]
	elif TransMode == "de_de_en" :
		TransType = [
			'Google'	#Papago, Google
			, 'http://amazonde.ntos.co.kr/_Mini_/_TransSelenium/trans.php'	#Ntos 번역 Url
			, 'amazon'		#CustId (Ntos Id)
			, 'sl=de&tl=en'	#번역사이트 언어설정
			, 'it_name'	#번역할 필드
			, 'it_name_en'	#업데이트할 필드
			]
	elif TransMode == "de_en_ko" :
		TransType = [
			'Papago'	#Papago, Google
			, 'http://amazonde.ntos.co.kr/_Mini_/_TransSelenium/trans.php'	#Ntos 번역 Url
			, 'amazon'		#CustId (Ntos Id)
			, 'sk=en&tk=ko'	#번역사이트 언어설정
			, 'it_name_en'	#번역할 필드
			, 'it_name_ko'	#업데이트할 필드
			]
	elif TransMode == "push" :	#git push
		TransType = [
			'push'	#Papago, Google
			, ''	#Ntos 번역 Url
			, ''		#CustId (Ntos Id)
			, ''	#번역사이트 언어설정
			, ''	#번역할 필드
			, ''	#업데이트할 필드
			]

	elif TransMode == "pull" :	#git pull
		TransType = [
			'pull'	#Papago, Google
			, ''	#Ntos 번역 Url
			, ''		#CustId (Ntos Id)
			, ''	#번역사이트 언어설정
			, ''	#번역할 필드
			, ''	#업데이트할 필드
			]
	elif TransMode == "reboot" :	#reboot
		os.system("C:/xampp/htdocs\_Ntos/_TransSelenium/_ReBoot.bat")
		exit()
	else :
		TransType = [
			''	#Papago, Google
			, ''	#Ntos 번역 Url
			, ''		#CustId (Ntos Id)
			, ''	#번역사이트 언어설정
			, ''	#번역할 필드
			, ''	#업데이트할 필드
			]
