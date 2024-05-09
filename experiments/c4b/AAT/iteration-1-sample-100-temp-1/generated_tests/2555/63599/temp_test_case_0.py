
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "111111101010"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "011111110"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "1010101"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "1010101010000000"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "10001000"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "101110000001011"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "00000001111111"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "1111111222222"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "10111111101"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "10111011000"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "1011000000"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "11111110000000"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "0000011111"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "1011111101"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "10111110000000"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "1010000001111111"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "11111110000000"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "10111111110"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "011111100"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "01111111"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "011111110"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "11111111000000"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "1001111101"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "01111110"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "1010101001010111"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "111111110000000"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "10000001"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "1011111111"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "11111110000000"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "1011111101011100"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "101010101110111110"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "1010101010001001101"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "11111110000000"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "101100111000"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


if __name__ == '__main__':
    unittest.main()  
    
    