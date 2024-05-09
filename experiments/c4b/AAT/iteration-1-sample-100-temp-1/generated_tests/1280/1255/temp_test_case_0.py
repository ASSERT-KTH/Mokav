
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['200', '45 67 89 12 34 56 78 90 23 45 67 89']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['7', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['5', '3 2 1 6 4']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['8', '2 3 1 5 4 6 7 8 9 11 10 12']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['10', '7 2 3 4 5 6 1 8 9 10 11 12']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['15', '4 2 3 1 5 10 7 6 8 9 12 11']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['5', '3 2 1 0 0 0 0 0 0 0 0 0']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['10', '5 3 2 2 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['20', '10 5 4 3 2 1 0 9 8 7 6 11']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['15', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['12', '10 1 8 3 4 7 5 12 2 6 11 9']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['11', '23 45 6 78 9 10 21 32 43 54 65 76']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['10', '2 3 5 7 11 13 17 19 23 29 31 37']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['50', '23 45 67 12 34 56 78 90 21 43 65 87']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['90', '97 54 38 2 49 81 69 41 57 17 79 2']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['6', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12', '']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['8', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['3', '5 5 5 3 1 2 1 9 1 0 10 3']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['20', '13 5 2 1 0 0 0 0 0 0 0 0']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['1', '1 2 3 4 5 6 7 8 9 10 11']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['3', '2 2 2 2 2 2 2 2 2 2 2 2']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = ['15', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = ['25', '5 5 5 5 5 5 5 5 5 5 5 5']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['13', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['10', '5 2 1 3 4 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['1', '5 2 1 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['7', '4 2 3 1 5 6 0 9 8 10 7 11']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['7', '4 2 1 0 0 0 0 0 0 0 0 0']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['5', '2 1 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['15', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 17']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['11', '4 3 2 2 1 0 0 0 0 0 0 0']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['13', '1 2 3 4 5 6 7 8 9 10 11 12 13']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['20', '10 9 8 7 6 5 4 3 2 1 0 -1']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['100', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['25', '10 5 6 9 8 7 4 3 2 1 11 12']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['10', '20 5 5 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_47), original_source(*input_47))
            


    def test48(self):
        input_48 = ['14', '1 1 4 5 6 7 10 11 12 13 14 15 16']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = ['15', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_49), original_source(*input_49))
            


    def test50(self):
        input_50 = ['4', '10 2 6 5 7 9 1 3 4 8 0 0']
        self.assertEqual(patched_source(*input_50), original_source(*input_50))
            


    def test51(self):
        input_51 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_51), original_source(*input_51))
            


    def test52(self):
        input_52 = ['5', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_52), original_source(*input_52))
            


    def test53(self):
        input_53 = ['6', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_53), original_source(*input_53))
            


    def test54(self):
        input_54 = ['5', '3 2 1 4 6 9 8 7 5 10 11 12']
        self.assertEqual(patched_source(*input_54), original_source(*input_54))
            


    def test55(self):
        input_55 = ['11', '15 10 7 4 3 2 1 1 0 0 0 0']
        self.assertEqual(patched_source(*input_55), original_source(*input_55))
            


    def test56(self):
        input_56 = ['5', '10 20 30 40 50 60 70 80 90 100 110 120']
        self.assertEqual(patched_source(*input_56), original_source(*input_56))
            


if __name__ == '__main__':
    unittest.main()  
    
    