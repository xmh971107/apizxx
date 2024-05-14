import requests
url="http://httpbin.org/get"
r=requests.get(url)
#响应的文本信息
print(r.text)
#响应的二进制格式
print(r.content)
#响应的编码格式
print(r.encoding)
#响应的头步信息
print(r.headers)
#响应的状态码
print(r.status_code)
#响应的cookies值
print(r.cookies)
