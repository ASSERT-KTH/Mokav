
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "5 10 15 20"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = ['2 4', '3 5']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['0 1', '2 3']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['5 8', '9 4']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['10 5', '3 6']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['3 7', '5 4']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['1 5', '7 2']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['5 10', '15 20']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = "0 2 1 5"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = ['3 10', '9 5']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = "1 3 5 7"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "10 12 15 18"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = ['0 5', '3 9']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


if __name__ == '__main__':
    unittest.main()  
    
    