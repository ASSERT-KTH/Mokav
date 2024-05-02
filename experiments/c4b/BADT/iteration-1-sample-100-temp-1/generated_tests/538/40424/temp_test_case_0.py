
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "10 10 10 5 5"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "1 1 1 2 2"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "5 5 5 4 4"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "7 7 7 7 7 7 20"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "10 10 10 1 1 1 2 2 3 4"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "15 20 15 20 15"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "5 5 5 4 4 3 3 3 2 2 2 1 1 1 0 0 0"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "3 3 3 3 3 3 3 3 3 3"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "2 2 2 3 3"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "4 4 4 5 6 7 8 9 9 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 24 25 25 25 26 27 28 29 30 30 31 32 33 34 35 36 37 38 39 40 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 45 46 47 48 49 60 61 62 63 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "7 7 7 3 20"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "5 5 5 6 6"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "9 9 9 9 9 9 9 4 1 2 3 3 3 4 3 3 21"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "5 5 5 7 7"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "10 10 10 9 9"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "5 5 5 3 20"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "5 5 5 3 2"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "1 1 2 3 4"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "4 4 4 7 7 20 20 30 30 30 40 40 40 91 91 91 91 99 99 99"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "1 1 1 2 2 3 3 4 4"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "6 2 6 2 10"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "1 2 3 4 5"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "1 2 3 4 5 6 7 8 9 10"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "5 5 5 5 5 5 5 5 2 3 4 6 1"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "1 2 2 3 3"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "4 3 3 3 2"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "7 3 7 3 7"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "10 20 10 20 10"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "1 1 1 2 2"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "4 2 1 4 3 3 4 4 3 2"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "7 7 7 3 3"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "5 5 5 10 20"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "5 5 5 3 2 1"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "10 10 10 10 10 10 10 10 10 10 20 20 20 20 20 30 30 30 30 40 40 40 50 50 60 60 70 70 80 90 100"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "1 1 1 2 2"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "4 4 4 2 2"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "7 7 7 3 20"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "1 1 2 2 3 3 4 5 6 7 9"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "2 2 2 3 3"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 4 100 52 21 45 65 8 9 38 49 20 16 38 14 3 45 5 19 30 25 22 23 44 36 7 8 12 13 17 43 55 33 11 8 23 35 23 3 23 12 23 36 3 5 6 20 7 8 23 12 11 44 36 23 19 3 7 8 23 12 23 3 20 17 23 13 23 3 23 11 8 6 20 7 8 23 12 11 13 17 13 11 8 7 13 11 17 13 11 7 13 11 17 13 11 7 13 15 17 13 11 6 10 10 78 32 5 7 3 33 676 32 4 2 6 7 8 3 4 23 8 10 23 4 26 6 23 4 11 2 75 34 8 3 2 34 6 3 2 5 80 3 7 92 5 9 12 37 5 4 67 3 6 1 76 3 57 1 3 2 4 2 6 7 24 35 23 3 27 39 6 12 34 23 27 7 3 88 16 23 4 2 56 7 23 7 12 4 65 3 45 6 23 56 7 34 23 32 34 65 3 6 42 2 2 4 23 44 6 3 23 2 6 7 23 4 23 34 65 3 46 23 7 34 6 5 8 23 25 6 4 23 2 6 7 6 4 5 34 2 56 3 10 4 12 5 6 3 2 4 23 44 6 8 23 23 23 23 45 23 88 34 6 7 23 23 24 7 45 34 6 90 56 3 6 24 2 14 3 12 8 90 90 23 7 34 34 56 9 7 76 3 2 4 67 3 6 12 23 4 34 24 5 2 34 5 3 6 8 23 34 45 23 76 3 6 23 12 23 46 8 3 4 6 8 42 23 34 7 32 3 56 8 3 2 4 6 12 34 76 3 56 7 23 78 56 34 12 45 23 35 3 1 6 5 6 23 4 2 34 6 90 47 7 23 20 24 1 6 90 76 3 4 23 4 23 6 8 7 3 23 4 6 24 45 35 23 34 12 96 3 6 4 23 11 7 34 23 54 35 6 23 5 7 3 1 12 24 45 3 78 6 32 3 1 6 34 24 23 7 23 6 12 34 3 56 7 23 78 6 34 12 45 23 24 3 6 1 3 20"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "8 8 8 8 8 8 8"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "4 4 4 4 4 4 4 4 4 4 4 4 8 9"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "3 3 3 2 2"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "2 2 2 4 5"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "10 10 10 20 20"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "4 4 4 6 100 100 100 1 1 1"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "3 3 3 3 3 3 8 10 10 10 15 15 15 20 20 20 20 20"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "7 7 7 3 3"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "4 4 4 3 20"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "8 3 7 3 20"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "7 3 7 3 20 20"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "3 3 3 4 4 4 4 5 5 5 5 100 100 100"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "5 5 5 4 3"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "7 7 7 3 3 20"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "1 1 1 2 2 2 3 3 3 4 4 4 5 5 5"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "4 4 4 4 4"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "8 8 8 3 20"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "5 1 1 3 3"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "1 1 1 2 2 2 3 3 3 4 4 5 5 5 5"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "1 2 3 4 5 6"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "1 2 3 4 5 5 5 6 6 6 7 7 7 8 9 10 11 12 15 100"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "4 4 4 5 6"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "1 2 3 4 5 6 7"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "5 5 5 5 5"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "3 3 3 4 4 4 5 5 5 6 6 6 7 7 7"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "1 2 2 3 3 4 4 4 5 5 5 6 6 6 7 7 8 8 9 9 10"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "10 10 10 20 20"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "8 4 8 4 16"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "1 2 3 4 5 6 7 8 9"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "7 3 7 3 20 10"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "5 7 9 9 9"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "7 3 7 3 20 16 16 16 16 16 16"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "5 5 5 6 6"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "6 6 6 4 4 4 2 2 2 100 100 100 50 50 50 30 30 30 9 9"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


    def test90(self):
        input_90 = "7 7 7 3 20"
        self.assertEqual(patched_source(input_90), original_source(input_90))
            


    def test91(self):
        input_91 = "5 5 5 4 4"
        self.assertEqual(patched_source(input_91), original_source(input_91))
            


    def test92(self):
        input_92 = "1 1 1 2 50"
        self.assertEqual(patched_source(input_92), original_source(input_92))
            


    def test93(self):
        input_93 = "1 1 1 3 5"
        self.assertEqual(patched_source(input_93), original_source(input_93))
            


    def test94(self):
        input_94 = "5 5 5 4 4"
        self.assertEqual(patched_source(input_94), original_source(input_94))
            


    def test95(self):
        input_95 = "1 1 1 2 3"
        self.assertEqual(patched_source(input_95), original_source(input_95))
            


if __name__ == '__main__':
    unittest.main()  
    
    