
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "0 0 1 1 1 2 2 3 3 4 4 5 5 6 6 7 100 100 100 100 100"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "5 5 5 2 1"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "7 3 7 3 20 100 1 100 1"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "4 4 4 7 9 9 9"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "3 3 3 4 5"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "4 4 4 5 5"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "1 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "10 10 10 20 20"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "2 2 2 1 1"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


if __name__ == '__main__':
    unittest.main()  
    
    