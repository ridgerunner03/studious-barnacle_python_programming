import requests
from random import choice

topic = input("Let me tell you a joke!  Give me a topic: ")
url="https://icanhazdadjoke.com/search"
response=requests.get(url,headers={"Accept":"application/json"},params={"term":topic})
data =response.json()
num=len(data["results"])
j=choice(data["results"])
print(f'There are {num} jokes about this topic.  Here\'s one: {j["joke"]}')
        
