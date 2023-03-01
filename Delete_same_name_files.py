print("\nListing the all Files in FileStore Folder\n")

import requests
import json

db_url = 'https://adb-7837751364337038.18.azuredatabricks.net'
url = db_url + '/api/2.0/dbfs/list'
ac_token = 'dapi941bd5a60931894d044e5d138a828a53-3'
header = {'Authorization': 'Bearer ' + ac_token, "Content-Type": "application/json"}
payload = {
    'path': '/FileStore/tables'
}
response = requests.get(url, headers=header, params=payload)
data = response.json()
base_url = db_url + '/api/2.0/dbfs/delete'
l = []
name = input("enter File name: ")
for file in (data['files']):
    if name in file['path'][::1]:
        print(file['path'])
        p = {
            'path': file['path']
        }
        res = requests.post(base_url, headers=header, data=json.dumps(p))
        if res.status_code == 200:
            print(f"The Directory successfully delete at {p['path']}")
        else:
            print("Error Occurs")



