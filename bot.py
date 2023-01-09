import requests
import time

payload = {'content': "di_isi_pesan"}
header = {'authorization': 'di_isi_token'}
link = "https://discord.com/api/v9/channels/di_isi_id_channel/messages"
r = requests.post(link, data=payload, headers=header)
print(" => Send")
time.sleep(2)
print(" => Delay")
