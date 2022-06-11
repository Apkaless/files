import requests



ip = input('Enter Server IP:PORT: ')
r = requests.get('http://%s/players.json'%(ip))

res = r.json()
print('\n')
players = 0
for i in res:
    info = i
    player_name = info['name']
    player_id = info['id']
    player_ping = info['ping']
    print(f"Player Name: {player_name}\nPlayer ID: {player_id}\nPlayer Ping: {player_ping}\n",'='*20, '\n')
    players += 1

print(f'Total Players: {players}\n')

input('')