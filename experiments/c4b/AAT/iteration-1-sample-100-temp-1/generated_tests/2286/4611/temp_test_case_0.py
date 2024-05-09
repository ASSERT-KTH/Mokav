
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "apple pie"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "apple"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = "apple"
        self.assertEqual(patched_source(input_2), original_source(input_2))
            


    def test3(self):
        input_3 = "apple"
        self.assertEqual(patched_source(input_3), original_source(input_3))
            


    def test4(self):
        input_4 = "apple banana"
        self.assertEqual(patched_source(input_4), original_source(input_4))
            


    def test5(self):
        input_5 = "hello my friend"
        self.assertEqual(patched_source(input_5), original_source(input_5))
            


    def test6(self):
        input_6 = "apple"
        self.assertEqual(patched_source(input_6), original_source(input_6))
            


    def test7(self):
        input_7 = "apple!"
        self.assertEqual(patched_source(input_7), original_source(input_7))
            


    def test8(self):
        input_8 = "apple"
        self.assertEqual(patched_source(input_8), original_source(input_8))
            


    def test9(self):
        input_9 = "eat pizza"
        self.assertEqual(patched_source(input_9), original_source(input_9))
            


    def test10(self):
        input_10 = "hello"
        self.assertEqual(patched_source(input_10), original_source(input_10))
            


    def test11(self):
        input_11 = "apple"
        self.assertEqual(patched_source(input_11), original_source(input_11))
            


    def test12(self):
        input_12 = "hello"
        self.assertEqual(patched_source(input_12), original_source(input_12))
            


    def test13(self):
        input_13 = "apple?"
        self.assertEqual(patched_source(input_13), original_source(input_13))
            


    def test14(self):
        input_14 = "hello you"
        self.assertEqual(patched_source(input_14), original_source(input_14))
            


    def test15(self):
        input_15 = "hello Y"
        self.assertEqual(patched_source(input_15), original_source(input_15))
            


    def test16(self):
        input_16 = "eye an"
        self.assertEqual(patched_source(input_16), original_source(input_16))
            


    def test17(self):
        input_17 = "hello "
        self.assertEqual(patched_source(input_17), original_source(input_17))
            


    def test18(self):
        input_18 = "apple"
        self.assertEqual(patched_source(input_18), original_source(input_18))
            


    def test19(self):
        input_19 = "apple"
        self.assertEqual(patched_source(input_19), original_source(input_19))
            


    def test20(self):
        input_20 = "apple"
        self.assertEqual(patched_source(input_20), original_source(input_20))
            


    def test21(self):
        input_21 = "apple"
        self.assertEqual(patched_source(input_21), original_source(input_21))
            


    def test22(self):
        input_22 = "hello world"
        self.assertEqual(patched_source(input_22), original_source(input_22))
            


    def test23(self):
        input_23 = "hello?"
        self.assertEqual(patched_source(input_23), original_source(input_23))
            


    def test24(self):
        input_24 = "apple"
        self.assertEqual(patched_source(input_24), original_source(input_24))
            


    def test25(self):
        input_25 = "apple aaBcd?"
        self.assertEqual(patched_source(input_25), original_source(input_25))
            


    def test26(self):
        input_26 = "hello"
        self.assertEqual(patched_source(input_26), original_source(input_26))
            


    def test27(self):
        input_27 = "apple pear"
        self.assertEqual(patched_source(input_27), original_source(input_27))
            


    def test28(self):
        input_28 = "Hello apples"
        self.assertEqual(patched_source(input_28), original_source(input_28))
            


    def test29(self):
        input_29 = "apple"
        self.assertEqual(patched_source(input_29), original_source(input_29))
            


if __name__ == '__main__':
    unittest.main()  
    
    