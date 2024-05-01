
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['0 1 2 3 4\r', '5 6 7 8 9\r', '10 11 12 13 14\r', '15 16 17 18 19\r', '20 21 22 23 24']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    