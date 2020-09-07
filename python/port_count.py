import requests
import json

apic = "http://198.18.133.200"
auth_endpoint = "/api/aaaLogin.json"

url = apic + auth_endpoint

body = "{\n  \"aaaUser\" : {\n    \"attributes\" : {\n      \"name\" : \"admin\",\n      \"pwd\" : \"C1sco12345\"\n    }\n  }\n}\n"

payload = body


headers = {
'Content-Type': 'text/plain'
}

response = requests.request("POST", url,headers = headers, data = payload )

jsontoken = json.loads(str(response.text))

token = jsontoken['imdata'][0]['aaaLogin']['attributes']['token']

get_endpoint = "/api/node/class/topology/pod-1/l1PhysIf.json"

headers = {"Cookie": "APIC-Cookie="+token}
url = apic + get_endpoint
r = requests.request("GET", url,headers=headers)

r = json.loads(str(r.text))

enabled = 0
disabled = 0

x = 0
while x < len(r['imdata']):
    print(r['imdata'][x]['l1PhysIf']['attributes']['switchingSt'])
    if r['imdata'][x]['l1PhysIf']['attributes']['switchingSt'] == "enabled":
        enabled +=  1
    else:
        disabled += 1
    x += 1

totalPorts = len(r['imdata'])


json = json.dumps({'totalPorts': totalPorts, 'enabledPorts': enabled, 'disabledPorts': disabled})

print(json)
