
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "120 96 36"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "7 13 20"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "21 9 6"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "10 15 25"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "54 36 18"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "48 18 12"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "10 15 5"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "4 6 12"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "4 6 8"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "18 24 12"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "75 105 105"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "15 25 10"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "30 20 10"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "24 48 36"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "12 15 9"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "9 6 15"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "12 18 24"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "48 18 6"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "10 15 25"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "36 12 24"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "25 20 15"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "12 24 18"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "18 24 30"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "48 18 42"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "20 50 75"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "54 27 9"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "24 36 60"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "18 24 30"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "30 15 5"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "16 24 8 12"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "10 15 20"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "9 15 21"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "48 18 6"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "15 27 39"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "12 18 24"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "30 20 10"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "15 21 9"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "15 20 25"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "24 36 6"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "8 12 18"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "12 18 24"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "18 24 30"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


if __name__ == '__main__':
    unittest.main()  
    
    