
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['3 4', '2 3']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['10 20 100 200', '2 3']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['3 6', '2 3']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['2 4 8 16', '2 4']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['3 5', '4 6']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['4 6 10 12', '2 3']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['2 3 6 9', '3 3']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['3 5 9 11', '2 3']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['10 15', '2 3']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['2 2 6 6', '3 3']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['1 1 3 3', '2 2']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['1 4', '2 3']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['10 20 30 40', '5 10']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['3 5 9 11', '2 3']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['3 7', '2 5']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['4 3 10 7', '2 4']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['10 15', '5 5']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['0 0 2 2', '1 1']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['2 2 8 8', '2 2', '']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['1 3 5 7', '2 4']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['4 4 6 6', '2 2']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['1 1 3 3', '1 2']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['4 5 10 12', '2 3']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['4 6 10 10', '2 5']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['3 5 7 9', '2 4']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['2 7 5 8', '1 1']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = "1 3 4 5 2 3"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = ['10 15', '5 3']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['1 2 3 4', '2 2']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['4 4 10 10', '2 2']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['3 5 9 13', '2 3']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['6 2', '2 1']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['3 4 7 10', '2 5', '']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['9 3', '3 1']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['1 2 4 5', '2 3']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['3 3 6 6', '2 2']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['8 3', '2 2']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['1 3', '2 4']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['2 3 8 9', '1 1']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['0 0 2 2', '1 1']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['5 8 15 20', '2 4']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['3 5 9 11', '2 3']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['5 5 10 10', '2 2']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['4 4 8 8', '2 2']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['4 6', '2 3']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = ['10 10 20 20', '2 3']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['1 3 5 7', '2 2']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = ['5 10 15 20', '2 3']
        self.assertEqual(patched_source(*input_47), original_source(*input_47))
            


    def test48(self):
        input_48 = ['3 3 9 9', '1 1']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = "1 4 4 1 1 2"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = ['4 6', '2 3']
        self.assertEqual(patched_source(*input_50), original_source(*input_50))
            


if __name__ == '__main__':
    unittest.main()  
    
    