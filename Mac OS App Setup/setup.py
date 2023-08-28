import os,sys,requests, shutil, termtitle, pyfiglet
from zipfile import ZipFile; from colorama import Fore
cwd = os.getcwd()
#Download Function
def download(url: str, fileName: str):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    length = response.headers.get('content-length')
    block_size = 1000000  # default value
    if length:
        length = int(length)
        block_size = max(4096, length // 20)
    filesize = length*10**-6
    filesize = round(filesize, 2)
    print(Fore.BLUE+f"{fileName}"+Fore.RESET+' size: '+Fore.CYAN+f"{filesize} MB"+Fore.RESET)
    with open(fileName, 'wb') as f:
        size = 0
        for buffer in response.iter_content(block_size):
            if not buffer:
                break
            f.write(buffer)
            size += len(buffer)
            if length:
                percent = int((size / length) * 100)
                print(Fore.RESET+"Downloading "+Fore.BLUE+f"{fileName}"+': '+Fore.CYAN+f"{percent}%", end='\r')
    print(Fore.GREEN+"\nDone Downloading: "+Fore.CYAN+f"{fileName}"+Fore.RESET+'\n')

#main tool prompt
#warning = 'IF YOU DO NOT KNOW WHAT THIS TOOL DOES GO TO https://test.html'
if sys.platform != 'darwin':
    sys.exit('Your current OS is not Mac OS as such this program cannot be run.')
title = '"Mac OS Setup"'
os.system('termtitle '+title)
os.system('clear')
logo = pyfiglet.figlet_format("\nMac OS Setup\n")
print(logo)
prompt1 = input('1. Install Homebrew package manager\n2. Select recommended packages to install\n3. exit\n\n:')
if prompt1 == '1':
    os.system('clear')
    print(logo)
    print('Starting Install of the Homebrew package manager.')
    download_install_script = download('https://raw.githubusercontent.com/thegamershollow/Python-Projects/main/Mac%20OS%20App%20Setup/homebrew-install.sh','install.sh')
    os.system('sh install.sh')
if prompt1 == '3':
    sys.exit('Exiting')



#homebrewCommand = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
#os.system(homebrewCommand)