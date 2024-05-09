
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "AAAABBBBCCCCDD"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "AAAAAA"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "AAAAAAA"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "AAAAA"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "AAABBB"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "111122233444"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "AAABBBAAAA"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "1111"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "AAAABBBCCC"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "11111"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "AAAAABBCCC"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "AAAABBBCD"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "AAAAAA"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "AAAAABBBB"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "AAAAABBBBB"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "AAABBB"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "11122333444555"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "aaabbbccc"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "AAAABBBBCCCC"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "AAABBBCCC"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "AAABBBBAAA"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "ABBBCC"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "aaaaaabbbbbb"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "101110011"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "aabbbccc"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "AAAABBBBCCCC"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "AAAAABBBBB"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "AAA"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "111111111111111111111111111111"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "AAAAABBBBB"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "AAAAABBCCCCCCCCDDD"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "AAAAABBBCCCCDDD"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "11111111"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "AAAAAA"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "AAAAABBBBB"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "AAAABBBCCCC"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "AAAAAAAABBBX"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "BBBBB"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "aaaaaab"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "AAAABBCCCCDDEEFFGG"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "111110"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "111111"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "110101"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "AAAAAA"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "AAAABBCCDD"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "AAAAABBBBB"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "AAAAAAA"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "AAABBBCCC"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "AABBBCCC"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "1111222233334444"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "AAABBBAA"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "aabbbcccd"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "111222"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "ABBCCCDDDDEE"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "AAABBBBCCC"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "aaaaaabbbbbb"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "aaabbcccc"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "AAABBBAA"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "AAAAA"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "AABBCC"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "aaaaaaaaaa"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "aaaabbbcccc"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "aaa"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "AAAAA"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "aaabbbaaa"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "11111"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "AAAA"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "AAABBAB"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "AAA"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


if __name__ == '__main__':
    unittest.main()  
    
    