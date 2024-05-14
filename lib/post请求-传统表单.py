import requests
url="http://httpbin.org/post"
data={
    "name":"zhangxinxin",
    "age":"20"
}
headers={
    "content-type":"x-www-form-urlencoded"
}
r=requests.post(url=url,data=data,headers=headers)
print(r.text)
