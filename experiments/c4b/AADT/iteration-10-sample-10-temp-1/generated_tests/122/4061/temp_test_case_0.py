
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "250 500 750 1000 1250 2 3 4 5 6 150 200 250 300 350"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


    def test1(self):
        input_1 = "240 260 315 298 380 370 400 305 350 250 380 340 400 350 380 400 440 320 350 330 420 430 360 350 405 315 490 380 440 370 300 1000 1500 50"
        self.assertEqual(patched_source(input_1), original_source(input_1))
            


    def test2(self):
        input_2 = ['125 150 200 300 175', '20 15 25 30 18', '100 200']
        self.assertEqual(patched_source(*input_2), original_source(*input_2))
            


if __name__ == '__main__':
    unittest.main()  
    
    