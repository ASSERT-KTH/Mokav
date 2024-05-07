
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['5', '7 3 2 9 5 8 11 10 6 15 1 4']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['100', '50 30 20 10 5 4 3 2 1 1 1 1']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['7', '1 2 3 4 5 6 7']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


if __name__ == '__main__':
    unittest.main()  
    
    