
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = [{'zero': {'value': 0, 'outgoing_nodes': ['four'], 'incoming_nodes': []}, 'four': {'value': 4, 'outgoing_nodes': ['one'], 'incoming_nodes': ['zero']}, 'one': {'value': 1, 'outgoing_nodes': [], 'incoming_nodes': ['four']}}]
        self.assertEqual(patched_source(*input_0), original_source(*input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    