
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "['B.......\r\r', '........\r\r', '.B....B.\r\r', '....W...\r\r', '........\r\r', '..W.....\r\r', '........\r\r', '........']"
        self.assertEqual(list(buggy_source(input_0)), list(accepted_source(input_0)))
            


    def test1(self):
        input_1 = "['........\r\r', '........\r\r', '.........\r\r', '.....W...\r\r', '........\r\r', '..B.....\r\r', '........\r\r', '........']"
        self.assertEqual(list(buggy_source(input_1)), list(accepted_source(input_1)))
            


    def test2(self):
        input_2 = "['........\r\r', '........\r\r', '.B....B.\r\r', '....W...\r\r', '........\r\r', '......W.\r\r', '........\r\r', '........']"
        self.assertEqual(list(buggy_source(input_2)), list(accepted_source(input_2)))
            


    def test3(self):
        input_3 = "['........\r\r', '........\r\r', '.B..B...\r\r', '....W...\r\r', '........\r\r', '..W.....\r\r', '........\r\r', '........']"
        self.assertEqual(list(buggy_source(input_3)), list(accepted_source(input_3)))
            


    def test4(self):
        input_4 = "['........\r\r', '........\r\r', 'B..B...B\r\r', '....W...\r\r', '........\r\r', '..W.....\r\r', '........\r\r', '........']"
        self.assertEqual(list(buggy_source(input_4)), list(accepted_source(input_4)))
            


    def test5(self):
        input_5 = "['BWBWBWBW\r\r', 'WBWBWBWB\r\r', 'BWBWBWBW\r\r', 'WBWBWBWB\r\r', 'BWBWBWBW\r\r', 'WBWBWBWB\r\r', 'BWBWBWBW\r\r', 'WBWBWBWB']"
        self.assertEqual(list(buggy_source(input_5)), list(accepted_source(input_5)))
            


    def test6(self):
        input_6 = "['WBWBWBWB\r\r', 'WBWBWBWB\r\r', 'WB.B.B.B\r\r', 'WB.WW..B\r\r', 'WWBBWBWB\r\r', 'WBWBBBWB\r\r', 'WBBBWWBB\r\r', 'WWWWWBWB']"
        self.assertEqual(list(buggy_source(input_6)), list(accepted_source(input_6)))
            


    def test7(self):
        input_7 = "['........\r\r', '........\r\r', '.B....B.\r\r', '....W...\r\r', '........\r\r', '...W....\r\r', '........\r\r', '........']"
        self.assertEqual(list(buggy_source(input_7)), list(accepted_source(input_7)))
            


    def test8(self):
        input_8 = "['........\r\r', '........\r\r', '.B....B.\r\r', '....W...\r\r', '........\r\r', '..W.....\r\r', '.......W\r\r', '........']"
        self.assertEqual(list(buggy_source(input_8)), list(accepted_source(input_8)))
            


    def test9(self):
        input_9 = "['....B...\r\r', '...W....\r\r', '........\r\r', '..B.....\r\r', '....W.W.\r\r', '........\r\r', '.....W..\r\r', '........']"
        self.assertEqual(list(buggy_source(input_9)), list(accepted_source(input_9)))
            


if __name__ == '__main__':
    unittest.main()  
    
    