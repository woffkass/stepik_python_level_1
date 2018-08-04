import requests
r =  requests.get(input())
count = 0
while True:
    print(r.text)
    r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+r.text)
    if r.text.find('We') == 0:
        print(r.text)
        break
    count += 1
    if count > 500:
        break
