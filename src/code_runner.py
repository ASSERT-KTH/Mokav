from src.test_generator import TestGenerator
from src.utils import write_to_file, run_process, read_file
import pandas as pd
import ast
import logging
import os
import json

class CodeRunner:
    def __init__(self, is_func, is_qb, iteration_count, meta_data_config, generated_tests_dir, number_of_samples, temperature) -> None:
        self.is_func = is_func
        self.is_qb = is_qb
        self.iteration_count = iteration_count
        self.test_generator = TestGenerator(config=meta_data_config, number_of_samples=number_of_samples, temperature=temperature, is_qb=is_qb)
        self.generated_tests_dir = generated_tests_dir
        self.number_of_samples = number_of_samples
        self.temperature = temperature
        self.contain_exec_diff = 'E' in meta_data_config

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

    def prepare_data_qb(self, program_name):

        rej = read_file(f'quixbugs/python_programs/{program_name}.py')
        acc = read_file(f'quixbugs/correct_python_programs/{program_name}.py')
        with open(f"quixbugs/json_testcases/{program_name}.json", "r") as data_file:
            existing_test = [json.loads(line) for line in data_file]
        existing_test = existing_test[0]
        if not isinstance(existing_test, list):
            existing_test = ' '.join(map(str, existing_test))
        existing_test = {'inputdata': existing_test[0]}
        return acc, rej, existing_test
                
    def move_global_ret_inside_func(self, source):
        src_lines = source.split('\n')
        new_src_lines = [src_lines[1], '\t' + src_lines[0]]
        new_src_lines.extend(src_lines[2:])
        source = '\n'.join(new_src_lines) # global_ret is moved into the function
        return source

    def create_unnitest(self, buggy_code, acc_code, test_cases, author_id=None, problem_id=None):
        with open(f"temp_acc_qb.py", "w") as f:
            f.write(acc_code)

        with open(f"temp_bug_qb.py", "w") as f:
            f.write(buggy_code)

        unittest_str = f"""
import unittest
from temp_acc_qb import patched_func as patched_source
from temp_bug_qb import original_func as original_source

class TestFunctions(unittest.TestCase):
                
"""

        for i, test_case in enumerate(test_cases):
            input_data = test_case["inputdata"]
            if "\n" in input_data:
                input_data = list(input_data.split("\n"))

            is_input_list = type(input_data) is list

            if not is_input_list:
                input_data = f'"{input_data}"'

            unittest_str = (
                unittest_str
                + f"""

    def test{i}(self):
        input_{i} = {input_data}
        self.assertEqual(patched_source({"*" if is_input_list else ""}input_{i}), original_source({"*" if is_input_list else ""}input_{i}))
            
"""
            )

        unittest_str += """

if __name__ == '__main__':
    unittest.main()  
    
    """

        with open(f"temp_test_case.py", "w") as f:
            f.write(unittest_str)

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

    def generate_test_and_run_until_assertion_error(self, rej, acc1, existing_test, existing_test_output, 
                                                    output_code, author_id, problem_id, is_iteration=False):

        acc_unique_var_state, rej_unique_var_state = None, None

        try:
            if self.contain_exec_diff:
                acc_unique_var_state, rej_unique_var_state = self.get_exec_diff(existing_test["inputdata"], acc1, rej)
        except Exception as e:
            logging.info(f"###EXCEPTION###: {e}")

        test_case = self.test_generator.generate_test(
            rej, acc1, existing_test, existing_test_output, output_code, author_id=author_id, 
            problem_id=problem_id, acc_unique_var_state=acc_unique_var_state, bug_unique_var_state=rej_unique_var_state, is_iteration=is_iteration)
        data_list = self.change_test_to_dict(test_case)

        # Create unittests with single test method
        test_output = ''
        for i, data in enumerate(data_list):
            try:
                self.create_unnitest(rej, acc1, [data])
                output = str(run_process(["python", "temp_test_case.py"], 5))
                test_output += '\n NEW TEST OUTPUT: \n' + output
                if "AssertionError" in output:
                    break
            except Exception as e:
                test_output += f"\n NEW TEST OUTPUT: \nException: {e}"

        return test_output, data_list

    def get_code_output(self, input_data, code, is_acc=True, collect_var_states=False):
        module_name = 'acc' if is_acc else 'bug'
        func_name = 'patched' if is_acc else 'original'

        if "\n" in str(input_data):
            input_data = list(input_data.split("\n"))

        is_input_list = type(input_data) is list

        if not is_input_list:
            input_data = f'"{input_data}"'
        
        with open(f"temp_{module_name}_qb.py", "w") as f:
            f.write(code)


        filename = f"temp_{module_name}_exec.py"
        with open(filename, "w") as f:
            f.write(f'''
from temp_{module_name}_qb import {func_name}_func as {func_name}_func
input_data = {input_data}
output_code = {func_name}_func({"*" if is_input_list else ""}input_data)
output_code = list(output_code)
print(output_code)
''')


        if collect_var_states:
            process_acc_exec = run_process(["python", "-m", "spotflow", "-t", f"{func_name}_func", "unittest", filename], 5)
        else:
            process_acc_exec = run_process(["python", filename], 5)

        output = str(process_acc_exec.stdout.decode()).strip()
        return output
    
    def get_var_states(self, input_data, code, is_acc=True):
        var_info = {}

        output = self.get_code_output(input_data, code, is_acc=is_acc, collect_var_states=True)
        lines = output.splitlines()
        
        is_var_state = False
        for i, l in enumerate(lines):
            if 'VarStateHistory' in l:
                is_var_state = True
                continue

            if not is_var_state:
                continue

            if 'ReturnState:' in l:
                break

            ## We now it is a variable state line
            
            l = l.removeprefix('- ') # to ignore the starting '- ' characters
            var_name, var_values = (l.split(': ')[0], ': '.join(l.split(': ')[1:]))

            if var_name == 'args' or var_name == 'global_list':
                continue

            var_values = [x for x in var_values.split(' #SPLITTER# ') if len(str(x)) < 50] # only keep short values
            var_info[var_name] = {'states': set(var_values), 'ind': i}

        return var_info

    def get_first_unique_state(self, l_var_info, r_var_info):
        common_vars = list(set(l_var_info.keys()).intersection(set(r_var_info.keys())))

        common_vars.sort(key=lambda var: l_var_info[var]['ind'])

        for var in common_vars:
            l_states = l_var_info[var]['states']
            r_states = r_var_info[var]['states']

            unique_states = l_states.difference(r_states)

            if len(unique_states) > 0:
                return (var, list(unique_states)[0])

    def get_exec_diff(self, input_data, acc_code, rej_code):
        acc_var_info = self.get_var_states(input_data, acc_code, is_acc=True)
        rej_var_info = self.get_var_states(input_data, rej_code, is_acc=False)

        unique_acc_var_state = self.get_first_unique_state(acc_var_info, rej_var_info)
        unique_rej_var_state = self.get_first_unique_state(rej_var_info, acc_var_info)

        return unique_acc_var_state, unique_rej_var_state

    def check_test(self, acc1, rej, existing_test, problem_id, author_id):

        try:
            logging.info(
                f"###(PROBLEM_ID, AUTHOR)###: ({problem_id}, {author_id})")
            # acc1, _, rej, existing_test = self.prepare_data(problem_id, author_id)

            existing_test_output = self.get_code_output(existing_test["inputdata"], acc1)

            output, data_list = self.generate_test_and_run_until_assertion_error(
                rej, acc1, existing_test, existing_test_output, None, author_id, problem_id, is_iteration=False)
            logging.info(f"###TEMP_TEST_PY_OUTPUT: \n\n{output}")
            if not ("AssertionError" in output):
                for i in range(self.iteration_count):

                    ### TODO: if the first response doesn't have correct format, the output is computed for another response
                    if len(data_list) > 0:
                        input_data = self.process_input_data(data_list[0]["inputdata"])
                        output_code = self.get_code_output(input_data, acc1)
                    else:
                        output_code = None

                    output, data_list = self.generate_test_and_run_until_assertion_error(
                        rej, acc1, existing_test, existing_test_output, output_code, author_id, problem_id, is_iteration=True)
                    logging.info(f"###ITERATION###: {i + 1}")
                    logging.info(f"###TEMP_TEST_PY_OUTPUT_RETRY: \n\n{output}")
                    if ("AssertionError" in output):
                        self.save_generated_test(author_id, problem_id, i + 1, output)
                        return "Found1"
                return str(output)
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
                acc1, _, rej, existing_test = self.prepare_data(i[1], i[0])
                # self.check_test(acc1, rej, existing_test, i[1], i[0])
                logging.info(
                    f"###CHECK_TEST###:\n{self.check_test(acc1, rej, existing_test, i[1], i[0])}")
            # logging.info(f"###CHECK_TEST###:\n{self.check_test(1975, 60724)}")
        elif self.is_qb:
            
            program_names = os.listdir('quixbugs/python_programs/')
            for program_name in program_names:
                try:
                    acc1, rej, existing_test = self.prepare_data_qb(program_name[:-3])
                    logging.info(f"###CHECK_TEST###:\n{self.check_test(acc1, rej, existing_test, program_name, program_name)}")
                except Exception as e:
                    logging.info(f"###EXCEPTION###: {e}")

        else:
            self.check_test(1, 1)
        return "Done"
