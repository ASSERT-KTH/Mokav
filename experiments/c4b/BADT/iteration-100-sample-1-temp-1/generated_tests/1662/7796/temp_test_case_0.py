
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "abcdefghij@valid.hostname.with.no.slash"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ@abcdefghijklmnoptestabcdefghijklmnopqrstuv.xyz/valid"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "abcdefghij@validhostname.valid.com/validpath/validfile"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "a@b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "abc@abcdefghabcdefghabcdefghabcdefgh.com"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "abcde@abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd.abcd"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "abcdefghijklmnop@validhostname.abcdefghijklmnopqrstuvwxyz1234567890"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "abcdefghijklmnopqrstuv@abcdefghijklmno"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "abcdefghijklmnopqrstuvwx@abcdefghijklmnoqrstuvwxyz1234.com"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "abcdefghijklmnopqrst@abcdefghijklmno.xyzabcdefghijklmnopqrst@abcdefghijklmno.xyz"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "abcdefghijklmnopqrstuvw@examp123le.com"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "abcdefghijklmnopqrstuvwxy123456@abcdefghijklmno.com"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "abcdefghijklmnop@abcd.efghijklmnopqrstuv"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "a@b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z.a.b.c.d.e.f.g.h.i.j.k.l.m.n"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "abcdefghijklmnopqrstuvwxy@abcde.abcde.abcde.abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "abcdefghij123456@abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "abcdefghijklmnop@validhostname.valid"
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "abcdefghijklmnopqrstuvwx@yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy.zzzzzzzzzzzzzzzz"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "abcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "abcdefghijklmnop@subdomain1.subdomain2.subdomain3.subdomain4.subdomain5"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "abcdefghijklmnopqrstuvw@abcdefghijklmno.abcdefghijklmno.abcdefghijklmno.abcdefghijklmno"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmno.pqrstuvwxyzabcdefghijklmno"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "user123@example.com/abcdefghijklmnopqrstuvwx"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "abcd@abcdef.abcdefghijklmnopqrstuvwxyz.1234567890"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "abcdefghijklmnopqrstuvwxyz@abcdefghijklmno.com/1234567890"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "abcdefghijklmnopqrstuvwxy@abcd.efghijklmnopqrstuvwxy.abcd"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "AAAAA@valid.hostname.with.length.morethan32characters1234567890"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "aaaaaaaaaaaaaaaaaaaaaaaaaaa@bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.com"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "abcdefghijklmnopqrstuv@abcdefghijklmno.pqrstuvwxyza.bcdefghijklmnopq"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


    def test30(self):
        input_30 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_30), original_source(input_30))
            


    def test31(self):
        input_31 = "invalidemail@hostname1234567890.hostname1234567890.hostname1234567890.hostname1234567890"
        self.assertEqual(patched_source(input_31), original_source(input_31))
            


    def test32(self):
        input_32 = "abcdefghijklmnop@abcdefghijklmno.xyz"
        self.assertEqual(patched_source(input_32), original_source(input_32))
            


    def test33(self):
        input_33 = "abcdefghijklmnop@valid.domain.with.long.hostname.segment.1234567890"
        self.assertEqual(patched_source(input_33), original_source(input_33))
            


    def test34(self):
        input_34 = "abcdefghij1234567890@valid.hostname.with.more.than.32.characters.com/xyz"
        self.assertEqual(patched_source(input_34), original_source(input_34))
            


    def test35(self):
        input_35 = "abcdefghijklmn@valid.hostname.example"
        self.assertEqual(patched_source(input_35), original_source(input_35))
            


    def test36(self):
        input_36 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmno.pqrstuvwxyz.abcdefghijklmno.pqrstuvwxyz"
        self.assertEqual(patched_source(input_36), original_source(input_36))
            


    def test37(self):
        input_37 = "ABCDEFGHIJKLMNOP@abcdefghijklmnopqrstuvwxyz.1234567890"
        self.assertEqual(patched_source(input_37), original_source(input_37))
            


    def test38(self):
        input_38 = "abcdefghijklmnopqrstuvwx@abcdefgh.ijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_38), original_source(input_38))
            


    def test39(self):
        input_39 = "abcdefghijklmnop@abcdefgh.ijklmnopqrstuvwx/abcdefghijklmnopqrstuv"
        self.assertEqual(patched_source(input_39), original_source(input_39))
            


    def test40(self):
        input_40 = "abcdefghijklmnop@abcdefghijklmnoqrs.tuvwx.yz"
        self.assertEqual(patched_source(input_40), original_source(input_40))
            


    def test41(self):
        input_41 = "abcdefghijklmnopqrstuvwxy012345@abcdefghijklmno.com"
        self.assertEqual(patched_source(input_41), original_source(input_41))
            


    def test42(self):
        input_42 = "abcdefghij@example.com/12345678901234567"
        self.assertEqual(patched_source(input_42), original_source(input_42))
            


    def test43(self):
        input_43 = "abcdefghijklmnopqrstuv@xyzabcdefghijklmnopqrstuv.xyzabcdefghijklmnopqrstuv"
        self.assertEqual(patched_source(input_43), original_source(input_43))
            


    def test44(self):
        input_44 = "abcdefghijklmnopqrstuv@xyzabcdefghijklmnopqrstuv.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv"
        self.assertEqual(patched_source(input_44), original_source(input_44))
            


    def test45(self):
        input_45 = "abcdefghijklmnopqrstuvwx@abcdefghijklm.nopqrstuvwxyz"
        self.assertEqual(patched_source(input_45), original_source(input_45))
            


    def test46(self):
        input_46 = "abcdefghijklmnopqrstuv@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com"
        self.assertEqual(patched_source(input_46), original_source(input_46))
            


    def test47(self):
        input_47 = "abcdefghijklmnopqrst@uvwxyz1234567890.com"
        self.assertEqual(patched_source(input_47), original_source(input_47))
            


    def test48(self):
        input_48 = "abcdefghijklmno@abcde.1234567890.com/12345"
        self.assertEqual(patched_source(input_48), original_source(input_48))
            


    def test49(self):
        input_49 = "abcdefghijklmnopqrstuvwxyzaaaaa@valid.domain.with.lengthconstraints"
        self.assertEqual(patched_source(input_49), original_source(input_49))
            


    def test50(self):
        input_50 = "test@verylonghostnameverylonghostnamevery@verylonghostnameverylong"
        self.assertEqual(patched_source(input_50), original_source(input_50))
            


    def test51(self):
        input_51 = "abcdefghijklmnop@valid.com"
        self.assertEqual(patched_source(input_51), original_source(input_51))
            


    def test52(self):
        input_52 = "abcdefghijklmnop@abcdefghijklmno.abcdefghijklmno.abcdefghijklmno"
        self.assertEqual(patched_source(input_52), original_source(input_52))
            


    def test53(self):
        input_53 = "abcdefghijklmnopqrstuvw@exceeded.length.here.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_53), original_source(input_53))
            


    def test54(self):
        input_54 = "abcdefghijklmnopqrstuvw@abcdefgh.ijklmnopqrstuvwxyz.1234567"
        self.assertEqual(patched_source(input_54), original_source(input_54))
            


    def test55(self):
        input_55 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa@bbbbbbbbbbbbbbbbbbbbbb.com"
        self.assertEqual(patched_source(input_55), original_source(input_55))
            


    def test56(self):
        input_56 = "abcdefghijklmno@abcde.1234567890.1234567890.1234567890.12345"
        self.assertEqual(patched_source(input_56), original_source(input_56))
            


    def test57(self):
        input_57 = "abcdefghijklmnopqrstuvwx@abcdefghijklmnopqrstuvwx.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_57), original_source(input_57))
            


    def test58(self):
        input_58 = "abcdefghijklmnopqrstuvwx@abcdefghij.klmnopqrstuvwxyz.123456"
        self.assertEqual(patched_source(input_58), original_source(input_58))
            


    def test59(self):
        input_59 = "abcdefghijklmnopqrstuvwx@abcdefghijklmnoabcdefghijklmnoabcdefghi"
        self.assertEqual(patched_source(input_59), original_source(input_59))
            


    def test60(self):
        input_60 = "abcdefghijklmnopqrstuvwxy1@valid.host.name.here"
        self.assertEqual(patched_source(input_60), original_source(input_60))
            


    def test61(self):
        input_61 = "abcdefghijklmnop@abcdefghijklmno.com/a123456"
        self.assertEqual(patched_source(input_61), original_source(input_61))
            


    def test62(self):
        input_62 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyzabcdefghijklmnop"
        self.assertEqual(patched_source(input_62), original_source(input_62))
            


    def test63(self):
        input_63 = "abcdefghijklmnop@abcdefghijklmno.xyzabcdefghijklmno.xyzabcdefghijklmnop"
        self.assertEqual(patched_source(input_63), original_source(input_63))
            


    def test64(self):
        input_64 = "abcdefghijklmnopqrstuvwxy@zabcdefghijklmnopqrstuvwxy.zabcdefghijklmnopqrstuvwxy.zabcdefghijklmnopqrstuvwxy.z"
        self.assertEqual(patched_source(input_64), original_source(input_64))
            


    def test65(self):
        input_65 = "abcdefghijklmnopqrstuvwxyzaaa@valid.hostname.withexcesslengthsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        self.assertEqual(patched_source(input_65), original_source(input_65))
            


    def test66(self):
        input_66 = "abcdefghijklmnopqrstuvwxy@abcdefghijk.com/1234567890"
        self.assertEqual(patched_source(input_66), original_source(input_66))
            


    def test67(self):
        input_67 = "abcdefghijklmnop@abcdefghijklmnoooooooopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_67), original_source(input_67))
            


    def test68(self):
        input_68 = "abcdefghij123456@klmnopqrstuvwxyz1234567.com"
        self.assertEqual(patched_source(input_68), original_source(input_68))
            


    def test69(self):
        input_69 = "abcdefghijklmnop@abcdef.ghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_69), original_source(input_69))
            


    def test70(self):
        input_70 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_70), original_source(input_70))
            


    def test71(self):
        input_71 = "abcdefghijklmnopqrstuvwx@abcdefghijklmno.com/1234567890"
        self.assertEqual(patched_source(input_71), original_source(input_71))
            


    def test72(self):
        input_72 = "abcdefghijklmnopqrstuv@abcdefghijklmno.com/abcdefghijklmnopqrstuv"
        self.assertEqual(patched_source(input_72), original_source(input_72))
            


    def test73(self):
        input_73 = "abcdefghi1234567@valid.host.com"
        self.assertEqual(patched_source(input_73), original_source(input_73))
            


    def test74(self):
        input_74 = "abcdefghijklmnopqrstuvwxy@abcde.example.com/1234567890"
        self.assertEqual(patched_source(input_74), original_source(input_74))
            


    def test75(self):
        input_75 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@valid.hostname1234567890"
        self.assertEqual(patched_source(input_75), original_source(input_75))
            


    def test76(self):
        input_76 = "16char@validhostname.validhostname.validhostname.validhostname"
        self.assertEqual(patched_source(input_76), original_source(input_76))
            


    def test77(self):
        input_77 = "abcdefghijklmnopqrstuvwxyza@abcdefghijklmno.abcdefghijklmno"
        self.assertEqual(patched_source(input_77), original_source(input_77))
            


    def test78(self):
        input_78 = "abcdefghijklmnopqrstuvwxyyyyyyy@gmail.com"
        self.assertEqual(patched_source(input_78), original_source(input_78))
            


    def test79(self):
        input_79 = "abcdefghijklmnopqrstuvwxyz@abcdefgh.ijklmnopqrstuvwxyzqrstuvwxyz"
        self.assertEqual(patched_source(input_79), original_source(input_79))
            


    def test80(self):
        input_80 = "abcd1234@abcd1234567890abcdef.abcdef.abcdef"
        self.assertEqual(patched_source(input_80), original_source(input_80))
            


    def test81(self):
        input_81 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyz.com"
        self.assertEqual(patched_source(input_81), original_source(input_81))
            


    def test82(self):
        input_82 = "12345678901234567@valid.hostname1234567890.valid.hostname1234567890"
        self.assertEqual(patched_source(input_82), original_source(input_82))
            


    def test83(self):
        input_83 = "abcdefghijklmnopqrstuv@abcdefghijklmno.pqrstuvwxyzabcdefghijklmnopqrstuv"
        self.assertEqual(patched_source(input_83), original_source(input_83))
            


    def test84(self):
        input_84 = "abcdefghijklmnopqrstuvwxyz@example.com"
        self.assertEqual(patched_source(input_84), original_source(input_84))
            


    def test85(self):
        input_85 = "test@toolonghostname123456789012345678901234567890"
        self.assertEqual(patched_source(input_85), original_source(input_85))
            


    def test86(self):
        input_86 = "abcdefghijklmnopqrstuvw@abcdefghijklmno.com"
        self.assertEqual(patched_source(input_86), original_source(input_86))
            


    def test87(self):
        input_87 = "abcdefghijklmnopqrstuvwxy@abcdefghijklmnopqrstuvwxyz1234567.abcdefghijklmnopqrstuvwxyz1234567"
        self.assertEqual(patched_source(input_87), original_source(input_87))
            


    def test88(self):
        input_88 = "abcdefghijklmnopqrstuvw@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvw.abcdefghijklmnopqrstuvw.abcdefghijklmnopqrstuvw"
        self.assertEqual(patched_source(input_88), original_source(input_88))
            


    def test89(self):
        input_89 = "abcdefghij@klmnopqrstuvw.xyzabcdefg"
        self.assertEqual(patched_source(input_89), original_source(input_89))
            


if __name__ == '__main__':
    unittest.main()  
    
    