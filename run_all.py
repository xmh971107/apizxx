# import unittest,os,time
# from lib.HTMLTestRunner import HTMLTestRunner
# from lib.send_email import send_email
# from config.config import *
#
# class MyTestCase(unittest.TestCase):
#     def test_all(self):
#         logging.info("==========运行所有的case==========")
#         suit=unittest.defaultTestLoader.discover(test_path,"*test.py")
#         # t=time.strftime("%Y_%m_%d_%H_%M_%S")
#         with open('report.html', 'wb')as f:
#             HTMLTestRunner(
#                 stream=f,
#                 title="xzs测试用例",
#                 description="xzs登录和注册用例集",
#                 verbosity=2
#             ).run(suit)
#
#         send_email('report.html')
#         logging.info("===============测试结束===============")
# if __name__ == '__main__':
#     unittest.main()
import logging
import unittest,os,time,pickle,sys
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suit import *



class MyTestCase(unittest.TestCase):
    def test_all(self):
        logging.info("====运行所有的case========")
        suit=unittest.defaultTestLoader.discover(test_path,'test*.py')
        # t=time.strftime('%Y_%m_%d_%H_%M_%S')
        with open(report_file, 'wb')as f:
            HTMLTestRunner(
                stream=f,
                title='xzs测试用例',
                description='xzs登录和测试用例集',
                verbosity=2
            ).run(suit)
        if result.failures:
            save_failures(result,last_fails_file)
            logging.error("测试失败，失败用例已保存到文件：{}".format(last_fails_file))
        else:
            logging.info("测试成功")

        send_email(report_file)
        logging.info("========测试结束=======")

def discover():
    return unittest.defaultTestLoader.discover(test_case_path)
def run(suite):
    logging.info("====测试开始========")
    with open(report_file, 'wb') as f:
        result=HTMLTestRunner(
            stream=f,
            title='接口测试',
            description='测试描述',
            verbosity=2,
            tester="smart"
        ).run(suite)
        if result.wasSuccessful():
            send_email(report_file)
            logging.info("========测试结束=======")
def run_all():
    run(discover())
def run_suite(suite_name):
    suite=get_suite(suite_name)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print("TestSuite不存在")


def collect():
    suite=unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() !=0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
def collect_only():
    t0=time.time()
    i=0
    for case in collect():
        i +=1
        print("{}.{}".format(str(i),case.id()))
    print("=================================")
    print("Collect {} tests is {:.3f}s".format(str(i),time.time() -t0))
def makesuite_by_testlist(test_list_file):
    with open(test_list_file,encoding='utf-8') as f:
        testlist = f.readlines()

    # #去掉每行结尾的“/n”和 #号开头的行
    testlist=[i.strip()for i in testlist if not i.startswith("#")]
    print(testlist)
    suite=unittest.TestSuite()
    all_cases=collect()
    for case in all_cases:
        case_name=case.id().split('.')[-1]
        if case_name in testlist:
            suite.addTest(case)
    return suite
#根据tag来组建suite
def makesuite_by_tag(tag):
    suite =unittest.TestSuite()
    for i in collect():
      if i._testMethodDoc and tag in i._testMethodDoc:
          suite.addTest(i)
    return suite

def save_failures(result,file):
    suite=unittest.TestSuite()
    for case_result in result.failures:
        suit.addTest(case_result[0])
    with open(file,'wb')as f:
        pickle.dump(suite,f)

def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb')as f:
        suite=pickle.load(f)
    run(suite)
def main():
    if option.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all()


if __name__ == '__main__':
    suite=makesuite_by_testlist(test_list_file)
    run(suite)
    rerun_fails()        # suit=makesuite_by_testlist(test_list_file)
        # run(suit)






