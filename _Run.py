# -*- coding: utf-8 -*- 

#기본설정

import requests

NtosTransConfigUrl = "http://mini.ntos.co.kr/_Mini_/_TransSelenium/_Trans.txt";

TransMode = ""
try :
	response = requests.get(NtosTransConfigUrl)
	TransMode = response.text
except :
	TransMode = ""




if TransMode == "" :
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


	else :
		TransType = [
			''	#Papago, Google
			, ''	#Ntos 번역 Url
			, ''		#CustId (Ntos Id)
			, ''	#번역사이트 언어설정
			, ''	#번역할 필드
			, ''	#업데이트할 필드
			]