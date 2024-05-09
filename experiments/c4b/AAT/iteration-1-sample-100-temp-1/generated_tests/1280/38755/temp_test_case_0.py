
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['5', '2 4 6 8 10']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['7', '3 1 2 4 1 3 5']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['5', '3 2 1']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = "5 1 2 3 4 5"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "10 1 2 3 4"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = ['5', '8 4 3 2']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['6', '3 1 2 4 1 2']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['5', '1 2 3']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['5', '3 2 1']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['10', '4 1 2 3 9']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['5', '3 1 2 4 6']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['5', '3', '1 2 3']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['5', '4 2 1 3 5']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['2', '3 1 4 2 2']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['5', '3 2 1 4 5']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['4', '2 1 2 2']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['5', '3 1 2 4 3']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['10', '5 5 5']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['5', '3 1 2']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['5', '3 1 4 2 2']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['5', '2 3 1 2 1']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = ['5', '10 20 30 40 50']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['5', '2 4 3 5 1']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['10', '3 3 4 4 4 5 5 5 6 6']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['5', '2 3 1 5 4']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['8', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['8', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['5', '4 2 1 3 5']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['5', '3 1 2 1 4']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['7', '2 2 4 4 6 6 8']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['7', '10 5 3 2 6 4 8']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['5', '1 2 3 4 5']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


if __name__ == '__main__':
    unittest.main()  
    
    