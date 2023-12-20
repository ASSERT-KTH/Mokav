from test_generator import TestGenerator
import pandas as pd
import random
import subprocess
import ast


import time
from functools import wraps


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
    def __init__(self, problem_id, author_id):
        self.problem_id = problem_id
        self.author_id = author_id

    def prepare_data(self):
        df_submissions = pd.read_csv('data/2acc_copy/cb_submission_res_2acc_alt.csv')
        df_testcases = pd.read_csv('data/2acc_copy/cb_testcase_res_2acc.csv')

        df = df_submissions[(df_submissions['problems_id'] == self.problem_id) & (
            df_submissions['author'] == self.author_id)]['func_sourceCode']
        df_acc_other = df_submissions[(df_submissions['verdicts_id'] == 1) & (
            df_submissions['problems_id'] == self.problem_id) & (df_submissions['author'] != self.author_id)]['func_sourceCode']
        acc1 = df.values.tolist()[0]
        rej = df.values.tolist()[1]
        acc2 = df_acc_other.values.tolist()[0]

        df_testcases = df_testcases[df_testcases['problems_id']
                                    == self.problem_id]
        test_cases = df_testcases[['inputdata']].to_dict('records')

        return acc1, acc2, rej, test_cases[0]


    def create_unnitest(self, buggy_code, acc_code, test_cases):
        with open(f'temp_acc_qb.py', 'w') as f:
            f.write(acc_code)
        with open(f'temp_bug_qb.py', 'w') as f:
            f.write(buggy_code)
        
        unittest_str = f'''
import unittest
from temp_bug_qb import func as buggy_source
from temp_acc_qb import func as accepted_source

class TestFunctions(unittest.TestCase):
                
'''

        for i,test_case in enumerate(test_cases):
            input_data = test_case['inputdata']
            if '\n' in input_data:
                input_data = list(input_data.split('\n'))

            unittest_str = unittest_str + f'''

    def test{i}(self):
        input_{i} = "{input_data}"
        self.assertEqual(buggy_source(input_{i}), accepted_source(input_{i}))
            
'''

        unittest_str += '''

if __name__ == '__main__':
    unittest.main()  
    
    '''

        with open(f'temp_test_case.py', 'w') as f:
            f.write(unittest_str)       

    

    @retry_decorator(max_retries=3, delay=1)
    def run(self):
        print(f'###PROBLEM_ID###: {self.problem_id}')
        print(f'###AUTHOR###: {self.author_id}')
        config = 'BADT'
        test_generator = TestGenerator(config)
        df = pd.read_csv('data/2acc_copy/cb_submission_res_2acc_alt.csv')
        acc_code1, acc_code2, buggy_code, existing_test = self.prepare_data()

        fault_inducing_test = test_generator.generate_test3(
            buggy_code, acc_code1, existing_test, None)
        fault_inducing_test = [
            item for sublist in fault_inducing_test for item in sublist]
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
        self.create_unnitest(buggy_code, acc_code1, data_list)
        try:
            process = subprocess.run(['python', f'temp_test_case.py'], capture_output=True, timeout=5)
        except subprocess.TimeoutExpired:
            process = 'Timeout'
        output = str(process)
        if ('AssertionError' not in output) and ('temp_bug_qb.py' not in output):
            for i in range(10):
                self.create_unnitest(buggy_code, acc_code1, data_list)
                try:
                    process = subprocess.run(['python', f'temp_test_case.py'], capture_output=True, timeout=1)
                except subprocess.TimeoutExpired:
                    process = 'Timeout'
                output = str(process)
                if ('AssertionError' in output) or ('temp_bug_qb.py' in output):
                    print('Found1')
                    break
            print(str(process))
        else:
            print('Found1')
        



if __name__ == '__main__':
    
    df = pd.read_csv('data/2acc_copy/cb_submission_res_2acc_alt.csv')
    df = df[(df['failed_tests_ratio'] < 0.9)]
    grouped = df.groupby(['author', 'problems_id'])['diff_ratio'].mean().reset_index()
    grouped = grouped.sort_values('diff_ratio', ascending=False)
    top_10_percent = int(len(grouped) * 0.1)
    result = grouped.iloc[2 * top_10_percent: 3 * top_10_percent][['author', 'problems_id']].values.tolist()

    for i in result:
        code_runner = CodeRunner(i[1], i[0])
        code_runner.run()
