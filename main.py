from termcolor import colored
import urllib.request
import json
import os
import requests
import socket
import time
from progress.bar import ShadyBar
import subprocess
import optparse
import re
# ----------------------------------------------------------------------------
try:
	while True:
		command = input(colored("<? >  ", 'red'))
		if command == "help":
# ----------------------------------------------------------------------------
			print("*" * 50)
			print("IP", " | ", "port-scan", " | ", "phone", " | ")
			print("*" * 50)
# ----------------------------------------------------------------------------
		if command =="exit":
# ----------------------------------------------------------------------------
			print()
			print(colored("Exiting from WOK...", 'red'))
			exit(0)
# ----------------------------------------------------------------------------
		if command == "IP":
# ----------------------------------------------------------------------------

			yes_color = colored("[+]", 'green')

			getIP = input(colored("[+] Enter IP --> ", 'red'))
			url = "https://ipinfo.io/{}/json".format(getIP)

			response = requests.get(url)

			JSON_url = response.json()

			try:
			    print(yes_color, "IP", "<--->", JSON_url['ip'])
			    print(yes_color, "Readme", "<--->", JSON_url['readme'])
			    print(yes_color, "TimeZone", "<--->", JSON_url['timezone'])
			    print(yes_color, "Region", "<--->", JSON_url['region'])
			    print(yes_color, "Hostname", "<--->", JSON_url['hostname'])
			    print(yes_color, "Location", "<--->", JSON_url['loc'])
			    print(yes_color, "Organization", "<--->", JSON_url['org'])
			    print(yes_color, "Country", "<--->", JSON_url['country'])
			    print(yes_color, "City", "<--->", JSON_url['city'])
			except KeyError:
			    print(colored("Некоторые данные получить неудалось", 'red'))

# ----------------------------------------------------------------------------
		if command == "port-scan":
# ----------------------------------------------------------------------------
			def fanc1():
				color_a = colored("[+] ", 'green')
				print(colored("~"*50, 'cyan'))
				host = input(color_a + "Host --> ")
				port = int(input(color_a + "Port --> "))
				print(colored("~"*50, 'cyan'))

				scan = socket.socket()

				color_b = colored("[!] ", 'red')
				color_c = colored("[!] ", 'white')

				try:
				    scan.connect((host, port))
				except socket.error:
				    print(color_b + "Port -- ", port, " -- [CLOSED]")
				else:
				    print(color_a + "Port -- ", port, " -- [OPEN]")

			def fanc2():
				Re_Select = int(input("[?] Вплоть до какого порта нужно провести сканирование?  "))
				print(colored("~"*50, 'cyan'))
				print(colored("\t[0] - Показывать только закрытые", 'cyan'))
				print(colored("\t[1] - Показывать только открытые", 'cyan'))
				print(colored("\t[5] - Показывать все(до {})".format(Re_Select), 'cyan'))
				print(colored("~"*50, 'cyan'))
				select = int(input("[scan]-->  "))
				color_a = colored("[+] ", 'green')
				color_b = colored("[!] ", 'red')
				color_c = colored("[!] ", 'white')

				host = input(color_a + "Host --> ")
				print(color_a+"Подождите пожалуйста, сканирование идет...")
				print("\n")
				port = []
				check_list = []
				bar = ShadyBar('Loading', max = Re_Select)
				for i in range(1, Re_Select):
					port.append(i)

				for i in port:
					try:
						scan = socket.socket()
						scan.settimeout(0.5)
						scan.connect((host, i))

					except socket.error:
						if select == 0:
							# print(color_b + "Port -- ", i, " -- [CLOSED]")

							a = "Port -- ", i, " -- [CLOSED]"
							check_list.append(a)
							bar.next()
						elif select == 5:
							# print(color_b + "Port -- ", i, " -- [CLOSED]")
							b = "Port -- ", i, " -- [CLOSED]"
							check_list.append(b)
							bar.next()
						else:
							bar.next()
							pass
					else:
						if select == 1:
							# print(color_a + "Port -- ", i, " -- [OPEN]")
							c = "Port -- ", i, " -- [OPEN]"
							check_list.append(c)
							bar.next()
						elif select == 5:
							# print(color_a + "Port -- ", i, " -- [OPEN]")
							d = "Port -- ", i, " -- [OPEN]"
							check_list.append(d)
							bar.next()
						else:
							pass
							bar.next()
				# mylist = []

				# for num in range(0, Re_Select):
				# 	mylist.append(num)
				

				# for item in mylist:
				#     bar.next()
				#     time.sleep(0.001)
				bar.finish()
				print()
				for i in range(0, len(check_list)):
					if " -- [CLOSED]" in check_list[i]:
						print(colored(check_list[i], 'red'))
					else:
						print(colored(check_list[i], 'green'))

			print(colored("~"*50, 'cyan'))

			print(colored("\t[1] --- сканировать отделный порт", 'cyan'))
			print(colored("\t[2] --- сканировать список", 'cyan'))

			print(colored("~"*50+"\n", 'cyan'))
			text_a = input("[scan]--> ")

			if text_a == "1":
			    fanc1()
			elif text_a == "2":
			    fanc2()
			else:
			    print(colored("Параметр введен не правильно!", 'red'))
# ----------------------------------------------------------------------------
		if command == "phone":
			yes_color = colored("[+]", 'green')
			code = input("[counry code] -->  ")
			phone = input("[phone] -->  "+code)
			getINFO = "https://htmlweb.ru/geo/api.php?json&telcod=" + (code+phone)
			response2 = requests.get(getINFO)

			JSON_url2 = response2.json()

			try:
			    print(yes_color, "Number", "<--->", code+phone)
			    print(yes_color, "Readme", "<--->", JSON_url2['country']['name'])
			    print(yes_color, "Region", "<--->", JSON_url2['region']['name'])
			    print(yes_color, "County", "<--->", JSON_url2['region']['okrug'])
			    print(yes_color, "Operator", "<--->", JSON_url2['0']['oper'])
			    print(yes_color, "Piece of light", "<--->", JSON_url2['country']['location'])
			except KeyError:
			    print(colored("Некоторые данные получить неудалось", 'red'))
# ----------------------------------------------------------------------------
except KeyboardInterrupt:
	print("\n")
	print(colored("Exiting from WOK...", 'red'))
	exit(0)
# ----------------------------------------------------------------------------
