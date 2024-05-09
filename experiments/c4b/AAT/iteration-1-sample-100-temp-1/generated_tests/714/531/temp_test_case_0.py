
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "0 10 5 15 7"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "20 30 10 40 15"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "5 10 1 15 3"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "24648817341102 24648817341102 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "1 5 2 6 3"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = ['26809585729892 79562017413902 78425477889227 91635263036702 47775690462274', '']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "355004 355004 355004 355004 355004"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "6 8 4 10 5"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "35 50 25 40 30"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "21 30 15 25 18"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "202 409 99 500 150"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = ['24648817341102 41165114064236 88046848035 13602161452932 10000831349205', '']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "951621245713 951621245714 2 2 1"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "5 10 1 8 3"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "79 122 45 95 60"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = ['187 273 83 347 250', '']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "5 10 3 8 4"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = ['19888888 50000000 22222222 88888888 33333333', '']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = "4 8 2 6 5"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "12 14 15 17 13"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "2548398623 1248398624 64738912 1248398624 64738912"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "219 623 123 745 500"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = ['6 8 2 10 4', '']
        self.assertEqual(patched_source(*input_27), original_source(*input_27))
            


    def test28(self):
        input_28 = ['25333397806 59154347807 16366381490 43209860912 2941172323', '']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = "10 20 15 25 12"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "14 20 8 26 10"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "7 9 4 11 5"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "1 5 3 7 4"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "363958947 678969452 111405897 567441451 519765631"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "10 15 5 20 8"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = ['42 17 35 65 25', '']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = "1 5 7 10 3"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "20 30 10 15 25"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "3 5 2 6 4"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "12 15 10 20 18"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "10 20 5 15 7"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = ['24648817341102 41165114064236 88046848035 13602161452932 10000831349205', '']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = "36269398003 648803611600 11818166469 298600625517 569361229"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = ['150 200 50 100 75', '']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "13 20 8 25 15"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = ['34058331026371 41287095116599 57984601502006 37271223633036 40441505971264', '']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = "13 15 10 20 12"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "11 15 7 20 10"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "1749116310547 2909630973958 29517242608120 43221128752660 24520700751939"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "117 200 50 150 80"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "24648817341102 41165114064236 88046848035 13602161452932 999999999"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = ['19834348285303 39765114064236 88046848035 12602161452932 9000831349205', '']
        self.assertEqual(patched_source(*input_54), original_source(*input_54))
            


    def test55(self):
        input_55 = "123456789 234567890 345678901 456789012 567890123"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "10 20 5 15 8"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "10000000000001 20000000000000 30000000000000 40000000000000 25000000000000"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "9 11 5 15 7"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = ['255 500 100 400 50', '']
        self.assertEqual(patched_source(*input_59), original_source(*input_59))
            


    def test60(self):
        input_60 = "1 5 3 7 4"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "1999840111446633 3332986643658309 6457482147153479 9998937757996839 4980854520814021"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = ['21612094829252 31741948124979 984912480 140940912849 1009084912048', '']
        self.assertEqual(patched_source(*input_64), original_source(*input_64))
            


    def test65(self):
        input_65 = "5 10 3 8 4"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "10000000000000 20000000000000 30000000000000 40000000000000 25000000000000"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "350271190 745611648 872237626 625026947 708578734"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "3 5 6 8 4"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "462270466296 585675244871 480964801089 752417707647 281252971067"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = ['10 20 30 40 25', '']
        self.assertEqual(patched_source(*input_70), original_source(*input_70))
            


    def test71(self):
        input_71 = ['24648817341102 41165114064236 88046848035 13602161452932 10000831349205', '']
        self.assertEqual(patched_source(*input_71), original_source(*input_71))
            


    def test72(self):
        input_72 = "24648817341102 41165114064236 88046848035 13602161452932 9876543210"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "115450 315450 230450 430450 320450"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "500 600 400 700 450"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "3 6 1 8 5"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = ['29177553369807 29177553369807 9177553369807 9177553369807 9177553369807', '']
        self.assertEqual(patched_source(*input_76), original_source(*input_76))
            


    def test77(self):
        input_77 = "10000000000000 20000000000000 15000000000000 25000000000000 30000000000000"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = ['19992335507804 19992356320408 3972258937839 14479427304389 19992342264168', '']
        self.assertEqual(patched_source(*input_78), original_source(*input_78))
            


    def test79(self):
        input_79 = "5 10 1 15 7"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "24648959770927 41165235424964 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "9 11 3 15 7"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "24648817341102 41165114064236 88046848035 13602161452932 99999999999999"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "24648817341102 41165114064236 88046848035 13602161452932 10000831349205"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "11 20 15 25 18"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "5 10 2 8 6"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "20341632 7813614630256 258789 27814633216 500000000"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "10 20 5 15 8"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = ['100 200 50 150 75', '']
        self.assertEqual(patched_source(*input_89), original_source(*input_89))
            


    def test90(self):
        input_90 = "6 10 4 8 3"
        self.assertEqual(patched_source(input_90), original_source(input_90))
            


if __name__ == '__main__':
    unittest.main()  
    
    