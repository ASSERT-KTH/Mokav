
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "test@domain.com/test@domain.com"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "test@example.com"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "user@domain.com"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "abc@def.com"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "valid_username@invalid_hostname"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "username@@hostname.com"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "a@domain.com"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "john.doe@example.com"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "example@example.com"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "user@domain.com"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "hello@world.com"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "user@domain.com"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "john.doe@test.com"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "test@user.com/"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "username@hostname.com"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "alice.@example.com/alice"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "johndoe@domain.com"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "abc@gmail.com"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "username@hostname.com"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "test@domain.com"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "email@example.com/////"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "john.doe@example.com"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "a@b.c.d/e"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "user@domain.com/////"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "example@domain.com"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "example@domain.com//"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "hello@world."
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "valid_username@host.com"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "john@doe.com"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "username@hostname"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "test@domain.com/testing"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "test@domain.com"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "example@example.com"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "user@domain.com/testing"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "john.doe@example.com"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "username@domain.com"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "test@gmail.com"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "email@example.com"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "a@b.com"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "user@domain.com"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "user@domain.com"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "john@domain.com"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "example@domain.com/different"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "test@domain.com"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "abc@def.com"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "testing@domain.com"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "1username@example.com/"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "john.doe@@example.com"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "abc@def.com/ghi"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "user@@example.com"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "test@domain.com"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "test@domain.com"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "username@domain.com"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "abc@@def.com"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "test@domain.com"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "user@domain"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "test@example.com/test"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "test@domain.com"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "user123@domain.com/asldk"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "username@hostname/"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "username@example.com//"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "example@example.com"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "a@b.com"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "aaaaaaa..........@@@@@"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "abc@test.com/xyz"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "test@domain.com"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "john.doe@example.com"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "test@test.com"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "test@test.com"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "johndoe@example.com////"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "my_email@domain.com"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "abc@def.gh/ijklmnopqrstuvwxyz123456"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "user@@example.com"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "email@domain.com"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "user@domain.com"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "tes@ting.com"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "username@website.com"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "john.doe@example.com/foo"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "john.doe@example.com"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "test@domain.com/test"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "myusername@mywebsite.com/myfolder"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "username@hostname/invalid"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "john_doe@gmail.com/test"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "john.doe@example.com"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "user@domain.com////"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "username@domain.com"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "username@domain.com"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "ab@cd.com"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "testing@domain.com/testing"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "@example.com"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


if __name__ == '__main__':
    unittest.main()  
    
    