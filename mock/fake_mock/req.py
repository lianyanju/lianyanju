import requests
import json

url = "http://0.0.0.0:8000/user"

payload = json.dumps({
  "username": "lyj",
  "password": "str",
  "email": "lianyanju@163.com",
  "full_name": "lianyanju"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)