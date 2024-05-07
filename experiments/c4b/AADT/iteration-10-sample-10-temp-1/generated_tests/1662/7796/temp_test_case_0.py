
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "abcdefghijklmnopqrstuvwxyz@abcdefghi.jklmnopqrstuvwxyz/qwerty"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "abcdefghijklmnop@subdomain.example.com/123456789012345678901234567890123"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "abcdefghijk@example.com/test"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "abcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "random@gmail.com/a"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "test@test.com/a"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "test@verylongdomainnamethatislongerthan32charactersandshouldtriggerNOoutput"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "abcdefghijklmnop@xyz.com"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "qwerty@abcdefgh.com"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "abcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "test@example.com/verylonghostnameverylonghostnameverylonghostname"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "abcdefghijklmnop@domain.com"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "abcdefghijk@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/xyz"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "abcdefghijk@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvw"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "abcde@abcde.abcde/abcde"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "abcdefghijklmnop@xyz.com"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee@e.com"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "abcdefghij123456@mydomain.com/test"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "test@verylonghostnameverylonghostnameverylonghostnameverylong"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyz.com"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "test@test.com/abcdefghijklmnopqrstuvwx"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "abcdefghijklmnopqrstuvwxyz@verylonghostnameverylonghostname.com/username"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "test@example.com"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "abcdefghijklmnop@abcdefghijklmnopabcdefghijklmnopabcdefghijklmnop.com"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "abcdefghijklm@nopqrstuvwxyzabcdefghijklmnopqrstu"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "abcdefghijklmnop@abcd.com"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyz.com"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "abcdefghij1234567890@xyz.com"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "abcdefghijklmnop@domain.com/test"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyz.com"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyza.com"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "test@test.com/test"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "abcdefghijklmnop@abcdefgh.abcdefgh.abcdefgh.abcdefgh/abcdefgh"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "abcdefghij@example.com/test"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "test@subdomain.example.com/test12345"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "abcdefghijklmnop@abcdefghijklmnoqrstuvwxyz.abcdefghijklmn"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.xyz/1234567890"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "abcdefghijklmnop@abcdefgh.ijklmnop/qrstuvwxyz"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "abcdefghijklmnop@abcdefgh.abcdefgh.abcdefgh.abcdefgh.abcdefgh"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "abcdefghijklm@n.opqrstuvwxyz/123456789012345678901234567890"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "qwerty@abcdefghijklmnopabcdefghijklmnopabcdefghijklmnopabcdefghijklmnop"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "abcdefghijk@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "abcdefghijklmnop@abcdefghijk.abcdefghijklmnopqrstuvwxyz/abcdefghijkl"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "abcdefghi@jklmnopqrstuvwxyzjklmnopqrstuvwxyzjklmnopqrstuvwxyzjklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww@example.com"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "abcdefghijklmnop@www.example.com/123456789012345678901234567890123"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "abcdefghijklmnopqrstuvwxy@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.zzz"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/a"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "abcdefghi@jklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "abcdefghijklmnop@abcdefghijklmno.xyz/abcdefghijklmno"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "email@example.com"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "abcdefghijklmnop@abcdefghijklmno.xyz/abcdefghijklmnop"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "abcdefghijklmnop@abcdefghijklmno.com"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "abcdefghijklmnop@abcdefghijklmno.pqrstuvwxyz/abcdefghijklmnop"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "abcdefghijklmnop@abcdefghijklmnoabcdefghijkl"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "abcdefghijklmnop@abcdef.ghijklmnopqrstuvwxyz/abcdefghij"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "test@test.com/12345678901234567890123456789012"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "test@test.com/test123"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "test@verylonghostnameverylonghostnameverylonghostname.com"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "hello@verylonghostnameverylonghostnameverylonghostnameverylonghostname.com"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz/abcd"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "abcdefghijklmnop@subdomain.domain.com/verylongsubdirectoryname"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "a@b.c"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "abcdefghijklmnop@abcdefghijklmnoabcdefghijklmnop"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "abcdefghijklmnop@examplerandomdomain.com"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "abcdefghijklmnop@examplerandomtext.com"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "abcdefghijklmnop@testing.testing/testing123"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "test@example.com/anexamplethatexceedsthelengthof32characters"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "abcdefghijklmnop@xyz123.com/abcdefghijklmno"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "abcdefghijklmnop@abcdefghijklmno.com"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "abcdefghijklmnop@abcdefgh.abcdefghabcdefghabcdefghabcdefghabcdefgh"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "abcdefghijklmnopqrstuvw@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "abcdefghijk@domain.com/123456789012345678901234567890123"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "abcdefghijklmnop@abcdefghijk.abcdefghijklmno/abcdefghijkl"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "abcdefghijklmnop@testing.com/test"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "abcdefghijklmnop@example.com"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "test@test@test.com"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.com"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "test@example.com"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "test@verylonghostnameverylonghostnameverylonghostnameverylonghostname.com"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@mail.com"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "abcdefghijklmnop@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "abcdefghijklmnop@sub.example.com/xyz"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "test@example.com/abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "abcdefghijklmnop@abcdefghijklmno.xyz/abcdefghijklmnop"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


if __name__ == '__main__':
    unittest.main()  
    
    