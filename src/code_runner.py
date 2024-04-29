from src.test_generator import TestGenerator
from src.utils import write_to_file, run_process
import pandas as pd
import ast
import logging
import os

class CodeRunner:
    def __init__(self, is_func, is_qb, is_iterative, meta_data_config, generated_tests_dir) -> None:
        self.is_func = is_func
        self.is_qb = is_qb
        self.is_iteravtive = is_iterative
        self.test_generator = TestGenerator(config=meta_data_config)
        self.generated_tests_dir = generated_tests_dir

        if is_func:
            self.df_submissions = pd.read_csv(
                "c4b_data/cb_submission_res_v_0_3.csv"
            )
            self.df_testcases = pd.read_csv(
                "c4b_data/cb_testcase_res_2acc.csv")

    def prepare_data(self, problem_id, author_id) -> tuple:
        df = self.df_submissions[
            (self.df_submissions["problems_id"] == problem_id)
            & (self.df_submissions["author"] == author_id)
        ]["func_sourceCode_list_2"]
        df_acc_other = self.df_submissions[
            (self.df_submissions["verdicts_id"] == 1)
            & (self.df_submissions["problems_id"] == problem_id)
            & (self.df_submissions["author"] != author_id)
        ]["func_sourceCode_list_2"]
        acc1 = self.move_global_ret_inside_func(df.values.tolist()[0])
        rej = self.move_global_ret_inside_func(df.values.tolist()[1])
        # acc2 = df_acc_other.values.tolist()[0]
        acc2 = None

        df_testcase = self.df_testcases[self.df_testcases["problems_id"] == problem_id]
        test_cases = df_testcase[["inputdata"]].to_dict("records")

        return acc1, acc2, rej, test_cases[0]
    
    def move_global_ret_inside_func(self, source):
        src_lines = source.split('\n')
        new_src_lines = [src_lines[1], '\t' + src_lines[0]]
        new_src_lines.extend(src_lines[2:])
        source = '\n'.join(new_src_lines) # global_ret is moved into the function
        return source

    def create_unnitest(self, buggy_code, acc_code, test_cases, author_id=None, problem_id=None):
        with open(f"temp_acc_qb.py", "w") as f:
            f.write(acc_code)

        write_to_file(
            f"results_sample/sample_{author_id}_{problem_id}", "accepted.py", acc_code)
        with open(f"temp_bug_qb.py", "w") as f:
            f.write(buggy_code)

        write_to_file(
            f"results_sample/sample_{author_id}_{problem_id}", "buggy.py", buggy_code)

        unittest_str = f"""
import unittest
from temp_bug_qb import original_func as original_source
from temp_acc_qb import patched_func as patched_source

class TestFunctions(unittest.TestCase):
                
"""

        for i, test_case in enumerate(test_cases):
            input_data = test_case["inputdata"]
            if "\n" in input_data:
                input_data = list(input_data.split("\n"))

            unittest_str = (
                unittest_str
                + f"""

    def test{i}(self):
        input_{i} = "{input_data}"
        self.assertEqual(patched_source(input_{i}), original_source(input_{i}))
            
"""
            )

        unittest_str += """

if __name__ == '__main__':
    unittest.main()  
    
    """

        with open(f"temp_test_case.py", "w") as f:
            f.write(unittest_str)
        with open(f"results_sample/sample_{author_id}_{problem_id}/test.py", "w+") as f:
            f.write(unittest_str)
        write_to_file(
            f"results_sample/sample_{author_id}_{problem_id}", "test.py", unittest_str)

    def change_test_to_dict(self, test_case) -> list:
        data_list = []
        for difference_exposing_test in test_case:
            if difference_exposing_test:
                try:
                    data_list.append(ast.literal_eval(
                        difference_exposing_test[0].replace("python", "")))
                except Exception as e:
                    print(e)
                    logging.info(f"ast.literal_eval error: {e}")
                    continue
        return data_list

    def process_input_data(self, input_data):
        if "\n" in input_data:
            return list(input_data.split("\n"))
        return input_data

    def generate_test_and_run(self, rej, acc1, test_case, output_code, author_id, problem_id):
        test_case = self.test_generator.generate_test(
            rej, acc1, test_case, output_code, author_id=author_id, problem_id=problem_id)
        data_list = self.change_test_to_dict(test_case)
        self.create_unnitest(rej, acc1, data_list)
        return str(run_process(["python", "temp_test_case.py"], 50)), data_list

    def accepted_code_output(self, input_data):

        with open(f"temp_acc_exec.py", "w") as f:
            f.write(f'''
from temp_acc_qb import patched_func as patched_func
input_data = "{input_data}"
output_code = patched_func(input_data)
output_code = list(output_code)
print(output_code)
''')
        process_acc_exec = run_process(["python3", f"temp_acc_exec.py"], 50)
        output_code = str(process_acc_exec.stdout.decode()).strip()
        return output_code

    def check_test(self, problem_id, author_id):

        try:
            logging.info(
                f"###(PROBLEM_ID, AUTHOR)###: ({problem_id}, {author_id})")
            acc1, _, rej, test_case = self.prepare_data(problem_id, author_id)
            output, data_list = self.generate_test_and_run(
                rej, acc1, test_case, None, author_id, problem_id)
            print("###TEMP_TEST_PY_OUTPUT", output)
            logging.info(f"###TEMP_TEST_PY_OUTPUT: \n\n{output}")
            if not (("AssertionError" in output) or (("temp_acc_qb.py" not in output) and ("temp_bug_qb.py" in output))):
                if self.is_iteravtive:
                    for i in range(10):
                        print("data list", data_list)
                        input_data = self.process_input_data(
                            data_list[0]["inputdata"])
                        output_code = self.accepted_code_output(input_data)
                        output, data_list = self.generate_test_and_run(
                            rej, acc1, test_case, output_code, author_id, problem_id)
                        print("###TEMP_TEST_PY_OUTPUT_RETRY", output)
                        logging.info(f"###ITERATION###: {i + 1}")
                        logging.info(f"###TEMP_TEST_PY_OUTPUT_RETRY: \n\n{output}")
                        if ("AssertionError" in output) or (("temp_acc_qb.py" not in output) and ("temp_bug_qb.py" in output)):
                            self.save_generated_test(author_id, problem_id, i + 1, output)
                            return "Found1"
                return str(output)
            elif "Timeout" in output:
                return "Timeout!!"
            else:
                self.save_generated_test(author_id, problem_id, 0, output)
                return "Found1"
        except Exception as e:
            logging.info(f"###EXCEPTION###: {e}")
            return "Exception!!"

    def save_generated_test(self, author_id, problem_id, iteration_ind, execution_output):
        os.system(f'mkdir {self.generated_tests_dir}/{problem_id}')
        full_dir = f'{self.generated_tests_dir}/{problem_id}/{author_id}'
        os.system(f'mkdir {full_dir}')
        os.system(f'cp temp_test_case.py {full_dir}/temp_test_case_{iteration_ind}.py')
        os.system(f'cp temp_acc_qb.py {full_dir}/temp_acc_qb.py')
        os.system(f'cp temp_bug_qb.py {full_dir}/temp_bug_qb.py')
        write_to_file(f"{full_dir}", f"test_output.txt", execution_output)

    # @retry_decorator(max_retries=3, delay=1)
    def run(self):
        if self.is_func:
            grouped = (
                self.df_submissions.groupby(["author", "problems_id"])[
                    "diff_ratio"]
                .mean()
                .reset_index()
            )
            grouped = grouped.sort_values("diff_ratio", ascending=False)
            result = grouped[
                ["author", "problems_id"]
            ].values.tolist()

            for i in result:
                # print(self.check_test(i[1], i[0]))
                logging.info(
                    f"###CHECK_TEST###:\n{self.check_test(i[1], i[0])}")
            # logging.info(f"###CHECK_TEST###:\n{self.check_test(1975, 60724)}")

        else:
            self.check_test(1, 1)
        return "Done"
