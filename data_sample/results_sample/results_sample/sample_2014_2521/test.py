
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "9999999"
        self.assertEqual(list(buggy_source(input_0)), list(accepted_source(input_0)))
            


    def test1(self):
        input_1 = "10001"
        self.assertEqual(list(buggy_source(input_1)), list(accepted_source(input_1)))
            


    def test2(self):
        input_2 = "12"
        self.assertEqual(list(buggy_source(input_2)), list(accepted_source(input_2)))
            


    def test3(self):
        input_3 = "1110"
        self.assertEqual(list(buggy_source(input_3)), list(accepted_source(input_3)))
            


    def test4(self):
        input_4 = "1100"
        self.assertEqual(list(buggy_source(input_4)), list(accepted_source(input_4)))
            


    def test5(self):
        input_5 = "10001001"
        self.assertEqual(list(buggy_source(input_5)), list(accepted_source(input_5)))
            


    def test6(self):
        input_6 = "11111"
        self.assertEqual(list(buggy_source(input_6)), list(accepted_source(input_6)))
            


    def test7(self):
        input_7 = "1000011"
        self.assertEqual(list(buggy_source(input_7)), list(accepted_source(input_7)))
            


    def test8(self):
        input_8 = "1000111"
        self.assertEqual(list(buggy_source(input_8)), list(accepted_source(input_8)))
            


    def test9(self):
        input_9 = "12"
        self.assertEqual(list(buggy_source(input_9)), list(accepted_source(input_9)))
            


if __name__ == '__main__':
    unittest.main()  
    
    