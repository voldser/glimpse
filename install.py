from subprocess import check_output
import os
from platform import system as systemos, architecture
os.popen('pip3 install -r requirements.txt').read()
from wget import download

def create_domain():
        try:
                dir = os.popen('pwd').read()
                dir2 = os.popen("whereis sh").read().split()[1][:-2] + "glimpse"
                file = open(dir2, "w")
                file.write("cd " + dir + "python3 main.py")
                file.close()
                os.system("chmod +x " + dir2)
        except: pass



def Ngrok():
        if True:
                if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
                        filename = 'ngrok-stable-linux-arm.zip'
                else:
                        ostype = systemos().lower()
                        if architecture()[0] == '64bit':
                                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
                        else:
                                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
                url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
                download(url)
                os.system('unzip ' + filename)
                os.system('rm -Rf ' + filename)
                os.system('clear')



Ngrok()
create_domain()
os.system("ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa <<< y")
os.system('python3 main.py')
