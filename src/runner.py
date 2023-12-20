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
        df_submissions = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
        df_testcases = pd.read_csv('data/2acc/cb_testcase_res_2acc.csv')

        df = df_submissions[(df_submissions['problems_id'] == self.problem_id) & (
            df_submissions['author'] == self.author_id)]['sourceCode']
        df_acc_other = df_submissions[(df_submissions['verdicts_id'] == 1) & (
            df_submissions['problems_id'] == self.problem_id) & (df_submissions['author'] != self.author_id)]['sourceCode']
        acc1 = df.values.tolist()[0]
        rej = df.values.tolist()[1]
        acc2 = df_acc_other.values.tolist()[0]

        df_testcases = df_testcases[df_testcases['problems_id']
                                    == self.problem_id]
        test_cases = df_testcases[['inputdata']].to_dict('records')

        return acc1, acc2, rej, test_cases[0]

    def judge_acc_buggy(self, buggy_code, acc_code1, acc_code2, test_cases):
        with open(f'temp_acc1.py', 'w') as f:
            f.write(acc_code1)
        with open(f'temp_acc2.py', 'w') as f:
            f.write(acc_code2)
        with open(f'temp_bug.py', 'w') as f:
            f.write(buggy_code)
        for test_case in test_cases:
            input_data = test_case['inputdata'].encode()
            process = subprocess.run(
                ['python', f'temp_acc1.py'], input=input_data, capture_output=True, timeout=20)
            output_acc1 = str(process.stdout.decode()).strip()
            print('output_acc1:', output_acc1)

            process = subprocess.run(
                ['python', f'temp_acc2.py'], input=input_data, capture_output=True, timeout=20)
            output_acc2 = str(process.stdout.decode()).strip()
            print('output_acc2: ', output_acc2)

            process = subprocess.run(
                ['python', f'temp_bug.py'], input=input_data, capture_output=True, timeout=20)
            output_bug = str(process.stdout.decode()).strip()
            print('output_bug: ', output_bug)
            result = output_acc1 == output_bug
            if not result:
                res, out = 'Found1', test_case

                if output_acc1 != output_acc2:
                    res, out = 'TestValidationException', (
                        output_acc1, output_acc2)
            else:
                res, out = 'InsufficientTestException', output_bug
        return res, out

    @retry_decorator(max_retries=3, delay=1)
    def run(self):
        print(f'###PROBLEM_ID###: {self.problem_id}')
        print(f'###AUTHOR###: {self.author_id}')
        config = 'BADT'
        test_generator = TestGenerator(config)
        df = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
        acc_code1, acc_code2, buggy_code, existing_test = self.prepare_data()

        fault_inducing_test = test_generator.generate_test3(
            buggy_code, acc_code1, existing_test, None)
        fault_inducing_test = [
            item for sublist in fault_inducing_test for item in sublist]
        print("###FAULTIND###\n\n", fault_inducing_test)
        data_list = []
        for fault_test in fault_inducing_test:
            data_list.append(ast.literal_eval(
                fault_test.replace('python', '')))
        print("###DATALIST###\n\n", data_list)

        res, out = self.judge_acc_buggy(
            buggy_code, acc_code1, acc_code2, data_list)

        if res == 'InsufficientTestException' or res == 'TestValidationException':
            for i in range(10):
                fault_inducing_test = test_generator.generate_test3(
                    buggy_code, acc_code1, existing_test, out)
                fault_inducing_test = [
                    item for sublist in fault_inducing_test for item in sublist]
                data_list = []
                for fault_test in fault_inducing_test:
                    data_list.append(ast.literal_eval(
                        fault_test.replace('python', '')))
                res, out = self.judge_acc_buggy(
                    buggy_code, acc_code1, acc_code2, data_list)
                if res != 'InsufficientTestException':
                    break
        print(res, out)


if __name__ == '__main__':
    
    # df = pd.read_csv('data/2acc/cb_submission_res_2acc_alt.csv')
    # df = df[(df['failed_tests_ratio'] < 0.9)]
    # grouped = df.groupby(['author', 'problems_id'])['diff_ratio'].mean().reset_index()
    # grouped = grouped.sort_values('diff_ratio', ascending=False)
    # top_10_percent = int(len(grouped) * 0.1)
    # result = grouped.iloc[5 * top_10_percent: 6 * top_10_percent][['author', 'problems_id']].values.tolist()

    # for i in result:
    #     code_runner = CodeRunner(i[1], i[0])
    #     code_runner.run()

    df = pd.read_csv('data/2acc_copy/cb_submission_res_2acc_alt.csv')
    code_runner = CodeRunner(df['problems_id'][5], df['author'][5])
    code_runner.run()
