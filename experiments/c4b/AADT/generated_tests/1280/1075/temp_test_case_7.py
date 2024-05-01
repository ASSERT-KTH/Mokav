
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['35\r', '1 1 1 1 2 2 2 2 1 1 1 1 2 2 2 2 1 1 1 1 2 2 2 2 1 1 1 1 2 2 2 2 1 1 1 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['35\r', '5 5 6 6 7 7 4 4 3 3 2 2 1 1 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 17 17 18 18']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['35\r', '8 8 7 9 9 6 6 5 5 10 10 11 11 4 4 3 3 1 1 7 7 8 8 9 9 2 2 5 5 6 6 3 3 4']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['35\r', '5 2 4 3 1 6 7 9 8 11 12 10 15 13 14 16 18 17 20 19 28 24 21 22 26 23 25 27 29 31 30 32 33 34']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['35\r', '12 12 11 11 10 10 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 13 13 14 14 15 15 16 16 17 17 18']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['35\r', '5 4 7 8 2 2 3 3 1 1 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 6 6 17 17 18 18 19 19 20 20']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['35\r', '2 2 4 4 6 6 8 8 10 10 12 12 14 14 16 16 18 18 20 20 22 22 24 24 26 26 1 1 3 3 5 5 7 7 9 9']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['16\r', '5 5 4 4 3 3 2 2 1 1 9 9 8 8 7 7 6 6 14 14 12 10 12 10 11 13 11 13 15 15 16']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['35\r', '6 6 5 5 4 4 3 3 2 2 1 1 7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 17 18 19 20']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['35\r', '7 7 8 8 9 9 10 10 11 11 12 12 13 13 14 14 15 15 16 16 1 1 2 2 3 3 4 4 5 5 6 6 17']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    