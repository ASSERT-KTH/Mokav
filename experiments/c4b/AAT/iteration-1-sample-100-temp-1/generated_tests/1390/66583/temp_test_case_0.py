
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "20 30 10"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "25 10 3"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "75 30 40"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "10 50 30"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "70 35 26"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "60 50 30"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "100 20 25"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "80 10 9"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "20 30 10"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "10 20.5 29.5"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "10 50 40"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "500 20 30"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "20 5 13"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "50 30 15"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "100 20 30"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "20 15 10"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "400 20 2"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "200 45.6 20.5"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "10 20 30"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "50 10 5"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "5 20 30"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "10 30 40"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "20 30 40"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "5 50 30"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "100 20 5"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "50 20 25"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "200 20 30"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "20 10.0 30.0"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "5 40 10"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "10 30 25"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "12.5 20.0 7.0"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "100 30 40"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "120 50 30"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "150 20 10"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "100 50 20"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "10 50 60"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "100 30 25"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "45 20 10"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "100 20 10"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "150 50 20"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "20 10 5"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "10 20.5 15"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "100 50 60"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "100 20 30"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "10 50 20"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "80 25 20"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "100 30 25"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "250 10 20"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "100 20 30"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "20 30 25"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "50 20 30"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "150 20 30"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "200 10 10"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "12 20 30"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "5 20 10"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "20 50 10"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "80 30 7"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "10 20 30"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "50 20 10"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "100 20 10"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "75 32.5 10"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "20 50 10"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "50 20 10"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "10 50 20"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "200 50 75"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "105 20 20"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "98 35 33"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "9 80 1"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "15 10 20"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "500 20 25"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "10 50 30"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "82.982 23.156 20.0"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "10 -1 20"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "100 20 30"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "30 20 25"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "5 20 30"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "50 20 30"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "70 50.0 35.0"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "50 30 20"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "10 50 40"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "100 50 60"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "100 20 25"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "100 10 20"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "100 20 15"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "900 10 300"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


if __name__ == '__main__':
    unittest.main()  
    
    