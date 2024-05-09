
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['7', '1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = "8 1 2 3 4 5 6 7 8"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "7 5 3 1 2 4 6"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "2 3 4 5 6 7 8 1"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = ['7', '1 2 3 4 5 6 7']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = "7 6 5 4 3 2 1"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "7 6 5 4 3 2 1"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "7 2 2 2 2 2 2 2"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "7 1 2 3 4 5 6 7 8"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "5 1 2 3 4 5"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "7 3 1 2 4 5 6 7"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "7 5 3 1 2 4 6"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "7 3 2 4 5 3 1"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = ['7', '1 2 3 4 5 6 7']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['14', '1 2 3 4 5 6 7 8 9 10 11 12 13 14']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = "7 5 3 2 8 6 4"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


if __name__ == '__main__':
    unittest.main()  
    
    