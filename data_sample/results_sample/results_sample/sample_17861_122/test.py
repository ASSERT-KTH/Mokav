
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "['300 450 600 750 900\r\r', '10 20 30 40 50\r\r', '2 1']"
        self.assertEqual(list(buggy_source(input_0)), list(accepted_source(input_0)))
            


    def test1(self):
        input_1 = "['100 200 300 400 500\r\r', '1 2 3 4 5\r\r', '5 10']"
        self.assertEqual(list(buggy_source(input_1)), list(accepted_source(input_1)))
            


    def test2(self):
        input_2 = "['400 900 1400 1900 2400\r\r', '0 1 2 3 4\r\r', '1 0']"
        self.assertEqual(list(buggy_source(input_2)), list(accepted_source(input_2)))
            


    def test3(self):
        input_3 = "['10 9 10 11 12\r\r', '0 0 0 0 0\r\r', '0 0']"
        self.assertEqual(list(buggy_source(input_3)), list(accepted_source(input_3)))
            


    def test4(self):
        input_4 = "['15 30 45 60 75\r\r', '0 1 2 3 4\r\r', '1 0']"
        self.assertEqual(list(buggy_source(input_4)), list(accepted_source(input_4)))
            


    def test5(self):
        input_5 = "['50 100 150 200 250\r\r', '6 5 4 3 2\r\r', '0 1']"
        self.assertEqual(list(buggy_source(input_5)), list(accepted_source(input_5)))
            


    def test6(self):
        input_6 = "['200 300 400 500 600\r\r', '5 4 3 2 1\r\r', '5 0']"
        self.assertEqual(list(buggy_source(input_6)), list(accepted_source(input_6)))
            


    def test7(self):
        input_7 = "['10 20 30 40 50\r\r', '0 1 2 3 4\r\r', '1 0']"
        self.assertEqual(list(buggy_source(input_7)), list(accepted_source(input_7)))
            


    def test8(self):
        input_8 = "['250 200 150 100 50\r\r', '0 1 2 3 4\r\r', '1 0']"
        self.assertEqual(list(buggy_source(input_8)), list(accepted_source(input_8)))
            


    def test9(self):
        input_9 = "['20 80 40 60 100\r\r', '0 4 2 1 3\r\r', '1 0']"
        self.assertEqual(list(buggy_source(input_9)), list(accepted_source(input_9)))
            


if __name__ == '__main__':
    unittest.main()  
    
    