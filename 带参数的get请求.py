import requests

url="http://www.tuling123.com/openapi/api"
pama={
    "key":"ec961279f453459b9248f0aeb6600bbe",
    "info":"你好"
}
r=requests.get(url,params=pama)
print(r.text)