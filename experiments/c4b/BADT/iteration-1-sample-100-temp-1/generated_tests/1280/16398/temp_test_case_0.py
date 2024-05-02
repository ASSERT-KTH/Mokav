
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['4\r', '1 3 2 5 4 6 1 2 3 4 2 2']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['10\r', '10 8 6 4 2 0 0 2 4 6 8 10']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['15\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['7\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['3\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['7\r', '2 1 1 3 2 2 1 1 1 2 1 1']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['10\r', '1 1 2 2 2 2 3 3 3 3 3 3']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['6\r', '1 3 2 5 4 4 7 1 0 9 6 8']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['10', '5 5 4 3 2 1 1 2 3 4 5 6']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['15\r', '10 4 3 2 1 7 5 6 8 9 11 12 13 14']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = ['6\r', '3 4 5 6 7 8 9 10 11 12 13 14']
        self.assertEqual(patched_source(*input_10), original_source(*input_10))
            


    def test11(self):
        input_11 = ['3\r', '1 1 1 2 2 2 2 2 1 2 3 1']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = ['5\r', '1 1 1 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['10\r', '4 1 3 9 2 8 5 7 6 10 11 12']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = ['7\r', '5 3 2 2 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_15), original_source(*input_15))
            


    def test16(self):
        input_16 = ['10', '1 2 3 1 5 4 3 2 4 1 6 7']
        self.assertEqual(patched_source(*input_16), original_source(*input_16))
            


    def test17(self):
        input_17 = ['3\r', '1 1 1 2 1 3 2 3 4 1 3 1']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = ['6', '3 2 4 1 5 3 2 1 2 3 2 1']
        self.assertEqual(patched_source(*input_18), original_source(*input_18))
            


    def test19(self):
        input_19 = ['7\r', '3 1 5 2 2 1 4 5 2 1 1 1']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['5\r', '3 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['6\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = ['10\r', '4 3 8 2 6 10 1 7 5 9 11 0 12']
        self.assertEqual(patched_source(*input_23), original_source(*input_23))
            


    def test24(self):
        input_24 = ['10\r', '1 5 3 6 7 2 9 8 10 4 12 11']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = ['6\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_25), original_source(*input_25))
            


    def test26(self):
        input_26 = ['10\r', '5 5 5 5 5 5 5 5 1 1 1 1']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['6\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['7\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['3\r', '1 2 2 3 2 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = ['15\r', '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15']
        self.assertEqual(patched_source(*input_31), original_source(*input_31))
            


    def test32(self):
        input_32 = ['4\r', '1 3 1 2 3 1 2 3 2 1 2 1']
        self.assertEqual(patched_source(*input_32), original_source(*input_32))
            


    def test33(self):
        input_33 = ['7\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_33), original_source(*input_33))
            


    def test34(self):
        input_34 = ['10', '1 2 3 4 5 6 7 8 9 10 11 12 13']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['6\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['7\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['8\r', '1 2 1 3 4 5 6 7 8 9 10 11']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = ['12\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_38), original_source(*input_38))
            


    def test39(self):
        input_39 = ['8\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['10\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['4', '3 2 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['10\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = ['10', '3 1 4 1 5 9 2 6 5 3 5 8']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['10', '10 10 10 10 10 10 10 10 10 10 10 10']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = ['3\r', '3 3 3 3 4 4 3 3 3 3 3 3']
        self.assertEqual(patched_source(*input_47), original_source(*input_47))
            


    def test48(self):
        input_48 = ['6', '2 2 4 5 7 0 0 6 5 4 2 3']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = ['10\r', '2 2 2 2 2 2 2 2 2 2 2 2']
        self.assertEqual(patched_source(*input_49), original_source(*input_49))
            


    def test50(self):
        input_50 = ['10\r', '1 2 3 1 5 6 4 7 1 2 1 3']
        self.assertEqual(patched_source(*input_50), original_source(*input_50))
            


    def test51(self):
        input_51 = ['5\r', '1 1 1 1 2 2 3 2 1 2 2 1']
        self.assertEqual(patched_source(*input_51), original_source(*input_51))
            


    def test52(self):
        input_52 = ['10\r', '3 6 9 1 1 1 5 3 2 8 3 2']
        self.assertEqual(patched_source(*input_52), original_source(*input_52))
            


    def test53(self):
        input_53 = ['10\r', '3 2 1 3 2 1 2 1 3 1 2 3']
        self.assertEqual(patched_source(*input_53), original_source(*input_53))
            


    def test54(self):
        input_54 = ['7\r', '3 3 3 2 2 2 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_54), original_source(*input_54))
            


    def test55(self):
        input_55 = ['4\r', '2 2 3 4 1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_55), original_source(*input_55))
            


    def test56(self):
        input_56 = ['10\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_56), original_source(*input_56))
            


    def test57(self):
        input_57 = ['3\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_57), original_source(*input_57))
            


    def test58(self):
        input_58 = ['15\r', '7 3 2 8 5 7 2 1 4 7 9 6 8 8 4']
        self.assertEqual(patched_source(*input_58), original_source(*input_58))
            


    def test59(self):
        input_59 = ['7', '3 5 1 6 8 2 4']
        self.assertEqual(patched_source(*input_59), original_source(*input_59))
            


    def test60(self):
        input_60 = ['5\r', '1 1 1 1 2 2 3 2 2 3 1 1']
        self.assertEqual(patched_source(*input_60), original_source(*input_60))
            


    def test61(self):
        input_61 = ['1\r', '3 4 1 2 3 2 3 1 3 1 1 2']
        self.assertEqual(patched_source(*input_61), original_source(*input_61))
            


    def test62(self):
        input_62 = ['10\r', '5 2 8 1 7 3 6 4 10 9 1 2']
        self.assertEqual(patched_source(*input_62), original_source(*input_62))
            


    def test63(self):
        input_63 = ['8\r', '3 1 4 1 5 9 2 6 5 3 5 8']
        self.assertEqual(patched_source(*input_63), original_source(*input_63))
            


    def test64(self):
        input_64 = ['-5\r', '1 2 2 3 4 5 6 7 8 9 10 11']
        self.assertEqual(patched_source(*input_64), original_source(*input_64))
            


    def test65(self):
        input_65 = ['15\r', '5 3 4 2 8 7 10 6 9 11 15 12']
        self.assertEqual(patched_source(*input_65), original_source(*input_65))
            


    def test66(self):
        input_66 = ['20\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_66), original_source(*input_66))
            


    def test67(self):
        input_67 = ['7\r', '1 1 1 1 1 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_67), original_source(*input_67))
            


    def test68(self):
        input_68 = ['3\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_68), original_source(*input_68))
            


    def test69(self):
        input_69 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_69), original_source(*input_69))
            


    def test70(self):
        input_70 = ['10', '5 10 15 20 25 30 35 40 45 50 55 60']
        self.assertEqual(patched_source(*input_70), original_source(*input_70))
            


    def test71(self):
        input_71 = ['10\r', '5 1 3 7 6 8 2 4 10 9 11 12']
        self.assertEqual(patched_source(*input_71), original_source(*input_71))
            


    def test72(self):
        input_72 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_72), original_source(*input_72))
            


    def test73(self):
        input_73 = ['10\r', '5 5 10 10 15 15 20 20 25 25 30 30']
        self.assertEqual(patched_source(*input_73), original_source(*input_73))
            


    def test74(self):
        input_74 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_74), original_source(*input_74))
            


    def test75(self):
        input_75 = ['7\r', '5 3 2 2 2 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_75), original_source(*input_75))
            


    def test76(self):
        input_76 = ['7\r', '3 3 3 2 2 2 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_76), original_source(*input_76))
            


    def test77(self):
        input_77 = ['8', '3 5 2 1 4 5 6 3 4 2 1 3']
        self.assertEqual(patched_source(*input_77), original_source(*input_77))
            


    def test78(self):
        input_78 = ['6\r', '1 1 1 1 2 2 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_78), original_source(*input_78))
            


    def test79(self):
        input_79 = ['6\r', '1 1 1 1 1 2 2 3 2 2 1 1']
        self.assertEqual(patched_source(*input_79), original_source(*input_79))
            


    def test80(self):
        input_80 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_80), original_source(*input_80))
            


    def test81(self):
        input_81 = ['10\r', '8 9 7 6 5 3 4 1 2 10 11 12']
        self.assertEqual(patched_source(*input_81), original_source(*input_81))
            


    def test82(self):
        input_82 = ['10\r', '6 2 5 1 3 4 6 2 5 1 3 4']
        self.assertEqual(patched_source(*input_82), original_source(*input_82))
            


    def test83(self):
        input_83 = ['15', '5 5 5 5 5 5 5 5 5 5 5 5 5 5 6']
        self.assertEqual(patched_source(*input_83), original_source(*input_83))
            


    def test84(self):
        input_84 = ['6\r', '1 1 2 2 3 3 3 2 2 1 1 1']
        self.assertEqual(patched_source(*input_84), original_source(*input_84))
            


    def test85(self):
        input_85 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_85), original_source(*input_85))
            


    def test86(self):
        input_86 = ['10\r', '3 4 1 5 2 7 6 8 10 9 11 12']
        self.assertEqual(patched_source(*input_86), original_source(*input_86))
            


    def test87(self):
        input_87 = ['10\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_87), original_source(*input_87))
            


    def test88(self):
        input_88 = ['9\r', '5 4 3 2 1 1 2 3 4 5']
        self.assertEqual(patched_source(*input_88), original_source(*input_88))
            


    def test89(self):
        input_89 = ['10\r', '2 4 6 8 10 12 14 16 18 20 22 24']
        self.assertEqual(patched_source(*input_89), original_source(*input_89))
            


    def test90(self):
        input_90 = ['7\r', '2 3 1 4 5 6 1 3 2 2 1 2']
        self.assertEqual(patched_source(*input_90), original_source(*input_90))
            


    def test91(self):
        input_91 = ['3\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_91), original_source(*input_91))
            


    def test92(self):
        input_92 = ['3\r', '3 3 3 3 4 5 6 6 7 8 8 8']
        self.assertEqual(patched_source(*input_92), original_source(*input_92))
            


    def test93(self):
        input_93 = ['20\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_93), original_source(*input_93))
            


    def test94(self):
        input_94 = ['0', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_94), original_source(*input_94))
            


    def test95(self):
        input_95 = ['20\r', '1 2 3 4 5 6 7 8 9 10 11 12']
        self.assertEqual(patched_source(*input_95), original_source(*input_95))
            


    def test96(self):
        input_96 = ['5\r', '1 1 1 1 2 2 3 2 2 1 1 2']
        self.assertEqual(patched_source(*input_96), original_source(*input_96))
            


    def test97(self):
        input_97 = ['14\r', '1 2 3 4 5 6 7 8 9 10 11 12 13 14']
        self.assertEqual(patched_source(*input_97), original_source(*input_97))
            


    def test98(self):
        input_98 = ['3\r', '3 3 3 3 3 3 3 3 3 3 3 3']
        self.assertEqual(patched_source(*input_98), original_source(*input_98))
            


    def test99(self):
        input_99 = ['20\r', '30 15 5 25 25 20 10 15 5 5 35 30']
        self.assertEqual(patched_source(*input_99), original_source(*input_99))
            


if __name__ == '__main__':
    unittest.main()  
    
    