import unittest,sys
sys.path.append('../..')
from test.case.user.test_user_login import test_user_login
from test.case.user.test_user_reg1 import test_user_reg

smoke_suit=unittest.TestSuite()
smoke_suit.addTest(test_user_login('test_login_success'))
smoke_suit.addTest(test_user_reg('test_user_reg_ok'))
def get_suite(suit_name):
    return globals().get(suit_name)


unittest.TextTestRunner(verbosity=2).run(smoke_suit)

if __name__ == '__main__':
    unittest.main()
