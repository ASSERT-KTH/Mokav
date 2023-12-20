import json
import os
from test_generator import TestGenerator
import pandas as pd
import random
import subprocess
import ast
import time
from functools import wraps


def read_file(file_path):
    """Reads the contents of a file and returns it as a string."""
    with open(file_path, "r", encoding='utf-8') as file:
        contents = file.read()
    return contents


def retry_decorator(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retry_count = 0
            while retry_count < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Exception occurred: {e}")
                    retry_count += 1
                    print(
                        f"Retrying... (Attempt {retry_count} of {max_retries})")
                    time.sleep(delay)
            print(f"Max retries reached. Giving up.")
        return wrapper
    return decorator


class CodeRunner:


    def create_unnitest(self, buggy_code, acc_code, test_cases, function_name):
        with open(f'temp_acc_qb.py', 'w') as f:
            f.write(acc_code)
        with open(f'temp_bug_qb.py', 'w') as f:
            f.write(buggy_code)
        
        unittest_str = f'''
import unittest
from temp_bug_qb import {function_name} as buggy_source
from temp_acc_qb import {function_name} as accepted_source

class TestFunctions(unittest.TestCase):
                
'''

        for i,test_case in enumerate(test_cases):
            input_data = test_case['inputdata']
            if not isinstance(input_data, list):
                try:
                    input_data = list(input_data.split())
                except:
                    continue
            unittest_str = unittest_str + f'''

    def test{i}(self):
        input_{i} = {input_data}
        self.assertEqual(buggy_source(*input_{i}), accepted_source(*input_{i}))
            
'''

        unittest_str += '''

if __name__ == '__main__':
    unittest.main()  
    
    '''

        with open(f'temp_test_case.py', 'w') as f:
            f.write(unittest_str)       

    

    @retry_decorator(max_retries=3, delay=1)
    def run(self, acc_code, buggy_code, sample_test, function_name):
        config = 'BADT'
        test_generator = TestGenerator(config)
        fault_inducing_test = test_generator.generate_test3(
            buggy_code, acc_code, sample_test, None)
        print("###FAULTIND###\n\n", fault_inducing_test)
        data_list = []
        for fault_test in fault_inducing_test:
            if fault_test:
                try:
                    data_list.append(ast.literal_eval(fault_test.replace('python', '')))
                except Exception as e:
                    print(e)
                    continue
        print("###DATALIST###\n\n", data_list)
        self.create_unnitest(buggy_code, acc_code, data_list, function_name)
        try:
            process = subprocess.run(['python', f'temp_test_case.py'], capture_output=True, timeout=5)
        except subprocess.TimeoutExpired:
            process = 'Timeout'
        output = str(process)

        if 'AssertionError' not in output:
            for i in range(10):
                self.create_unnitest(buggy_code, acc_code, data_list, function_name)
                try:
                    process = subprocess.run(['python', f'temp_test_case.py'], capture_output=True, timeout=1)
                except subprocess.TimeoutExpired:
                    process = 'Timeout'
                output = str(process)
                if 'AssertionError' in output:
                    print('Found1')
                    break
            print(str(process))
        else:
            print('Found1')


if __name__ == '__main__':

    program_names = os.listdir('quixbugs/python_programs/')
    for program_name in program_names:
        try:
            code_runner = CodeRunner()
            buggy_code = read_file(f'quixbugs/python_programs/{program_name}')
            acc_code = read_file(f'quixbugs/correct_python_programs/{program_name}')
            with open("quixbugs/json_testcases/gcd.json", "r") as data_file:
                testdata = [json.loads(line) for line in data_file]
            testdata = testdata[0][0]
            if not isinstance(testdata, list):
                testdata = ' '.join(map(str, testdata))
            
            code_runner.run(acc_code=acc_code, buggy_code=buggy_code, sample_test= {'inputdata': testdata}, function_name =program_name[:-3])
        except Exception as e:
            print(e)
            continue
            

