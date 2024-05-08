
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "420846563 675119959 341032066 213470986"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = ['4 1 2 3', '']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = "1 2 3 4"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = ['489101009 378201975 258901004 2091998', '']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = "552448597 864606626 360673166 57796992"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "3 3 4 2"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = ['816 342 563 276', '']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['34598776 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = ['100 5 10 15', '']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = "30 10 20 5"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = ['3756499 210 987 1001', '']
        self.assertEqual(patched_source(*input_11), original_source(*input_11))
            


    def test12(self):
        input_12 = "1 2 3 4"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = ['539624191 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_13), original_source(*input_13))
            


    def test14(self):
        input_14 = ['305124830 894270190 514300407 2691939', '']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = "2 1 1 1"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "4 1 2 3"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "8 3 5 10"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "4 1 2 3"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "624191 1497 4027 1939"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = ['459533529 336652772 582731167 772318121', '']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = "4 1 2 3"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "839916162 628373995 771529501 848481923"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "312711458 995821119 563537757 874642369"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "1 1 1 1"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "478593842 382910297 932828384 1538493"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "4 4 3 2"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "650912816 123456789 987654321 555555555"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = ['4 1 2 3', '']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = "886573161 991864679 216542449 8385797"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "529624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "362 41 74 93"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "389191649 640722874 340200723 107657010"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = ['503642380 719767455 483249639 2464575', '']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = ['722249203 199232309 314906591 87703380', '']
        self.assertEqual(patched_source(*input_35), original_source(*input_35))
            


    def test36(self):
        input_36 = ['710825953 625874239 984943159 917759277', '']
        self.assertEqual(patched_source(*input_36), original_source(*input_36))
            


    def test37(self):
        input_37 = ['778612349 1047857167 660623395 1508275', '']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = ['562947825 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = ['78560854 435698732 217849366 2463021890', '']
        self.assertEqual(patched_source(*input_40), original_source(*input_40))
            


    def test41(self):
        input_41 = "480283443 738091270 368332888 142624781"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "448105731 421343123 22904923 107385550"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = ['928867853 851802047 619439977 2854709', '']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = ['4 1 2 3', '']
        self.assertEqual(patched_source(*input_44), original_source(*input_44))
            


    def test45(self):
        input_45 = "4 4 4 4"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "1 2 3 4"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "1 2 3 4"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = ['823749202 621908374 543019473 1254903', '']
        self.assertEqual(patched_source(*input_48), original_source(*input_48))
            


    def test49(self):
        input_49 = ['86 75 23 92', '']
        self.assertEqual(patched_source(*input_49), original_source(*input_49))
            


    def test50(self):
        input_50 = ['3 6 9 12', '']
        self.assertEqual(patched_source(*input_50), original_source(*input_50))
            


    def test51(self):
        input_51 = ['230420012 192830291 281930301 8483847', '']
        self.assertEqual(patched_source(*input_51), original_source(*input_51))
            


    def test52(self):
        input_52 = "12 34 56 78"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "411 233 377 144"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = ['346971393 497748446 328500758 1711904', '']
        self.assertEqual(patched_source(*input_54), original_source(*input_54))
            


    def test55(self):
        input_55 = "1000000000 500000000 200000000 100000000"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "4 2 3 5"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = ['539624191 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_57), original_source(*input_57))
            


    def test58(self):
        input_58 = ['1024 512 256 128', '']
        self.assertEqual(patched_source(*input_58), original_source(*input_58))
            


    def test59(self):
        input_59 = ['799 111 222 333', '']
        self.assertEqual(patched_source(*input_59), original_source(*input_59))
            


    def test60(self):
        input_60 = "72100541 148979715 948432499 967433179"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "1 3 5 7"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = ['305684977 392010617 204880135 2754971', '']
        self.assertEqual(patched_source(*input_62), original_source(*input_62))
            


    def test63(self):
        input_63 = ['2 5 8 3', '']
        self.assertEqual(patched_source(*input_63), original_source(*input_63))
            


    def test64(self):
        input_64 = ['592330249 714088215 516441346 388111307', '']
        self.assertEqual(patched_source(*input_64), original_source(*input_64))
            


    def test65(self):
        input_65 = ['564668657 192366395 763092746 959856453', '']
        self.assertEqual(patched_source(*input_65), original_source(*input_65))
            


    def test66(self):
        input_66 = "478891347 264288560 103881471 399913801"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = ['100 200 300 400', '']
        self.assertEqual(patched_source(*input_67), original_source(*input_67))
            


    def test68(self):
        input_68 = "363483 244848 735928 864955"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = ['539624191 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_69), original_source(*input_69))
            


    def test70(self):
        input_70 = "4 1 2 3"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = ['204908711 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_71), original_source(*input_71))
            


    def test72(self):
        input_72 = ['419307866 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_72), original_source(*input_72))
            


    def test73(self):
        input_73 = "4 1 2 3"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = ['4 1 1 1', '']
        self.assertEqual(patched_source(*input_74), original_source(*input_74))
            


    def test75(self):
        input_75 = "99105457 358341103 424764883 85750573"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = ['1 1 1 1', '']
        self.assertEqual(patched_source(*input_76), original_source(*input_76))
            


    def test77(self):
        input_77 = ['4 1 1 1', '']
        self.assertEqual(patched_source(*input_77), original_source(*input_77))
            


    def test78(self):
        input_78 = ['1 1 1 1', '']
        self.assertEqual(patched_source(*input_78), original_source(*input_78))
            


    def test79(self):
        input_79 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "1 2 3 4"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = ['988679350 123456789 987654321 987654320', '']
        self.assertEqual(patched_source(*input_81), original_source(*input_81))
            


    def test82(self):
        input_82 = "4 1 2 3"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = ['747989129 354745674 422935506 98721636', '']
        self.assertEqual(patched_source(*input_84), original_source(*input_84))
            


    def test85(self):
        input_85 = ['4166 2985 4378 8296', '']
        self.assertEqual(patched_source(*input_85), original_source(*input_85))
            


    def test86(self):
        input_86 = "372950119 418768573 6927125 992802747"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "3 1 2 3"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


    def test90(self):
        input_90 = "2 1 2 3"
        self.assertEqual(patched_source(input_90), original_source(input_90))
            


    def test91(self):
        input_91 = "455 367 178 993"
        self.assertEqual(patched_source(input_91), original_source(input_91))
            


    def test92(self):
        input_92 = "669273688 922333496 74510011 914523365"
        self.assertEqual(patched_source(input_92), original_source(input_92))
            


    def test93(self):
        input_93 = "334710597 789235989 156289364 62340926"
        self.assertEqual(patched_source(input_93), original_source(input_93))
            


    def test94(self):
        input_94 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_94), original_source(input_94))
            


if __name__ == '__main__':
    unittest.main()  
    
    