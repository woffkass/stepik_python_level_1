import requests
r =  requests.get(input())
text = r.text
a = text.splitlines()
print(len(a))
