#import twoip
#import requests
#from twoip import TwoIP
#twoip = TwoIP(key = None)
#twoip.geo()
#import socket
#print (socket.gethostbyname(socket.gethostname()))
#print (socket.gethostbyname("heroku.com"))

#import stun
#print(stun.get_ip_info())
#('Full Cone', '2.94.28.157', 54320)

import requests
r = requests.get('https://2ip.ua/ua').text
print(r)