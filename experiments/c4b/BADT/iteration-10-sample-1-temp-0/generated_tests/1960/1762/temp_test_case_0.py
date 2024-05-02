
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['1 2 3 4 5\r', '6 7 8 9 10\r', '11 12 13 14 15\r', '16 17 18 19 20\r', '21 22 23 24 25']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    