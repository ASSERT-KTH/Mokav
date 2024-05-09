
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['4\r', 'RRRR']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['4\r', 'GGRR']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['5\r', 'AAAAA']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['6\r', 'RRGG']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['5\r', 'AAA']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['3\r', 'R']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['2\r', 'X']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['2\r', 'AA']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['3\r', 'RRB']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['3\r', 'RG']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    