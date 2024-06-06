
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                


    def test0(self):
        input_0 = "{'node1': {'incoming_nodes': [], 'outgoing_nodes': ['node2']}, 'node2': {'incoming_nodes': ['node1'], 'outgoing_nodes': []}}"
        self.assertEqual(patched_source(input_0), original_source(input_0))
            


if __name__ == '__main__':
    unittest.main()  
    
    