
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['2500 5000 7500 10000 12500\r\r', '5 10 15 20 25\r\r', '1 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['500 800 1200 1600 2000\r\r', '2 3 4 5 6\r\r', '6 5']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['100 200 300 400 500\r\r', '5 4 3 2 1\r\r', '4 3']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['0 0 0 0 0\r\r', '0 0 0 0 0\r\r', '0 0']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['1200 700 300 1900 2400\r\r', '6 5 4 3 2\r\r', '3 2']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['1500 200 1000 3500 100\r\r', '1 1 1 1 1\r\r', '1 2']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['500 1000 1500 2000 2500\r\r', '7 8 9 10 11\r\r', '12 13']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['50 60 70 80 90\r\r', '2 3 4 5 6\r\r', '10 9 ']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['500 1000 1500 2000 2500\r\r', '1 2 3 4 5\r\r', '5 4']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['30 60 90 120 150\r\r', '5 4 3 2 1\r\r', '10 20']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    