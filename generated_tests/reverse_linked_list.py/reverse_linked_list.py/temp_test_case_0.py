
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = [{'node1': {'value': '1', 'successor': 'node2'}, 'node2': {'value': '2', 'successor': 'node3'}, 'node3': {'value': '3', 'successor': 'node4'}, 'node4': {'value': '4', 'successor': 'node5'}, 'node5': {'value': '5', 'successor': None}}, 'node1']
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    