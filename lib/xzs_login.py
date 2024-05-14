import requests
class mylogin():
    def login(self,us,ps):
        url="http://192.168.55.1:8000/api/user/login"
        header={
           "Content-Type": "application/json"
        }
        data={"userName":us,"password":ps,"remember":False}
        r=requests.post(url=url,headers=header,json=data)
        print(r.text)
        return r.text

if __name__ == '__main__':
    z=mylogin()
    print(z.login("student", "123456"))
