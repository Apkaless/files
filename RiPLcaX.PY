import requests
import time
import random
import os

os.system('pip install requests')

os.system('cls')


print('''

_______        ______        ______                   
___    |__________  /_______ ___  /___________________
__  /| |__  __ \_  //_/  __ `/_  /_  _ \_  ___/_  ___/
_  ___ |_  /_/ /  ,<  / /_/ /_  / /  __/(__  )_(__  ) 
/_/  |_|  .___//_/|_| \__,_/ /_/  \___//____/ /____/  
       /_/                                            



[x] Owner     : Apkaless

[x] Country   : Iraq

[x] Instagram : apkaless

[x] Status    : Online

''')

input('Press Enter To Continue... ')
os.system('cls')
try:
    print('Checking the connection to the internet')
    res = requests.get('https://www.google.com')
    if res.status_code == 200:
        print('You are connected!.')
        os.system('cls')
except:
    print('You are not connected to the internet!.')
    time.sleep(3)
    exit(0)

sess = requests.Session()

url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '331',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'csrftoken=null; mid=Yn95fAALAAFQLcWA7FT2YYM75Rh3; ig_did=EC3C9E2B-5E60-4D06-9C97-26590CE468F0; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=H8CHJQkguM1yFxPq4ke0vsgQupnBM9GvJSfW9gpnxNA.eyJ1c2VyX2lkIjoiMTAwMDI5OTQ4NDc5MjIzIiwiY29kZSI6IkFRQXJwTHJycUJPbzUwTmlKOGV6cmdacTg0OE85d1BUOHZxWG5MOWE3YWctMV9FNWxtQm9BNFVVbWE1VDExdUpJNWlhekd2MjRtMHZkaTVYUk41aHRuM2MwRnVCeURQZklRZU8wdEx3enRrLS1wanNrc014a0k3WUhzSnM2cEgzdW9UWEpmTE1WSVFUR1hTQWp6Y0NDVDh3WWpFaTl0bEZ0UHJneFNtS3BxTzhQamJUbXljeDlLNW9Ta3cxTVdJamxLb1hFNlQzWjBHM29sOFFIdnk2eHpWYVd2M1d2MEItTnRrb0VOd3dvc0oyMWNWT2xlTDdTcS1iRjNrVTQ2QVBIYmV4WUwtcVUxZkFIRXpZa2swd3VfWGNMQW52ZktITXNmLWt2SFBObUdsTHYxb2U1STdCRnFSTHVfM3M4SVlwSkp1OWlMTWJ2V0xqaGZjVGF1cVdybm9TIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU1wYWUxZFV2dGJoTDl5SU8yR3BScTVSZ3VIWkNjU09sUDc2Sm02WEFwMVpBR1ZQVWVaQkhKRnZXRlpDWkNveFIyMXNmdUREWTFjaG9wRVg0eTJVbjNtMW80a2NQY3JRQjYzcWRYYjdtRnprcFJaQVMzVm94d1pBVGkxd2JJYVJIWGxaQ2hUQnZTMVpDRW9uOGdQZmNBaU8wU1pBa080ZWVZV2NySllvWkJ5NVlIckJiTmZ3aVpDeXJKRUwyR3hIcDJCb3FRWkRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjUyNTIxMzQwfQ',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/accounts/emailsignup/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'x-instagram-ajax': '9bcc5b5208c5',
    'x-csrftoken': 'null',
    'x-requested-with': 'XMLHttpRequest'
}

def hunter():
    i = 0
    while True:
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        user = ''.join(random.choice(letters) for i in range(4))
        while True:

            data = {
                'enc_password': '#PWD_INSTAGRAM_BROWSER:0:0:Ya112234455',
                'email': 'iraq_spartan300warriors@gmail.com',
                'username': f'{user}',
                'first_name': 'sparta',
                # 'opt_into_one_tap': 'false'
            }

            i += 1
            res = sess.post(url, data=data, headers=headers).json()
        
            reslist = list(res)
            statusindex = reslist.index('status')
            status = reslist[statusindex]
            if res[status] == 'fail':
                print(f'{i}) You have been banned, during checking ==> {data["username"]}, || Don\'t close the script || Wait for 2 mins\n')
                time.sleep(120)
                continue

            drynindex = reslist.index('dryrun_passed')
            dryn = reslist[drynindex]
            status = reslist[statusindex]
            if res[dryn] == False:
                print(f'{i}) {res[dryn]} ==> {data["username"]}, Status: {res[status]}\n')
                break
            elif res[dryn] == True:
                print(f'{i}) Success ==> {data["username"]}, Status: {res[status]}\n')
                savefile = open('user.txt', 'a')
                savefile.writelines([f'Hunted By Apkaless ==> {data["username"]}\n'])
                break

if __name__ == '__main__':
    hunter()
