
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['5 5 5 5 5\r', '5 5 5 5 5\r', '5 5 5 5 5\r', '5 5 5 5 5\r', '5 5 5 5 5']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['5 5 5 5 5\r', '1 1 1 1 1\r', '3 3 3 3 3\r', '7 7 7 7 7\r', '9 9 9 9 9']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = "3 2 1 4 5"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = ['2 0 4 1 3\r', '5 6 2 0 9\r', '1 4 3 7 2\r', '0 8 2 6 5\r', '3 3 1 4 1']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['3 3 3 3 3\r', '3 3 3 3 3\r', '3 3 3 3 3\r', '3 3 3 3 3\r', '2 1 2 1 2']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['1 4 2 3 5\r', '6 9 5 8 7\r', '3 7 2 6 4\r', '9 2 7 4 8\r', '5 1 3 6 8']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = "3 3 3 3 3"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = ['0 0 0 0 0\r', '0 0 0 0 1\r', '0 0 0 0 0\r', '0 0 0 0 0\r', '0 0 0 0 0']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['2 3 4 5 6\r', '1 2 3 4 5\r', '0 1 2 3 4\r', '5 4 3 2 1\r', '6 7 8 9 10']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['1 2 3 4 5\r', '0 0 0 0 1\r', '0 0 0 0 0\r', '0 0 0 0 0\r', '0 0 0 0 0']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    