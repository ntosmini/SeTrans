# -*- coding: utf-8 -*- 

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

import re
#import pyperclip

TransSave = "n"


if time.strftime('%M', time.localtime(time.time())) == "00" or time.strftime('%M', time.localtime(time.time())) == "30" :
	# 프로세스 죽이기
	import psutil   # 실행중인 프로세스 및 시스템 활용 라이브러리
	print('Kill Start... '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	for proc in psutil.process_iter():
		try:
			# 프로세스 이름, PID값 가져오기
			processName = proc.name()
			processID = proc.pid
			#print(processName , ' - ', processID)
	 
			if processName == "chrome.exe" or processName == "chromedriver.exe" :
				print('kill - ', processName , ' - ', processID)
				parent_pid = processID  #PID
				parent = psutil.Process(parent_pid) # PID 찾기
				for child in parent.children(recursive=True):  #자식-부모 종료
					child.kill()
				parent.kill()
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
			pass
	time.sleep(1)


if time.strftime('%M', time.localtime(time.time())) == "100" :
	# 프로세스 죽이기
	import psutil   # 실행중인 프로세스 및 시스템 활용 라이브러리
	print('Kill Start... '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
	for proc in psutil.process_iter():
		try:
			# 프로세스 이름, PID값 가져오기
			processName = proc.name()
			processID = proc.pid
			#print(processName , ' - ', processID)
	 
			if processName == "chrome.exe" or processName == "chromedriver.exe" :
				print('kill - ', processName , ' - ', processID)
				parent_pid = processID  #PID
				parent = psutil.Process(parent_pid) # PID 찾기
				for child in parent.children(recursive=True):  #자식-부모 종료
					child.kill()
				parent.kill()
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
			pass
	time.sleep(5)
else :
	
	# 실행 PC 리스트 가져오기
	sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
	from _common import *

	Pc = str(Pc)

	from _Run import TransType
	TransSite = TransType[0]	#Papago, Google
	NtosUrl = TransType[1]	#Ntos 번역 Url
	CustId = TransType[2]	#Ntos Id
	TransLeng = TransType[3]	#번역사이트 언어설정
	TransOrigin = TransType[4]	#번역할 필드
	TransUp = TransType[5]	#업데이트할 필드


	if TransSite == "" :
		print("번역 미실행중 "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
		time.sleep(5)
	elif TransSite == "push" :
		if Pc == "1" :
			os.system("C:/xampp/htdocs\_Ntos/_TransSelenium/_GitPush.bat")
		else :
			print("Git push... "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
			time.sleep(5)
	elif TransSite == "pull" :
		if Pc != "1" :
			os.system("C:/xampp/htdocs\_Ntos/_TransSelenium/_GitPull.bat")
		else :
			print("Git pull... "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
			time.sleep(5)
	else : 


		# 번역
		def multiSelenium(process):

			slp = (int(process) - 1) * 6
			time.sleep(slp)





			data = {'CustId':CustId, 'Pc':Pc, 'Number': process, 'Mode':'list', 'TransOrigin':TransOrigin, 'TransUp':TransUp } 
			result = ""
			try :
				result_ = requests.post(NtosUrl, data=data)
				result = result_.text
			except :
				result = ""

			

			if re.search("404 Not Found", result ) or result == "" :
				exit()
			else :

				if result == "test" :
					if process == "1" :
						print("실행명령 "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
					else :
						print("중지 "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
				elif result == "error" :
					print('에러 '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
				elif result == "not" :
					print('번역없음 '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
				else :
					
					#번역시작
					resultList = result.split("\n\n")
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

					if TransSave == "y" :
						f = open("C:/xampp/htdocs/_Ntos/_TransSelenium/test_"+process+".txt", "w",encoding='UTF-8')
						f.write(TransItemName)
						f.close()

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
					#driver.implicitly_wait(3)

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
						if TransLeng == "sl=de&tl=en" :
							input_box = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
						else :
							input_box = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
						
					time.sleep(1)
					
					input_box.send_keys(TransItemName)
					#pyperclip.copy(TransItemName)
					#input_box.send_keys(Keys.CONTROL, 'v')
					input_box.send_keys(Keys.ENTER)

					#driver.implicitly_wait(7)
					time.sleep(15)

					if TransSite == "Papago" :
						trans_box = driver.find_element_by_xpath('/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[5]/div')
					else :
						#trans_box = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]')

						#de->en
						trans_box = driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[8]/div/div[1]')

					#driver.find_element_by_xpath('/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[4]/div[2]/div/span/button/i').click()


					name_list = trans_box.text
					if name_list == "" :
						Result = "번역안됨"
					else :
						if TransSave == "y" :
							f = open("C:/xampp/htdocs/_Ntos/_TransSelenium/test_"+process+"_.txt", "w",encoding='UTF-8')
							f.write(name_list)
							f.close()

						data = {'CustId':CustId, 'Pc':Pc, 'Number': process, 'Mode':'transup', 'TransOrigin':TransOrigin, 'TransUp':TransUp, 'codelist':TransItemCode, 'namelist' : name_list, 'orgnamelist' : TransItemName } 
						Result = ""
						try :
							Result_ = requests.post(NtosUrl, data=data)
							Result = Result_.text
						except :
							Result = "Up 실패"

					
					"""
					print("====================" + process + "=========================")
					print(name_list)
					"""
					
					print("\n Pc"+Pc+"-"+process+" ==============================================\n " +Result+" : "+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) +"\n")


					driver.close();


		if __name__ == '__main__':


			# 프로세스 3개
			#process_list = ["1", "2", "3"] #../_common.py
			#DriverJob = threading.Timer(10, ProcessQuit)
			#DriverJob.start()
			# 멀티 프로세스 사용
			#process_list = ["1", "2"]
			pool = multiprocessing.Pool(processes=len(process_list))
			pool.map(multiSelenium, process_list)
			pool.close()
			pool.join()
			sys.exit()
