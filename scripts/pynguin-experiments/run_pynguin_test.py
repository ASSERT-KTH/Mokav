import sys
import os
import glob
import pandas as pd

def extract_test_res(test_res_file):
    with open(test_res_file) as file:
        lines = file.readlines()
        for line in list(reversed(lines)):
            line = line.replace("\n", "")
            if '====' in line:
                line = line.replace(',', '')
                parts = line.split(' ')
                failed = passed = xfailed = 0
                for i, part in enumerate(parts):
                    if part == 'failed':
                        failed = int(parts[i - 1])
                    if part == 'passed':
                        passed = int(parts[i - 1])
                    if part == 'xfailed':
                        xfailed = int(parts[i - 1])
                return failed, passed, xfailed
    return None, None, None

def log_test_res(buggy_code, correct_code, test_file, test_res_dir, program, test_gen_ind):
    generated_test_dir = '/'.join(test_file.split("/")[0:-1])
    program_path = f'{generated_test_dir}/{program}.py'

    with open(f"{program_path}", "w") as text_file:
        text_file.write(buggy_code)
    test_log_file = f'{test_res_dir}/{program}_{test_gen_ind}_buggy.log'
    os.system(f'timeout 30 pytest {test_file} > {test_log_file}')
    failed, passed, xfailed = extract_test_res(f'{test_log_file}')
    os.system(f'echo "{program},buggy,{test_gen_ind},{failed},{passed},{xfailed}" >> {test_res_dir}/results.csv')

    with open(f"{program_path}", "w") as text_file:
        text_file.write(correct_code)
    test_log_file = f'{test_res_dir}/{program}_{test_gen_ind}_correct.log'
    os.system(f'timeout 30 pytest {test_file} > {test_log_file}')
    failed, passed, xfailed = extract_test_res(f'{test_log_file}')
    os.system(f'echo "{program},correct,{test_gen_ind},{failed},{passed},{xfailed}" >> {test_res_dir}/results.csv')

def transform_print_to_return(source, use_ret_lst):
    if use_ret_lst:
        source = source.replace("def func(*args):\n", "def func(*args):\n\tret_values = []\n")
        source = source.replace("print(", "ret_values.append(")
        source = source + "\n\treturn ret_values\n"
    else:
        source = source.replace("print(", "return(")

    return source

def main(argv):
    test_dir = argv[0]
    test_res_dir = argv[1]
    mode = argv[2]

    if mode != 'quixbugs' and mode != 'c4b':
        return
    
    if mode == 'c4b':
        df_submissions = pd.read_csv(argv[3])
        df_correct_submissions = df_submissions[(df_submissions['failed_tests_ratio'] < 0.9)
                                    & (df_submissions['verdicts_id'] == 1)]
        src_lst = df_correct_submissions['func_sourceCode'].values.tolist()
        author_lst = df_correct_submissions['author'].values.tolist()
        problem_id_lst = df_correct_submissions['problems_id'].values.tolist()

        use_ret_lst = eval(argv[4])

    elif mode == 'quixbugs':
        programs_dir = argv[3]

    res = glob.glob(f'{test_dir}/*/*/test_transformed_*.py')
    for p in res:
        program = p.split("/")[1]
        test_gen_ind = p.split("/")[2]

        if mode == 'c4b':
            program_ind = int(program.split("_")[1])
            correct_code = src_lst[program_ind]

            author = author_lst[program_ind]
            problem_id = problem_id_lst[program_ind]

            df_buggy_submissions = df_submissions[(df_submissions['author'] == author)
                                            & (df_submissions['problems_id'] == problem_id)
                                            & (df_submissions['verdicts_id'] != 1)]
            
            buggy_submissions = df_buggy_submissions['func_sourceCode'].values.tolist()
            try:
                assert len(buggy_submissions) == 1
            except:
                print(f'Error: {len(buggy_submissions)} buggy submissions found for {author} {problem_id}')
                continue
            buggy_code = buggy_submissions[0]

            correct_code = transform_print_to_return(correct_code, use_ret_lst)
            buggy_code = transform_print_to_return(buggy_code, use_ret_lst)

        elif mode == 'quixbugs':
            with open(f'{programs_dir}/python_programs/{program}.py', 'r') as file:
                buggy_code = file.read()
            with open(f'{programs_dir}/correct_python_programs/{program}.py', 'r') as file:
                correct_code = file.read()
        
        log_test_res(buggy_code, correct_code, p, test_res_dir, program, test_gen_ind)

if __name__ == "__main__":
    main(sys.argv[1:])