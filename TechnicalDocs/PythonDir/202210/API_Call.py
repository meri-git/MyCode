import requests

query = {'lat':'45', 'lon':'180'}
response = requests.get("http://api.open-notify.org/astros.json", params=query)
print(response.json())