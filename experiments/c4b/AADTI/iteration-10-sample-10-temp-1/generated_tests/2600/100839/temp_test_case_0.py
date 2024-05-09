
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['10\r\r', '2000 1995 1990']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['2\r\r', '2012 2013']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


    def test2(self):
        input_2 = ['2\r\r', '2010 2021']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


    def test3(self):
        input_3 = ['2\r\r', '2010 2012 2014']
        self.assertEqual(patched_source(*input_3), original_source(*input_3))
            


    def test4(self):
        input_4 = ['4\r\r', '2010 2012 2013 2014']
        self.assertEqual(patched_source(*input_4), original_source(*input_4))
            


    def test5(self):
        input_5 = ['2\r\r', '2017 2018']
        self.assertEqual(patched_source(*input_5), original_source(*input_5))
            


    def test6(self):
        input_6 = ['2\r\r', '2010 2020']
        self.assertEqual(patched_source(*input_6), original_source(*input_6))
            


    def test7(self):
        input_7 = ['4\r\r', '2000 2004 2008']
        self.assertEqual(patched_source(*input_7), original_source(*input_7))
            


    def test8(self):
        input_8 = ['5\r', '2001 2002 2003 2004 2005']
        self.assertEqual(patched_source(*input_8), original_source(*input_8))
            


    def test9(self):
        input_9 = ['2\r\r', '2010 2020']
        self.assertEqual(patched_source(*input_9), original_source(*input_9))
            


if __name__ == '__main__':
    unittest.main()  
    
    