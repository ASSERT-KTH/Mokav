
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "['23:59\r', '61']"
        self.assertEqual(list(buggy_source(input_0)), list(accepted_source(input_0)))
            


    def test1(self):
        input_1 = "['23:45\r\r', '15']"
        self.assertEqual(list(buggy_source(input_1)), list(accepted_source(input_1)))
            


    def test2(self):
        input_2 = "['01:15\r\r', '60']"
        self.assertEqual(list(buggy_source(input_2)), list(accepted_source(input_2)))
            


    def test3(self):
        input_3 = "['21:30\r\r', '90']"
        self.assertEqual(list(buggy_source(input_3)), list(accepted_source(input_3)))
            


    def test4(self):
        input_4 = "['23:59\r', '10 20']"
        self.assertEqual(list(buggy_source(input_4)), list(accepted_source(input_4)))
            


    def test5(self):
        input_5 = "['01:59\r\r', '60']"
        self.assertEqual(list(buggy_source(input_5)), list(accepted_source(input_5)))
            


    def test6(self):
        input_6 = "['23:59\r', '120']"
        self.assertEqual(list(buggy_source(input_6)), list(accepted_source(input_6)))
            


    def test7(self):
        input_7 = "['12:45\r\r', '60']"
        self.assertEqual(list(buggy_source(input_7)), list(accepted_source(input_7)))
            


    def test8(self):
        input_8 = "['12:30\r\r', '50']"
        self.assertEqual(list(buggy_source(input_8)), list(accepted_source(input_8)))
            


    def test9(self):
        input_9 = "['01:30\r\r', '90']"
        self.assertEqual(list(buggy_source(input_9)), list(accepted_source(input_9)))
            


if __name__ == '__main__':
    unittest.main()  
    
    