
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['3', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['5', '3 2 1 4 5']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['5', '3 1 2 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['6', '11 15 20 30 35 40 43 45 47 50 55 60']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['15', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['3', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['10', '5 4 3 2 1 6 7 8 9 10']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['2', '3 1 4 1 5 9 2 6 5 3 5 8']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['20', '5 2 4 9 18 13 8 5 6 12 16 19']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = "10 1 2 3 4 5 6 7 8 9 10 11 12"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = ['3', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['5', '2 3 5 6 8 9 12 15 18 20 25 30']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['3', '1 1 1 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['4', '10 5 2 1']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['17', '9 8 7 6 5 4 3 2 1 1 1 1']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['13', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['8', '2 2 2 3 3 3 4 4 4 5 5 5']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['15', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['5', '2 4 1 3 5 6 9 7 8 10 11 12']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['20', '10 5 8 2 15 9 7 12 3 6 11 4']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['5', '15 10 5 3 2 1 1 1 1 1 1 1', '']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['5', '2 1 3 2 4 5 6 7 8 9 10 11']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['18', '4 3 2 7 8 2 4 1 9 3 2 4']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['10', '5 3 2 7 8 15 12 4 5 9 2 5']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['5', '10 5 3 2 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = ['4', '7 4 9 1 6 8 9 2 7 4 8 1']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['13', '9 8 7 6 5 4 3 2 1 0 11 10']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['13', '30 20 10 15 25 5 2 1 7 9 7 12']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['10', '6 4 3 2 1 5 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['6', '2 3 3 4 4 5']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['4', '20 10 5 5 2 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['35', '7 14 3 8 2 5 6 1 7 9 10 4']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['5', '2 1 3 4 5']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['6', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['25', '4 9 5 2 7 8 6 11 10 3 1 12']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['4', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['15', '2 4 6 8 10 12 14 16 18 20 22 24']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['7', '3 1 4 1 5 9 2 6 5 3 5 8']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['7', '2 3 4 5 6 7 8 9 10 11 12 13']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['8', '7 3 2 9 1 6 4 8 5 11 10 12']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['5', '3 2 1 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['5', '3 2 1 4 5']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = ['5', '4 5 6 7 8 9 10 11 12 13 14 15']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['6', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_47), original_source(*input_47))
            


    def test48(self):
        input_48 = ['3', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = ['5', '3 2 3 4 10']
        self.assertEqual(patched_source(*input_49), original_source(*input_49))
            


    def test50(self):
        input_50 = ['100', '10 20 30 40 50 60 70 80 90 100 110 120']
        self.assertEqual(patched_source(*input_50), original_source(*input_50))
            


    def test51(self):
        input_51 = ['4', '5 3 2 1 4 7 8 10 6 9 12 11']
        self.assertEqual(patched_source(*input_51), original_source(*input_51))
            


    def test52(self):
        input_52 = ['3', '3 2 1 4 5 6 9 8 7 10 12 11']
        self.assertEqual(patched_source(*input_52), original_source(*input_52))
            


    def test53(self):
        input_53 = ['13', '1 2 3 4 5 6 7 8 9 10 11 12 13']
        self.assertEqual(patched_source(*input_53), original_source(*input_53))
            


    def test54(self):
        input_54 = ['1 ', ' 1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_54), original_source(*input_54))
            


    def test55(self):
        input_55 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_55), original_source(*input_55))
            


    def test56(self):
        input_56 = ['2', '5 2 1 3 4 2 3 4 8 7 9 1']
        self.assertEqual(patched_source(*input_56), original_source(*input_56))
            


    def test57(self):
        input_57 = ['5', '18 14 10 8 7 7 7 5 4 3 2 1']
        self.assertEqual(patched_source(*input_57), original_source(*input_57))
            


if __name__ == '__main__':
    unittest.main()  
    
    