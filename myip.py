import requests


req = requests.Session()

url = 'https://www.myexternalip.com/raw'

res1 = req.get(url)

ip = res1.text

full_url = f'https://ipinfo.io/widget/demo/{ip}'

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'flash=; _lfa=LF1.1.f01ef27cbf09406a.1652926275260; _gid=GA1.2.1883279487.1652926275; _gat_UA-2336519-21=1; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%226beb835d-5db8-4fc7-abd6-f64aede0f533%22; _ga_RWP85XL4SC=GS1.1.1652926274.1.1.1652926295.39; _ga=GA1.2.562335763.1652926275',
    'dnt': '1',
    'referer': 'https://ipinfo.io/?utm_source=myexternalip&utm_medium=website&utm_campaign=upsell_sister_sites',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
res2 = requests.get(full_url, headers=headers).json()


country_code = res2['data']['country']
city = res2['data']['city']
isp = res2['data']['company']['name']

print(f'External IP: {ip}\nCountry: {country_code}\nCity: {city}\nISP: {isp}')

input('')