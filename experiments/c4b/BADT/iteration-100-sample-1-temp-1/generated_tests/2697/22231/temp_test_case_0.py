
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['10 5', '15 10']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['16 24', '12 18']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['10 15', '20 25']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['10 6', '15 9']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['15 25', '5 10']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['2 5', '3 7']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['17 28', '34 51']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['120 50', '30 10']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['4 -6', '8 10']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['14 28', '6 10']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['8 12', '10 15']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['11 35', '17 8']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['49 14', '21 7']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['12 8', '24 18']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['10 15', '20 25']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['12 8', '5 3']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['10 20', '6 30']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['10 20', '15 25']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['12 18', '6 15']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['100 75', '50 25']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['16 10', '28 15']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['16 24', '25 35']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['10 15', '20 25']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['17 23', '11 5']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['16 24', '8 16']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


if __name__ == '__main__':
    unittest.main()  
    
    