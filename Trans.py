import sys
import os

import requests

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time
import threading

import multiprocessing

#import pyperclip



# 실행 PC 리스트 가져오기
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from _common import process_list







# 번역
def multiSelenium(process):

	slp = (int(process) - 1) * 9
	time.sleep(slp)

	# 실행 PC 리스트 가져오기
	sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
	from _common import Pc
	from _common import Server

	Pc = str(Pc)

	from _Run import TransType
	TransSite = TransType[0]	#Papago, Google
	NtosUrl = TransType[1]	#Ntos 번역 Url
	CustId = TransType[2]	#Ntos Id
	TransLeng = TransType[3]	#번역사이트 언어설정
	TransOrigin = TransType[4]	#번역할 필드
	TransUp = TransType[5]	#업데이트할 필드

	if TransSite == "" :
		print("번역 미실행중")
	elif TransSite == "push" :
		if process == "1" and Pc == "1" :
			os.system("C:/xampp/htdocs\\_Ntos/_TransSelenium/_GitPush.bat")
		else :
			print("Git push...")
	elif TransSite == "pull" :
		if process == "1" and Pc != "1" :
			os.system("C:/xampp/htdocs\\_Ntos/_TransSelenium/_GitPull.bat")
		else :
			print("Git pull...")
	else : 

		data = {'CustId':CustId, 'Pc':Pc, 'Number': process, 'Mode':'list', 'TransOrigin':TransOrigin, 'TransUp':TransUp } 
		try :
			response = requests.post(NtosUrl, data=data)
		except :
			time.sleep(2)
			response = requests.post(NtosUrl, data=data)



		#result = "".join(sampleText)
		result = response.text
		
		if result == "test" :
			if process == "1" :
				print("실행명령")
			else :
				print("중지")
		elif result == "error" :
			print('에러')
		elif result == "not" :
			print('번역없음')
		else :
			
			#번역시작
			resultList = result.split("@@@")
			number = 0
			itemcodeArr = []
			itemnameArr = []

			for val in resultList :
				(itemcode,itemname) = val.split("|@|")
				itemcodeArr.insert(number, itemcode)
				itemnameArr.insert(number, itemname.replace("\n", " "))
				number = number +1

			TransItemCode = "|@|".join(itemcodeArr)
			TransItemName = "\n\n\n\n".join(itemnameArr)
			"""
			f = open("C:/xampp/htdocs/_Ntos/_TransSelenium/test_"+process+".txt", "w",encoding='UTF-8')
			f.write(TransItemName)
			f.close()
			"""
			"""
			print('번역실행'+TransItemName)
			"""
			"""
			options = webdriver.ChromeOptions()
			options.add_argument('window-size=1920,1080')
			options.add_argument('HEADLESS')
			"""
			chrome_options = webdriver.ChromeOptions()
			chrome_options.add_argument('HEADLESS')
			chrome_options.add_argument("window-size=1920,1080")

			if TransSite == "Papago" :
				URL = 'https://papago.naver.com/?'+ str(TransLeng)
			else :
				URL = 'https://translate.google.com/?'+ str(TransLeng)
			if Server == "win" :
				driver = webdriver.Chrome('C:/xampp/htdocs/_Ntos/_TransSelenium/chromedriver.exe', chrome_options=chrome_options)
				#driver = webdriver.Chrome('C:/xampp/htdocs/_Ntos/chromedriver.exe', options=options)
				#driver = webdriver.Chrome('C:/xampp/htdocs/_Ntos/chromedriver.exe')
			else :	#ubuntu
				driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
			driver.implicitly_wait(3)

			driver.get(url=URL)
			driver.implicitly_wait(3)

			#종료
			"""
			def DriverQuit():
				terminate(process)
				driver.close()

			DriverJob = threading.Timer(50, DriverQuit)
			DriverJob.start()
			"""

			if TransSite == "Papago" :
				input_box = driver.find_element_by_xpath('/html/body/div/div/div[1]/section/div/div[1]/div[1]/div/div[3]/label/textarea')
			else :
				input_box = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
			time.sleep(1)
			
			input_box.send_keys(TransItemName)
			#pyperclip.copy(TransItemName)
			#input_box.send_keys(Keys.CONTROL, 'v')

			#driver.implicitly_wait(7)
			time.sleep(10)

			if TransSite == "Papago" :
				trans_box = driver.find_element_by_xpath('/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[5]/div')
			else :
				trans_box = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]')

			#driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[4]/div[2]/div/span/button/i').click()

			# 

			name_list = trans_box.text
			"""
			f = open("C:/xampp/htdocs/_Ntos/_TransSelenium/test_"+process+"_.txt", "w",encoding='UTF-8')
			f.write(name_list)
			f.close()
			"""
			data = {'CustId':CustId, 'Pc':Pc, 'Number': process, 'Mode':'transup', 'TransOrigin':TransOrigin, 'TransUp':TransUp, 'codelist':TransItemCode, 'namelist' : name_list, 'orgnamelist' : TransItemName } 
			try :
				response = requests.post(NtosUrl, data=data)
			except :
				time.sleep(2)
				response = requests.post(NtosUrl, data=data)
			"""
			print("====================" + process + "=========================")
			print(name_list)
			"""
			Result = response.text
			Time_ = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
			print("Pc"+Pc+" ("+process+") > "+Result+" : "+ Time_)


			driver.close();


if __name__ == '__main__':


	# 프로세스 3개
	#process_list = ["1", "2", "3"] #../_common.py
	#DriverJob = threading.Timer(10, ProcessQuit)
	#DriverJob.start()
	# 멀티 프로세스 사용
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	pool.close()
	pool.join()
	sys.exit()