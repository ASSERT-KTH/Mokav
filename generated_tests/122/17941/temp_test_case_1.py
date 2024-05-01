
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['210 230 245 260 275\r\r', '2 4 6 8 10\r\r', '3 1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['125 200 175 150 225\r\r', '5 4 3 2 1\r\r', '3 2']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['200 150 275 210 180\r\r', '3 2 1 4 5\r\r', '2 3']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['200 300 400 500 600\r\r', '5 4 3 2 1\r\r', '3 2']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['200 180 220 190 210\r\r', '6 5 4 3 2\r\r', '3 1']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['200 250 300 350 400\r\r', '1 2 3 4 5\r\r', '2 1']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['200 150 100 50 25\r\r', '5 4 3 2 1\r\r', '1 2']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['200 150 2800 3300 1400\r\r', '7 5 10 6 8\r\r', '5 2']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['200 180 160 140 120\r\r', '5 4 3 2 1\r\r', '3 4']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['100 200 300 400 500\r\r', '5 4 3 2 1\r\r', '3 2']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    