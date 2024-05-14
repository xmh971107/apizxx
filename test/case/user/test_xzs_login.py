import unittest,requests
from lib import  xzs_login

class MyTestCase(unittest.TestCase):
    def test_loginok(self):
        url="http://192.168.55.31:8000/api/user/login"
        header={
           "Content-Type": "application/json"
        }
        data={"userName":"student","password":"123456","remember":False}
        r=requests.post(url=url,headers=header,json=data)
        #print(r.text)
        self.assertIn("成功",r.text)

    def test_loginerr(self):
        url="http://192.168.55.31:8000/api/user/login"
        header={
            "Content-Type": "application/json"
        }
        data={"userName":"","password":"123456","remember":False}
        r=requests.post(url=url,headers=header,json=data)
        #print(r.text)
        self.assertIn("用户名或密码错误",r.text)

if __name__ == '__main__':
    unittest.main()
