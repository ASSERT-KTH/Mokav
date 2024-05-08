
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = ['10 20 30 40 50', '5 10 15 20 25', '6 7']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


    def test1(self):
        input_1 = ['130 100 120 120 120', '40 50 30 20 10', '200 300']
        self.assertEqual(patched_source(*input_1), original_source(*input_1))
            


if __name__ == '__main__':
    unittest.main()  
    
    