#IP TRACER 
import colorama 
import os 
from colorama import Fore, Back, Style 
import requests 
from termcolor import colored
import time
from requests import get 
import sys 

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

def screen_clear():
   if name == 'nt':
      _ = system('cls')



os.system(' clear ')
os.system(' date ')
time.sleep(0.1)
prPurple("|==========================|")
print(Fore.RED+" | ====  ||+++++            |")
time.sleep(0.1)
print(Fore.MAGENTA+" |  ||   ||    |            |")
time.sleep(0.1)
print(Fore.BLUE+" |  ||   ||+++++            |")
time.sleep(0.1)
print(Fore.MAGENTA+" |  ||   ||                 |")
time.sleep(0.1)
print(Fore.RED+" | ====  ||                 |")
time.sleep(0.1)
prPurple("|==========================|")
time.sleep(0.1)
print(Fore.MAGENTA+" |Option 1: check your IP   |")
print(Fore.MAGENTA+" |Option 2: trace a IP      |")
prPurple("|==========================|")
IP = str(input(" Options ==>> "))

if '2' in IP:
       os.system(' clear ')
       os.system(' date ')
       time.sleep(0.1)
       prPurple("|==========================|")
       print(Fore.RED+" | ====  ||+++++            |")
       time.sleep(0.1)
       print(Fore.MAGENTA+" |  ||   ||    |            |")
       time.sleep(0.1)
       print(Fore.BLUE+" |  ||   ||+++++            |")
       time.sleep(0.1)
       print(Fore.MAGENTA+" |  ||   ||                 |")
       time.sleep(0.1)
       print(Fore.RED+" | ====  ||                 |")
       time.sleep(0.1)
       prPurple("|==========================|")
       time.sleep(0.1)  
       ip = input("enter your ip here:")
       track = get(f'https://ipapi.co/{ip}/json/')
       prYellow(track.json())  
       


if '1' in IP:
       os.system(' clear ')
       os.system(' date ')
       time.sleep(0.1)
       prPurple("|==========================|")
       print(Fore.RED+" | ====  ||+++++            |")
       time.sleep(0.1)
       print(Fore.MAGENTA+" |  ||   ||    |            |")
       time.sleep(0.1)
       print(Fore.BLUE+" |  ||   ||+++++            |")
       time.sleep(0.1)
       print(Fore.MAGENTA+" |  ||   ||                 |")
       time.sleep(0.1)
       print(Fore.RED+" | ====  ||                 |")
       time.sleep(0.1)
       prPurple("|==========================|")
       time.sleep(0.1)
       print(Fore.MAGENTA+" |Option 1: check your IP   |")
       print(Fore.MAGENTA+" |Option 2: trace a IP      |")
       prPurple("|==========================|")
       myip = get('https://ipapi.co/json/')
       prYellow(myip.json())
       time.sleep(0.1)
       print(Fore.MAGENTA+"|//////////////////////////////////////|")
       time.sleep(0.1)
       print(Fore.BLUE+"|would you like me to start you on a VPN?/|")
       time.sleep(0.1)
       print(Fore.MAGENTA+"|//////////////////////////////////////|")
       VPN = str(input(" Y/N ==> "))

       if 'N' in VPN:
              os.system(' python3 ip.py ')

       if 'Y' in VPN:
              os.system(' sudo anonsurf start ')
              os.system(' python3 ip.py ')

       elif 'Yes' in VPN:
                  os.system(' sudo anonsurf start ')
                  os.system(' python3 ip.py ')

       elif 'yes' in VPN:
                  os.system(' sudo anonsurf start ')
                  os.system(' python3 ip.py ')

       elif 'sure' in VPN:
                   os.system(' sudo anonsurf start ')
                   os.system(' python3 ip.py ')

       elif 'no' in VPN:
                 os.system(' python3 ip.py ')

       elif 'No' in VPN:
                 os.system(' python3 ip.py ')