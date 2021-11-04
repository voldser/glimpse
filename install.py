from subprocess import check_output
import os
import urllib.request
from platform import system as systemos, architecture


# NGROK
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
        urllib.request.urlretrieve(url)
        os.system('unzip ' + filename)
        os.system('rm -Rf ' + filename)
        os.system('clear')

#LOCALXPOSE

Ngrok()
os.system('pip install -r requirements.txt')
os.system('ssh-keygen -t ed25519')
os.system('python main.py')
