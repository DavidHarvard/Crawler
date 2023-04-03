import requests

r = requests.get('https://scrape.center/favicon.ico')
print(r.text)
print(r.content)

with open('favicon.ico','wb') as f:
    f.write(r.content)