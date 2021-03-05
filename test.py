import requests
data = requests.post("http://localhost:5005/webhooks/rest/webhook",json={"message":"what time is the flight"})
print(data.json())