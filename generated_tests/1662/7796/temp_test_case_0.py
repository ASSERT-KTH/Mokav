
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "test@domain.com////"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "test@example.com./12345678901234567890123456789012"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "test@hostname.com/verylongpathwithmorethanthirtytwoccharacters"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "test@test.com/testtesttesttesttes"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr@abcdefghijklmnopqrst"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "abcdefghijklmnop@abcdefghijklmno.com/abcdefghijklmnop"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "abcdefghijklmnopqrstuvwxyz@abcdefghijklmnopqrstuvwxyz.abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz/abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "abcdefghijklmnop@abcde.abcde.abcde.abcde.abcde.abcde"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "abcd1234@abcdefgh123456.ijklmnopqrstuvwx/yz"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


if __name__ == '__main__':
    unittest.main()  
    
    