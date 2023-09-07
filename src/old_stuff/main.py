from test_generator import TestGenerator
import pandas as pd
import random
import subprocess
import ast

def prepare_data(problem_id, author_id):
    df_submissions = pd.read_csv('data/py_submissions.csv')
    df_testcases = pd.read_csv('data/py_testcases.csv')

    df = df_submissions[(df_submissions['problems_id'] == problem_id) & (df_submissions['author'] == author_id)]['sourceCode']
    acc = df.values.tolist()[0]
    rej = df.values.tolist()[1]

    df_testcases = df_testcases[df_testcases['problems_id'] == problem_id]
    test_cases = df_testcases[['expectedresult', 'inputdata']].to_dict('records')

    # return acc, rej, random.choice(test_cases)
    return acc, rej, test_cases


# def judge(code, input_data, expected_result):
#     with open('temp.py', 'w') as f:
#         f.write(code)
#     input_data = input_data.encode()
    
#     try:
#         process = subprocess.run(['python', 'temp.py'], input=input_data, capture_output=True, timeout=20)
#         output = process.stdout.decode().strip()
#         print('output', output)
#         print('expected_result', expected_result.strip())
#         result = output == expected_result.strip()
#     except Exception as e:
#         print(e)
#         result=None
#     return result

def judge(source_code, test_cases, name):

    with open(f'temp_{name}.py', 'w') as f:
        f.write(source_code)

    results = []
    for test_case in test_cases:
        input_data = test_case['inputdata'].encode()
        try:
          process = subprocess.run(['python', f'temp_{name}.py'], input=input_data, capture_output=True, timeout=20)
          output = str(process.stdout.decode()).strip()
          result = output == str(test_case['expectedresult']).strip()
          if not result:
            results.append(test_case)
        except Exception as e:
            print(e)
            result=None
            break
        # results.append((result, output, test_case[1].strip()))

    return results

# def validate_test(code, passing_test, failing_test):
#     # passing_res = judge(code, passing_test['inputdata'], passing_test['expectedresult'])
#     passing_res = judge(code, passing_test)
#     # failing_res = judge(code, failing_test['inputdata'], failing_test['expectedresult'])
#     failing_res = judge(code, failing_test)

#     print('PASSING', passing_res)
#     print('FAILING', failing_res)
#     if passing_res and not failing_res:
#         return f'Fault Inducing Test is Found: \n\n {failing_test}'
    

def run():
    config = 'BAD'
    test_generator = TestGenerator(config)
    df = pd.read_csv('data/py_submissions.csv')
    accepted_code, buggy_code, existing_test = prepare_data(df['problems_id'][10], df['author'][10])

    fault_inducing_test = test_generator.generate_test(buggy_code, accepted_code, existing_test)
    print(fault_inducing_test)
    data_list = ast.literal_eval(fault_inducing_test[0].replace('python', ''))
    # print(data_list)
    # fault_inducing_test = random.choice(data_list)
    # print('existing_test',existing_test)
    # print('fault_inducing_test',fault_inducing_test)


    res_acc = judge(accepted_code, data_list, 'acc')
    res_bug = judge(buggy_code, data_list, 'bug')

    print('res_acc', res_acc)
    print('res_bug', res_bug)


    # validate_test(buggy_code, existing_test, data_list)

if __name__ == '__main__':
    run()









######### runner previous ##############


# from test_generator import TestGenerator
# import pandas as pd
# import random
# import subprocess
# import ast


# import time
# from functools import wraps


# def retry_decorator(max_retries=3, delay=1):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             retry_count = 0
#             while retry_count < max_retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     print(f"Exception occurred: {e}")
#                     retry_count += 1
#                     print(f"Retrying... (Attempt {retry_count} of {max_retries})")
#                     time.sleep(delay)
#             print(f"Max retries reached. Giving up.")
#         return wrapper
#     return decorator


# class CodeRunner:
#     def __init__(self, problem_id, author_id):
#         self.problem_id = problem_id
#         self.author_id = author_id

#     def prepare_data(self):
#         df_submissions = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
#         df_testcases = pd.read_csv('data/2acc/cb_testcase_res_2acc.csv')

