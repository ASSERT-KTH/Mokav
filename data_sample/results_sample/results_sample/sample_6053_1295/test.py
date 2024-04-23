
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "2 4 5 10 8 100 3 1"
        self.assertEqual(list(buggy_source(input_0)), list(accepted_source(input_0)))
            


    def test1(self):
        input_1 = "1 1 1 0 0 0 1 1"
        self.assertEqual(list(buggy_source(input_1)), list(accepted_source(input_1)))
            


    def test2(self):
        input_2 = "2 4 5 10 2 100 2 1"
        self.assertEqual(list(buggy_source(input_2)), list(accepted_source(input_2)))
            


    def test3(self):
        input_3 = "2 2 2 2 2 2 2 2"
        self.assertEqual(list(buggy_source(input_3)), list(accepted_source(input_3)))
            


    def test4(self):
        input_4 = "2 2 2 10 10 10 2 2"
        self.assertEqual(list(buggy_source(input_4)), list(accepted_source(input_4)))
            


    def test5(self):
        input_5 = "3 3 5 10 5 100 3 1"
        self.assertEqual(list(buggy_source(input_5)), list(accepted_source(input_5)))
            


    def test6(self):
        input_6 = "3 4 5 3 2 10 3 1"
        self.assertEqual(list(buggy_source(input_6)), list(accepted_source(input_6)))
            


    def test7(self):
        input_7 = "2 3 5 6 7 8 3 1"
        self.assertEqual(list(buggy_source(input_7)), list(accepted_source(input_7)))
            


    def test8(self):
        input_8 = "5 2 3 4 6 50 2 5"
        self.assertEqual(list(buggy_source(input_8)), list(accepted_source(input_8)))
            


    def test9(self):
        input_9 = "1 1 1 1 1 1 1 1"
        self.assertEqual(list(buggy_source(input_9)), list(accepted_source(input_9)))
            


if __name__ == '__main__':
    unittest.main()  
    
    