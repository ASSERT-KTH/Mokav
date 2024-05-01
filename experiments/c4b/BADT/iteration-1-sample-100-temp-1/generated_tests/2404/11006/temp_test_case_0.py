
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['WBWBWBWB\r', 'BBBBBBBB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['WBWWBBWW\r', 'BBBBBBBW\r', 'WBWWBBWW\r', 'WBWBWBWW\r', 'WWWWWBWW\r', 'WBWWBWWW\r', 'BBWWBBBW\r', 'BWBBBWBW']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB\r', 'WBWBWBWB']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['BBBBCBBB\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['BBBWWBBB\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['BBBBBBBB\r', 'BWWBBWBW\r', 'BBWBWWBB\r', 'WBWBBWBB\r', 'WWBWWWBB\r', 'WWBBBWBB\r', 'BWBBBWBB\r', 'BWWBWBBB']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWWWBWW']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['BWWBWWBW\r', 'BBBBBWWB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['BWBWWBBBB\r', 'BBBWWBBB\r', 'WWBBWBWW\r', 'BBWBWBWB\r', 'BBBWWBBW\r', 'BWBBBWWW\r', 'BBWBWBBW\r', 'BBWBBBWB']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['WWBWWBWW\r', 'BBBBBBBB\r', 'WWBWWBWW\r', 'WBBWWBBW\r', 'WBBWWBBW\r', 'WWBWWBWW\r', 'WWBWWBWW\r', 'WWBWWBWW']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['WWWWWWWW\r', 'BBBBBBBB\r', 'WWWWWWWW\r', 'WWWWWWWW\r', 'WWWWWWWW\r', 'WWWWWWWW\r', 'WWWWWWWW\r', 'WWWWWWWW']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['BWBWBWBW\r', 'BBBBBBBB\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBBWBWB\r', 'BWBBWBWB\r', 'BWBBWBWB\r', 'BWBBWBWB']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['BBBBBBBB\r', 'WBWWBWWW\r', 'WBWWBWWW\r', 'WBWWBWWW\r', 'WBWWBWWW\r', 'WBWWBWWW\r', 'WBWWBWWW\r', 'WBWWBWWW']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['BWWBWBBW\r', 'BBBBBWBW\r', 'BBBWBWWW\r', 'BBBBBBWB\r', 'BWBWWBWW\r', 'WBWWBWWW\r', 'BWBWBWWB\r', 'BWBBBWBB']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['WWBWBBBB\r', 'WWBWBBBW\r', 'WWBWBBBB\r', 'WWBWBBBB\r', 'WWBWBBBB\r', 'WWBWBBBB\r', 'WWBWBBBB\r', 'WWBWBBBB']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['BBBWBBBW\r', 'BBBWWBBW\r', 'BBBWWBBW\r', 'WWBWWWWB\r', 'WBWWBWBW\r', 'WBBWWBBW\r', 'BWBBWBWB\r', 'BWWBWWWW']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = ['WBBWBBBB\r', 'BBBBBBBB\r', 'WWBBWWBW\r', 'WWWBWWBW\r', 'WBBWWBBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWBWWBBW']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = ['BWBWBWBW\r', 'BBBBBBBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['BBBBBBBB\r', 'BWWBWBWB\r', 'BWBBWBWB\r', 'BBBWWBWB\r', 'BBBBBWWB\r', 'BBBWWWWB\r', 'BWBBBWWB\r', 'BWWBBBBB']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['BBBBBBBB\r', 'BBWWBBBW\r', 'BWBBWBBW\r', 'BBBBBBBW\r', 'WWBBWBWW\r', 'BBBBWBBB\r', 'BBBBBBBB\r', 'BBBBBBBW']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBWBW\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['WWWBWWWB\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['BBBBBBBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBW\r', 'BBBBBBBW\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['BWWBWWBW\r', 'WWBWWBWW\r', 'BWBBWWBB\r', 'BWBBWWBW\r', 'BWBBWWBW\r', 'BWBWWBWB\r', 'BWBWWBWW\r', 'WWBWWBWW']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['BBBWBBBW\r', 'BBBBBBBB\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['WWWBWWWB\r', 'BBBBBBBB\r', 'WWWBWWWB\r', 'WWWBWWWB\r', 'WWWBWWWB\r', 'WWWBWWWB\r', 'WWWBWWWB\r', 'WWWBWWWB']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['BBBBBBBB\r', 'BBBBBWBW\r', 'BBBBBBBW\r', 'BBBBBBBW\r', 'BBBBBBBW\r', 'BBBBBBBW\r', 'BBBBBBBW\r', 'BBBBBBBW']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWB WWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWBWWBW\r', 'WWWWWWWW']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['BBBWBBBW\r', 'BBBBBBBB\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW\r', 'BBBWBBBW']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = ['BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW\r', 'BBBBBBBB\r', 'WWWBWWBW']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['BBBBBBBW\r', 'BBBBBBBB\r', 'BBBBBWBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = ['BBBBBBBB\r', 'BWWBWWBW\r', 'BWWBWWBW\r', 'BWWBWWBW\r', 'BWWBWWBW\r', 'BWWBWWBW\r', 'BWWBWWBW\r', 'BWWBWWBW']
        self.assertEqual(patched_source(*input_47), original_source(*input_47))
            


    def test48(self):
        input_48 = ['BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB\r', 'BBBBBBBB']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = ['BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW\r', 'BWBWBWBW']
        self.assertEqual(patched_source(*input_49), original_source(*input_49))
            


if __name__ == '__main__':
    unittest.main()  
    
    