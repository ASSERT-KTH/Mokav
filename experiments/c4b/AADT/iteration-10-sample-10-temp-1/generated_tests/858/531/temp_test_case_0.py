
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['515 20 30 40', '']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = "890719 265815 920448 373896"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = ['22345 67890 12345 98765', '']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['712345890 456789012 123456789 987654321', '']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "1 2 3 4"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "487 762 891 123"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "96821231 870381970 239119571 147930191"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "474372431 611048912 330994101 1595023"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = ['539624191 782710197 514300407 2691939', ' ']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


    def test10(self):
        input_10 = "545253605 807211730 533582394 2930492"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "823184685 456001443 27414423 897743523"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = ['943818272 1047781586 833615325 1902907', '']
        self.assertEqual(patched_source(*input_12), original_source(*input_12))
            


    def test13(self):
        input_13 = "17179869184 67108864 268435456 134217728"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = ['120945198 288107937 734526808 501872238', '']
        self.assertEqual(patched_source(*input_14), original_source(*input_14))
            


    def test15(self):
        input_15 = "38 71 11 94"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "342 75 89 102"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = ['4 1 1 1', '']
        self.assertEqual(patched_source(*input_17), original_source(*input_17))
            


    def test18(self):
        input_18 = "237736884 158754986 181080620 2837676"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = ['77123307 406027557 916120960 891143138', '']
        self.assertEqual(patched_source(*input_19), original_source(*input_19))
            


    def test20(self):
        input_20 = ['36 24 15 9', '']
        self.assertEqual(patched_source(*input_20), original_source(*input_20))
            


    def test21(self):
        input_21 = ['972583400 493876498 378264925 719462482', '']
        self.assertEqual(patched_source(*input_21), original_source(*input_21))
            


    def test22(self):
        input_22 = ['45196242 88751139 332511180 126284541', '']
        self.assertEqual(patched_source(*input_22), original_source(*input_22))
            


    def test23(self):
        input_23 = "1073741824 915971937 932269645 711444842"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = ['539624191 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_24), original_source(*input_24))
            


    def test25(self):
        input_25 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = ['453295206 671823662 382916328 815761609', '']
        self.assertEqual(patched_source(*input_26), original_source(*input_26))
            


    def test27(self):
        input_27 = "1 2 3 4"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = ['25 7 11 3', '']
        self.assertEqual(patched_source(*input_28), original_source(*input_28))
            


    def test29(self):
        input_29 = ['776517210 444814836 399132326 1083837', '']
        self.assertEqual(patched_source(*input_29), original_source(*input_29))
            


    def test30(self):
        input_30 = ['672158963 214345210 351080887 819746394', '']
        self.assertEqual(patched_source(*input_30), original_source(*input_30))
            


    def test31(self):
        input_31 = "460775600 897823500 458701200 203160301"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "77 0 3 6"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "346611 865993881 665350328 2792720"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = ['687336069 688065681 720948315 268464500', '']
        self.assertEqual(patched_source(*input_34), original_source(*input_34))
            


    def test35(self):
        input_35 = "4 1 1 1"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "175782685 985346786 327493865 9678124"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = ['480525589 120419309 449554436 1301371', '']
        self.assertEqual(patched_source(*input_37), original_source(*input_37))
            


    def test38(self):
        input_38 = "7 1 1 1"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = ['359851932 57438291 890522478 123456789', '']
        self.assertEqual(patched_source(*input_39), original_source(*input_39))
            


    def test40(self):
        input_40 = "4 5 6 7"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = ['163849721 792640248 328189283 8402614', '']
        self.assertEqual(patched_source(*input_41), original_source(*input_41))
            


    def test42(self):
        input_42 = ['486749771 557192323 337194534 86489271', '']
        self.assertEqual(patched_source(*input_42), original_source(*input_42))
            


    def test43(self):
        input_43 = ['825917269 273390678 479179131 881792776', '']
        self.assertEqual(patched_source(*input_43), original_source(*input_43))
            


    def test44(self):
        input_44 = "4 1 1 1"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = ['125793062 351572812 730561333 938823601', '']
        self.assertEqual(patched_source(*input_45), original_source(*input_45))
            


    def test46(self):
        input_46 = ['1 1 1 1', '']
        self.assertEqual(patched_source(*input_46), original_source(*input_46))
            


    def test47(self):
        input_47 = "30 5 10 15"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "4 1 2 3"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "332041914 961886095 785676132 149838"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "18 5 2 3"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "81738972 9456776 581644699 749972"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "793624191 782710197 524300407 2691939"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "3 4 5 6"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "10 5 3 2"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "600000000 1000000000 800000000 200000000"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "4 1 2 3"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = ['527624192 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_57), original_source(*input_57))
            


    def test58(self):
        input_58 = ['4 1 2 3', '']
        self.assertEqual(patched_source(*input_58), original_source(*input_58))
            


    def test59(self):
        input_59 = "4 1 1 1"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "0 2 1 3"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "539624191 782710197 514300407 2691939"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = ['449675123 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_62), original_source(*input_62))
            


    def test63(self):
        input_63 = "1 2 3 4"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = ['477372927 919248202 732790384 1276181', '']
        self.assertEqual(patched_source(*input_64), original_source(*input_64))
            


    def test65(self):
        input_65 = "2 3 5 7"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = ['614111582 812490919 497319762 391288847', '']
        self.assertEqual(patched_source(*input_66), original_source(*input_66))
            


    def test67(self):
        input_67 = "538 300 200 100"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = ['575023666 288938648 193717840 946884815', '']
        self.assertEqual(patched_source(*input_68), original_source(*input_68))
            


    def test69(self):
        input_69 = "100 50 25 75"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "474940880 202102717 381399742 8389393"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = ['754115152 258487552 573197844 416315724', '']
        self.assertEqual(patched_source(*input_71), original_source(*input_71))
            


    def test72(self):
        input_72 = "10 2 3 4"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = ['562772417 379962973 213318960 1943941', '']
        self.assertEqual(patched_source(*input_73), original_source(*input_73))
            


    def test74(self):
        input_74 = "4 1 1 1"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "6896542 4254736 572134 986512"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "4 2 3 1"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "876355390 1072349737 982637011 4213762"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "539624191 782710197 514300407 2"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = ['725456982 123456789 987654321 876543210', '']
        self.assertEqual(patched_source(*input_79), original_source(*input_79))
            


    def test80(self):
        input_80 = "4 1 2 3"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = ['539624191 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_81), original_source(*input_81))
            


    def test82(self):
        input_82 = ['539624191 782710197 514300407 2691939', '']
        self.assertEqual(patched_source(*input_82), original_source(*input_82))
            


if __name__ == '__main__':
    unittest.main()  
    
    