import json
import requests

db_url = "https://adb-7837751364337038.18.azuredatabricks.net"
url = db_url + "/api/2.0/clusters/delete"
ac_token = "dapi941bd5a60931894d044e5d138a828a53-3"
header = {"Authorization": "Bearer " + ac_token, "Content-Type": "application/json"}

payload = {
    'cluster_id': '0228-052811-9p8hi3td',
    'action': 'delete'
}

response = requests.post(url, headers=header, json=payload).json()
print(response)
