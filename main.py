import requests
from client import Client

#Initialize client and "login"
client = Client("0123456", "pass123")
json_client = client.getClientData()
response = requests.post("http://127.0.0.1:5000/auth", json=json_client)
token = response.json().get("access_token")

#Authenticate and retrieve data
headers = {
    "Authorization": str(token)
}
resource_response = requests.get("http://127.0.0.1:5000/resource", headers=headers)
print(resource_response.json())