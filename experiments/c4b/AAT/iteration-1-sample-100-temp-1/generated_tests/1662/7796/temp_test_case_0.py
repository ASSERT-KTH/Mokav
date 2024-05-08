
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "abcdefghijklmnop@test.com/abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "abcdefghijklmnop@abc.abcdefg.abcdefgh/abc"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "abcdefghijklmnop@abcdefghijklmno.pqrstuvwxyz"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "ABCDEFGHIJKLMNOP@abcdefghijklmnopqrstuvwxyz.123456/7890"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "email@example.com"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "abcdefghijklmnopqrstuvwxyz@abcde.abcde.abcde.abcdeabcdeabcde"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde/abcde"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "abcdefghijklmnop@xyz.com"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuv/xyz"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "ThisIsAVeryLongEmailAddressWhichExceedsTheMaxLengthAllowedByThePatchedVersion@domain.com"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuv/abcd"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "abcdefghijklmnop@abcdefgh.ijklmnopqrs.tuv"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "abcdefghijklmnopqrstuvwxyz@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "abcdefghijklmnop@abcdefghijk.abcdefghijk.abcdefghijk.abcdefghijk.abcdefghijk/abcdefghijkl"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "abcdefghijklmnop@abcdefghijklmnop.abcdefghijklmnopabcdefghijklmnop"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "testing123@verylonghostnameverylonghostnameverylonghostname.com/validpath"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "invalid-email@toolonghostname1234567890123456.com"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvw"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "abcdefghijklmnop@ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "test@test.......com"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "abcdefghijklmnop@abcdefghijklmno.com"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvwxyz/abcdefgh"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/abcdefghijklmnop"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "abcdefghijklmnop@abcdefgh.abcdefgh.abcdefgh.abcdefgh.abcdefgh"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "abcde@123456789012345678901234567890123"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "abcdefghijklmnop@examplerestapi.com/test"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "abcdefghijklmnop@example.com/xyz123"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "abcdefghijklmnop@example.com/abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "abcdefghijklmnop@abcd.efghijklmnopqrstuv"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "abcdefghijklmnop@testing.testing.testing.testing/testing"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "aaaaaaaaaaaaaaaaaaa@bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "abcdefghijklmnop@abcdefghijklmno"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "123456789012345678901234567890123@example.com"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "abcdefghijklmnop@example.com"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "email@example.com"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "abcdefghijklmnop@abcdefghijabcdefghijabcdefghijabcdefghij"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyz.abcdefghijklmnoqrstuvwxyz/abcdefghijklmno"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyz.com"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "abcdefghijklmnop@abcdefgh.abcdefgh.abcdefgh/abcdefgh"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "abcdefghijklmnop@abcde.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "test@toolonghostnameeeeeeeeeeeeeeeeeeeee.com"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "abcdefghijklmnop@123456789012345678901234567890123"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "abcdefgh@example.com/test"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "test@verylonghostnameverylonghostnameverylonghostnameverylonghostname"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "abcdefghij@example.com/12345678901234567890123456789012"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "abcdefghijklmnop@exceededhostnamecharacterlimitssssssssssssssssssss"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "abcdefghijklmnop@abcdefghijklmno"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "abcdefghij@klmnopqrstuvwxyz1234567890.com"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "abcdefghijklmnop@uvwxyz.com"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "test@example.com/verylongsubdomainverylongsubdomain"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "quuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuux@verylonghostnameverylonghostnameverylongh"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "abcdefghijklmnop@abcdefghijk.abcdefghijkl.abcdefghijkl"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "abcdefghijk@lmnop.qrstuvwxyz/1234567890"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "abcdefghijklmnop@abcdefghiklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "abcdefghijklmnop@abc.abcdefgh.abcdefgh/abcdefgh"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "test@test.test/test"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "abcdefghijklmnop@abcdefghijklmno.pqrstuvwxyz/abcdefghijklmno"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "username@invalidhostname12345678901234567890123456789012345.com"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "abcdefghijklmno@abcdefghijklmno.abcdefghijklmno.abcdefghijklmno"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "abcdefghijklmnop@abcdefghijklmno.pqrstuvwxyz/abcdefghijklmno"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/xyz"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "qwerty@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/qwerty"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "abcdefghijklmnopqrstuvw@xyz.com/12345678901234567"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "abcdefghijklmnopqrstuvwxyz@www.example.com"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "12345678901234567@abcdefghiabcdefghiabcdefghiabcdefghi"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyzabcdefghijklmnop"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "ulll9@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,test"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@example.com"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "abcdefghijklmno@pqrstuvwxyz.abcdefghijklmno/test"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "abcdefghijklmnop@abcdefghijklmno.pqrstuvwxyz/abcdefghijkl"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "abcdefghijklmnop@abcdef.ghijklmnopqrstuv/abcdefgh"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "abcdefghijklmnop@abcdefgh.ijklmnop/qrstuvwxyz"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "abcdefghijklmnop@abcdefghijk.abc/abcdefghijk"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "test@verylonghostnameverylonghostnameverylonghostnameverylong"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "abcdefghijklmnop@subdomain.example.com"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "test@example.com/12345678901234567890123456789012"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "abcdefghijklmnop@defghijklmnopqrstuvwxyzabcdefghijklmnop.abcdefghijklmnop"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


    def test90(self):
        input_90 = "abcdefghijklmnop@abcdefghijklmnopabcdefghijklmnopabcdefghijklmnop.com"
        self.assertEqual(patched_source(input_90), original_source(input_90))
            


    def test91(self):
        input_91 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_91), original_source(input_91))
            


    def test92(self):
        input_92 = "username@example.com/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(patched_source(input_92), original_source(input_92))
            


    def test93(self):
        input_93 = "abcdefghijklmnop@xyz.com/123456789012345678901234567890123"
        self.assertEqual(patched_source(input_93), original_source(input_93))
            


    def test94(self):
        input_94 = "abcdefghijklmnop@abcdefghijklmno.xyzabcdefghijklmnop"
        self.assertEqual(patched_source(input_94), original_source(input_94))
            


if __name__ == '__main__':
    unittest.main()  
    
    