
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "6 w patch"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "5 x y"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "6 apples yep"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "5 w hello"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "30 apples"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "-42 hello world"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "6 is weekday"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "30 xyz"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "5 x y"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "5 w xyz"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "5 x 10"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "6 w test"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "5 q w"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "10 apples are in the basket"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "5 red apples"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "8 green apples"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "8 apples"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "5 x start"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "6 hello world"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "5 wd 3"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "5 zebra walk"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "6 apples"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "5 x squared wxyz"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "6 good morning"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "5 x w"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "6 dogs"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "5 x warmer"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "6 efg"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "6 winter is coming"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "7 data wxyz"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "5 w something"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "6 w test"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "6 testing input"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "6 echo World"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "6 8 world"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "30.1 xyz wind"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "5 <startswith>w test"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "30 m w"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "5 hello world"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "6 white cat"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "30 b testing"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "5 abd wxyz"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "5 w test"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "6 wind speed"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "7 w test"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "5 wxyz"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "5 x start"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "5 wxyz"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "6 asd www"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "30"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "5   abc def"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "6 apples from the tree"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "6 cwt"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "5 yawn abcdefg"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "6 w apple"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "5 warcraft"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "7 am Good morning!"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "30 v 5"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "5 windstorm"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "20 walk morning"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "6 v 9"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "10 ww"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "29 w test"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "30 w 0"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "6 hello world"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "5 w test"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "29 zebra"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "7 w some text"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "5 running wall"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "30 w test"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "6 apple word"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "6 apples on the table"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "6 x y"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "5 hello world"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


if __name__ == '__main__':
    unittest.main()  
    
    