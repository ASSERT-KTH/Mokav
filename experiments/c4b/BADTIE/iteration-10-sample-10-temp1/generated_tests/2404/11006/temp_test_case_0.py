
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['BBBWWBWB\r', 'BBWBWWBW\r', 'BBBWWWBB\r', 'WWWWBBBW\r', 'WBWWWWBW\r', 'WBWWBBWB\r', 'WBWWWWWB\r', 'BWWWWBBW']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    