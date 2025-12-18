import requests
response=requests.get("https://official-joke-api.appspot.com/random_joke")
data=response.json()
print(data)

print(data.items())
print(data.keys())
print(data.values())

print(data["setup"])
print(data["punchline"])