import unittest
def setUpModule():
    print("=== setUpModule ===")
def tearDownModule():
    print("=== tearDownModule ===")
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupclass")
    @classmethod
    def tearDownClass(cls):
        print("teardownclass")

    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")
    def test_01(self):
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
