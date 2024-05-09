
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['2 1', 'GB']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['3 2', 'GBG']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['2 3', 'GBBG']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = "6 3 GGGBGB"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = ['2 2', 'BG']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['3 2', 'BGB']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['3 2', 'GBG']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['3 2', 'GBG']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['4 3', 'BGBG']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['3 2', 'GBGBGB']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['2 2', 'GB']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['3 2', 'GGGB']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = "3 1 BGG"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "2 3 GBB"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = ['2 1', 'GB']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = "3 2 BGGB"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = ['3 3', 'GBB']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = "3 3 ABC"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = ['8 3', 'GBGBGBGB']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['3 2', 'BGG']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['5 2', 'GBGBG']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['4 2', 'BGGB']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['2 2', 'GB']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


if __name__ == '__main__':
    unittest.main()  
    
    