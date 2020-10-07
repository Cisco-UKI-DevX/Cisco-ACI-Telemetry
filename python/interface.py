import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
apic = "https://sandboxapicdc.cisco.com"
auth_endpoint = "/api/aaaLogin.json"

url = apic + auth_endpoint

body = '{\n  "aaaUser" : {\n    "attributes" : {\n      "name" : "admin",\n      "pwd" : "ciscopsdt"\n    }\n  }\n}\n'

payload = body


headers = {"Content-Type": "text/plain"}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

jsontoken = json.loads(str(response.text))

token = jsontoken["imdata"][0]["aaaLogin"]["attributes"]["token"]

get_endpoint = (
    "/api/node/mo/topology/pod-1/node-201/sys/phys-[eth5/1]/CDeqptIngrTotal5min.json"
)

headers = {"Cookie": "APIC-Cookie=" + token}
url = apic + get_endpoint
r = requests.request("GET", url, headers=headers, verify=False)
result = json.loads(r.text)
result = result["imdata"][0]["eqptIngrTotal5min"]["attributes"]["bytesRateAvg"]
result = int(float(result))
print(result)
