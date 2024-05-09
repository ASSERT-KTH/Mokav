
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['251 400 600 750 1000\r\r', '30 20 50 10 40\r\r', '2 3']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['200 300 400 500 600\r\r', '10 20 30 40 50\r\r', '2 3']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['240 280 320 360 400\r\r', '0 1 2 3 4\r\r', '1 0']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['150 200 250 300 350\r\r', '0 1 2 3 4\r\r', '1 0']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['90 80 70 60 50\r', '1 2 3 4 5\r', '6 7']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['240 60 90 120 50\r\r', '55 72 80 62 43\r\r', '3 1']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['50 60 70 80 90\r\r', '10 20 30 40 50\r\r', '5 4']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['20 40 60 80 100\r\r', '0 1 2 3 4\r\r', '0 1']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['190 210 335 420 570\r\r', '0 1 2 3 4\r\r', '1 0']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['225 275 325 375 425\r\r', '10 20 30 40 50\r\r', '1 0']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    