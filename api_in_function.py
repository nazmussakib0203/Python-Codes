import requests


def call_api (api_link):
    response=requests.get(api_link)
    data=response.json()
    print(data)

try :
    call_api("https://official-joke-api.appspot.com/random_joke")

except Exception as e :
    print(e)

