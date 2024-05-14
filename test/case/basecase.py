import logging
import unittest,requests,_json,sys,ast
from lib.case_log import *
from lib.read_excel import *
from config.config import *


class BaseCase(unittest.TestCase):
    r=readexcel()
    @classmethod
    def setUpClass(cls):
        print(cls.__name__)
        if cls.__name__ != 'BaseCase':
            cls.data_list=cls.r.excel_to_list(data_file,cls.__name__)
            print(cls.__name__)

    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)

    def send_request(self,case_data):

        case_name=self.get_case_data("case_name")
        url=case_data.get('url')

        method=case_data.get['method']
        headers=case_data.get['headers']
        args=case_data.get['args']
        data_type=case_data.get['data_type']
        expect_res=case_data.get['expect_res']
        print(url,method,headers,args,data_type,expect_res)
        if method.upper()=='GET':
            logging.info("get data")
            response=requests.get(url,headers=headers,params=args)
            log_case_info(case_name,url,args,expect_res,requests.json())

        elif data_type.upper()=='JSON':
            logging.info("json data")
            data=json.loads(args)
            response=requests.request(method,url,headers=headers,data=data)
            log_case_info(case_name,url,args,expect_res,requests.json())
            self.assertIn(expect_res,response.text)

        elif data_type.upper()=='FORM':
            logging.info("form data")
            response=requests.request(method,url,headers=headers,data=args)
            log_case_info(case_name, url, args, expect_res, requests.json())
            self.assertIn(expect_res, response.text)


if __name__ == '__main__':
    unittest.main()