#         df = df_submissions[(df_submissions['problems_id'] == self.problem_id) & (
#             df_submissions['author'] == self.author_id)]['sourceCode']
#         df_acc_other = df_submissions[(df_submissions['verdicts_id'] == 1) & (
#             df_submissions['problems_id'] == self.problem_id) & (df_submissions['author'] != self.author_id)]['sourceCode']
#         acc1 = df.values.tolist()[0]
#         rej = df.values.tolist()[1]
#         acc2 = df_acc_other.values.tolist()[0]

#         df_testcases = df_testcases[df_testcases['problems_id']
#                                     == self.problem_id]
#         test_cases = df_testcases[['inputdata']].to_dict('records')

#         return acc1, acc2, rej, test_cases[0]

#     def judge_acc_buggy(self, buggy_code, acc_code1, acc_code2, test_cases):
#         with open(f'temp_acc1.py', 'w') as f:
#             f.write(acc_code1)
#         with open(f'temp_acc2.py', 'w') as f:
#             f.write(acc_code2)
#         with open(f'temp_bug.py', 'w') as f:
#             f.write(buggy_code)
#         for test_case in test_cases:
#             input_data = test_case['inputdata'].encode()
#             process = subprocess.run(
#                 ['python', f'temp_acc1.py'], input=input_data, capture_output=True, timeout=20)
#             output_acc1 = str(process.stdout.decode()).strip()
#             print('output_acc1:', output_acc1)

#             process = subprocess.run(
#                 ['python', f'temp_acc2.py'], input=input_data, capture_output=True, timeout=20)
#             output_acc2 = str(process.stdout.decode()).strip()
#             print('output_acc2: ',output_acc2)

#             if output_acc1 == output_acc2:

#                 process = subprocess.run(
#                     ['python', f'temp_bug.py'], input=input_data, capture_output=True, timeout=20)
#                 output_bug = str(process.stdout.decode()).strip()
#                 print('output_bug: ',output_bug)
#                 result = output_acc1 == output_bug
#                 if not result:
#                     res, out = 'Found1', test_case
#                 else:
#                     res, out = 'InsufficientTestException', output_bug
#             else:
#                 res, out = 'TestValidationException', (output_acc1, output_acc2)            
#         return res, out

#     @retry_decorator(max_retries=3, delay=1)
#     def run(self):
#         asb
#         config = 'BADT'
#         test_generator = TestGenerator(config)
#         df = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
#         acc_code1, acc_code2, buggy_code, existing_test = self.prepare_data()

#         fault_inducing_test = test_generator.generate_test3(
#             buggy_code, acc_code1, existing_test, None)
#         fault_inducing_test = [item for sublist in fault_inducing_test for item in sublist]
#         print("###FAULTIND###\n\n", fault_inducing_test)
#         data_list = []
#         for fault_test in fault_inducing_test:
#             # print(fault_test)
#             data_list.append(ast.literal_eval(
#                 fault_test.replace('python', '')))
#         # data_list = ast.literal_eval(
#         #     fault_inducing_test[0].replace('python', ''))
#         print("###DATALIST###\n\n", data_list)

#         res, out = self.judge_acc_buggy(
#             buggy_code, acc_code1, acc_code2, data_list)
        
#         # print(res)

#         if res == 'InsufficientTestException' or res == 'TestValidationException':
#             for i in range(10):
#                 fault_inducing_test = test_generator.generate_test3(
#                     buggy_code, acc_code1, existing_test, out)
#                 fault_inducing_test = [item for sublist in fault_inducing_test for item in sublist]
#                 data_list = []
#                 for fault_test in fault_inducing_test:
#                     data_list.append(ast.literal_eval(
#                         fault_test.replace('python', '')))
#                 res, out = self.judge_acc_buggy(
#                     buggy_code, acc_code1, acc_code2, data_list)
#                 if res != 'InsufficientTestException':
#                     break
#         print(res, out)


# if __name__ == '__main__':
#     df = pd.read_csv('data/2acc/cb_submission_res_2acc.csv')
#     code_runner = CodeRunner(df['problems_id'][0], df['author'][0])
#     code_runner.run()
#     # df = df[:40]
#     # for i in range(len(df)):
#     #     code_runner = CodeRunner(df['problems_id'][i], df['author'][0])
#     #     code_runner.run()
