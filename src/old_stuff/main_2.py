from test_generator import TestGenerator
import pandas as pd
import random
import subprocess
import ast

class TestValidationException(Exception):

    def __str__(self):
        return repr('Validation Failed!')

class InsufficientTestException(Exception):
    
        def __str__(self):
            return repr('Insufficient Test!')

class CodeRunner:
    def __init__(self, problem_id, author_id):
        self.problem_id = problem_id
        self.author_id = author_id

    # def prepare_data(self):
    #     df_submissions = pd.read_csv('data/3_cb/cb_submission_res3.csv')
    #     df_testcases = pd.read_csv('data/3_cb/cb_testcases_res3.csv')

    #     df = df_submissions[(df_submissions['problems_id'] == self.problem_id) & (df_submissions['author'] == self.author_id)]['sourceCode']
    #     acc = df.values.tolist()[0]
    #     rej = df.values.tolist()[1]

    #     df_testcases = df_testcases[df_testcases['problems_id'] == self.problem_id]
    #     test_cases = df_testcases[['expectedresult', 'inputdata']].to_dict('records')

    #     return acc, rej, test_cases

    def prepare_data(self):
        df_submissions = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
        df_testcases = pd.read_csv('data/2acc/cb_testcase_res_2acc.csv')

        df = df_submissions[(df_submissions['problems_id'] == self.problem_id) & (df_submissions['author'] == self.author_id)]['sourceCode']
        df_acc_other = df_submissions[(df_submissions['verdicts_id'] == 1) & (df_submissions['problems_id'] == self.problem_id) & (df_submissions['author'] != self.author_id)]['sourceCode']
        acc1 = df.values.tolist()[0]
        rej = df.values.tolist()[1]
        acc2 = df_acc_other.values.tolist()[0]
        

        df_testcases = df_testcases[df_testcases['problems_id'] == self.problem_id]
        test_cases = df_testcases[['expectedresult', 'inputdata']].to_dict('records')

        return acc1, acc2, rej, test_cases

    # def judge(self, source_code, test_cases, name):
    #     with open(f'temp_{name}.py', 'w') as f:
    #         f.write(source_code)

    #     results = []
    #     for test_case in test_cases:
    #         input_data = test_case['inputdata'].encode()
    #         try:
    #             process = subprocess.run(['python', f'temp_{name}.py'], input=input_data, capture_output=True, timeout=20)
    #             output = str(process.stdout.decode()).strip()
    #             result = output == str(test_case['expectedresult']).strip()
    #             if not result:
    #                 results.append(test_case)
    #         except Exception as e:
    #             print(e)
    #             result=None
    #             break

    #     return results

    # def judge_acc_buggy(self, buggy_code, acc_code, test_case):
    #     with open(f'temp_acc.py', 'w') as f:
    #         f.write(acc_code)
    #     with open(f'temp_bug.py', 'w') as f:
    #         f.write(buggy_code)

    #     input_data = test_case['inputdata'].encode()
    #     # try:
    #     process = subprocess.run(['python', f'temp_acc.py'], input=input_data, capture_output=True, timeout=20)
    #     output_acc = str(process.stdout.decode()).strip()
    #     print(output_acc)

    #     process = subprocess.run(['python', f'temp_bug.py'], input=input_data, capture_output=True, timeout=20)
    #     output_bug = str(process.stdout.decode()).strip()
    #     print(output_bug)
        
    #     result = output_acc == output_bug
    #     if not result:
    #         return test_case
    #     # except Exception as e:
    #     #     print(e)
    #     #     return None
    
    def judge_acc_buggy(self, buggy_code, acc_code1, acc_code2, test_case):
        with open(f'temp_acc1.py', 'w') as f:
            f.write(acc_code1)
        with open(f'temp_acc2.py', 'w') as f:
            f.write(acc_code2)
        with open(f'temp_bug.py', 'w') as f:
            f.write(buggy_code)

        input_data = test_case['inputdata'].encode()
        # try:
        process = subprocess.run(['python', f'temp_acc1.py'], input=input_data, capture_output=True, timeout=20)
        output_acc1 = str(process.stdout.decode()).strip()
        print(output_acc1)

        process = subprocess.run(['python', f'temp_acc2.py'], input=input_data, capture_output=True, timeout=20)
        output_acc2 = str(process.stdout.decode()).strip()
        print(output_acc2)

        if output_acc1 == output_acc2:

            process = subprocess.run(['python', f'temp_bug.py'], input=input_data, capture_output=True, timeout=20)
            output_bug = str(process.stdout.decode()).strip()
            print(output_bug)
            result = output_acc1 == output_bug
            if not result:
                return 'Found1', test_case
            else:
                return 'InsufficientTestException', output_bug
        else:
            return 'TestValidationException', (output_acc1, output_acc2)
        return None


    # def run(self):
    #     config = 'BAD'
    #     test_generator = TestGenerator(config)
    #     df = pd.read_csv('data/py_submissions.csv')
    #     accepted_code, buggy_code, existing_test = self.prepare_data()

    #     fault_inducing_test = test_generator.generate_test(buggy_code, accepted_code, existing_test)
    #     # print(fault_inducing_test)
    #     data_list = ast.literal_eval(fault_inducing_test[0].replace('python', ''))
    #     print(data_list)

    #     # res_acc = self.judge(accepted_code, data_list, 'acc')
    #     # res_bug = self.judge(buggy_code, data_list, 'bug')

    #     try:
    #         res = self.judge_acc_buggy(buggy_code, accepted_code, data_list)
    #     except Exception as e:
    #         print(e)
    #         # run()

    #     # print('res_acc', res_acc)
    #     # print('res_bug', res_bug)

    #     # print('res', res)


    def run(self):
        config = 'BAD'
        test_generator = TestGenerator(config)
        df = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
        acc_code1, acc_code2, buggy_code, existing_test = self.prepare_data()

        fault_inducing_test = test_generator.generate_test(buggy_code, acc_code1, existing_test, None)
        data_list = ast.literal_eval(fault_inducing_test[0].replace('python', ''))
        print(data_list)

        # res_acc = self.judge(accepted_code, data_list, 'acc')
        # res_bug = self.judge(buggy_code, data_list, 'bug')

        res, out = self.judge_acc_buggy(buggy_code, acc_code1, acc_code2, data_list)

        if res == 'InsufficientTestException':
            for i in range(10):
                fault_inducing_test = test_generator.generate_test(buggy_code, acc_code1, existing_test, out)
                data_list = ast.literal_eval(fault_inducing_test[0].replace('python', ''))
                res, out = self.judge_acc_buggy(buggy_code, acc_code1, acc_code2, data_list)
                if res != 'InsufficientTestException':
                    break
        print(res)

        # print('res_acc', res_acc)
        # print('res_bug', res_bug)

        # print('res', res)

if __name__ == '__main__':
    df = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
    code_runner = CodeRunner(df['problems_id'][0], df['author'][0])
    code_runner.run()
