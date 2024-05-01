
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['12\r', '3 6 9 12 15 18 21 24 27 30 33 36']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['15\r', '3 6 9 12 15 18 21 24 27 30 33 36']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['12\r', '8 16 24 32 40 48 4 12 20 28 36 44 52']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['12\r', '10 20 30 40 50 60 70 80 90 100 110 120']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['2\r', '1 1 1 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['11\r', '5 10 15 20 25 30 35 40 45 50 55 60']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['12\r', '1 2 4 8 16 32 64 128 256 512 1024 2048']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['12\r', '11 10 9 8 7 6 5 4 3 2 1 0']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['12\r', '1 2 3 4 5 6 11 7 8 9 10 12']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['15\r', '1 1 1 1 1 1 1 1 1 1 1 1']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    