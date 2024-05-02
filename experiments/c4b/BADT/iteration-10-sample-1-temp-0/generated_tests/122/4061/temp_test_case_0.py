
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['200 400 600 800 1000\r\r', '0 1 2 3 4\r\r', '1 0']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    