# from test.case.basecase import BaseCase
# from lib.db import *
# import json
#
# class test_user_reg(BaseCase):
#     def test_user_reg(self):
# #注册用户
#       case_data=self.get_case_data("reg_ok")
#       username=json.loads(case_data["args"])["username"]
#       print(username)
# #环境检查
#       if check_user(username):
#           del_user(username)
#           self.send_request(case_data)
# #数据库断言
#           self.assertTrue(check_user(username))
# #数据清理
#           del_user(username)
import unittest,requests,json
from test.case.basecase import BaseCase
from lib.db import *


class test_user_reg(BaseCase):
    def test_user_reg_ok(self):
        case_data=self.get_case_data("reg_ok")
        username=json.loads(case_data["args"])["userName"]
        if check_user(username):
            del_user(username)
        self.send_request(case_data)
        self.assertTrue(check_user(username))
        del_user(username)
    def test_user_reg_fail(self):
        case_data = self.get_case_data("reg_ok")
        name = json.loads(case_data["args"])["userName"]
        if not check_user(name):
            add_user(name,"123456")
        self.assertTrue(check_user(name))
        self.send_request(case_data)





if __name__ == '__main__':
    unittest.main()
