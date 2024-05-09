
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['2 2', 'BG']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['3 2', 'BGB']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['4 1', 'BGGB']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['2 1', 'BG']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['2 2', 'BG']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['4 3', 'BGBG']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['2 1', 'BG']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['2 1', 'BG']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['3 2', 'BGB']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['2 1', 'BG']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['2 2', 'BG']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['4 2', 'BGGB']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['2 1', 'GB']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['2 3', 'BGB']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['2 2', 'BG']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['3 2', 'GBG']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


if __name__ == '__main__':
    unittest.main()  
    
    