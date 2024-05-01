
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['7\r', '5 5 5 4 4 4 3 3 3 2 2 2 1 1 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['5\r', '1 2 2 1 3 2 1 1 1 1 2 1']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['12\r', '7 5 8 3 2 1 4 6 11 10 12 9']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['7\r', '1 2 3 4 5 6 7 8 9 10 11 12 13 14']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['7\r', '9 10 6 5 1 1 2 3 4 7 8 13']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['12\r', '5 5 5 4 3 3 2 2 2 1 1 1']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['10\r', '10 9 8 7 6 5 4 3 2 1']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['5\r', '1 5 2 3 4 7 6 9 8 10 11']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['15\r', '4 5 6 7 8 9 10 11 12 13 14 15 16 17 18']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    