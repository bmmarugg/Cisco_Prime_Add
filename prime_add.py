import requests
import json
from requests.auth import HTTPBasicAuth
from pprint import pprint

requests.packages.urllib3.disable_warnings()
with open("PATH/TO/creds.json") as credentials:
    creds = json.load(credentials)

with open("PATH/TO/prime_device.json") as dev:
    device = json.load(dev)

with open("PATH/TO/device_list.txt") as f:
    device_line = f.read().splitlines()
while("" in device_line):
    device_line.remove("")
device_list = device_line

username = creds['prime_api_user']
password = creds['prime_api_pass']

auth = HTTPBasicAuth(username, password)
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


def main():
    add_device = {'devicesImport':
                        {'devices':
                            {'device':
                                {
                                    "credentialProfileName": "CREDENTIAL PROFILE HERE",
                                    "ipAddress": f"{device}",
                                    "networkMask": "255.255.255.255"
                                }
                            }
                        }
                    }


    results = requests.put('https://YOUR_SERVER_HERE/webacs/api/v1/op/devices/bulkImport',
                          headers=headers, auth=auth, verify=False, data=json.dumps(add_device))

    info = results.json()
    pprint(info)


for device in device_list:
    main()