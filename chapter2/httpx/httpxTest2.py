import httpx

headers = {
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

#我们需要手动打开HTTP/2.0的支持
client = httpx.Client(http2 = True)
response = client.get('https://spa16.scrape.center/')
print(response.text)



