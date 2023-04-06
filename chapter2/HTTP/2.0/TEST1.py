import httpx
client = httpx.Client(http2=True)
response = client.get('https://www.httpbin.org/get')
print(response.text)
print(response.http_version)

#在客户端的httpx上启用对http/2.0的支持不代表请求和相应都通过HTTP/2.0传输这得客户端和服务端都支持HTTP/2.0才可以  如果客户端连接到仅支持HTTP/1.1的服务器，那么它也需要改用HTTP/1.1