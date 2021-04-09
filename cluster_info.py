import requests

url = "https://cluster1.demo.netapp.com:443/api/cluster?return_records=true&return_timeout=15"

payload={}
headers = {
  "Authorization": "Basic YWRtaW46TmV0YXBwMSE="
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)