import requests
url="http://httpbin.org/post"
data="""{
    "name":"zhangxinxin",
    "age":"20"
}"""
'{"name":"zhangxinxin","age":"20"}'
r=requests.post(url=url,data=data)
print(r.text)