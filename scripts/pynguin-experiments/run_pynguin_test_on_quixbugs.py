import sys
import os
import glob

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

def log_test_res(quixbugs_dir, test_file, test_res_dir, program, test_gen_ind):
    generated_test_dir = '/'.join(test_file.split("/")[0:-1])
    buggy_code = f'{quixbugs_dir}/python_programs/{program}.py'
    correct_code = f'{quixbugs_dir}/correct_python_programs/{program}.py'

    os.system(f'cp {buggy_code} {generated_test_dir}/{program}.py')
    test_log_file = f'{test_res_dir}/{program}_{test_gen_ind}_buggy.log'
    os.system(f'timeout 30 pytest {test_file} > {test_log_file}')
    failed, passed, xfailed = extract_test_res(f'{test_log_file}')
    os.system(f'echo "{program},buggy,{test_gen_ind},{failed},{passed},{xfailed}" >> {test_res_dir}/results.csv')

    os.system(f'cp {correct_code} {generated_test_dir}/{program}.py')
    test_log_file = f'{test_res_dir}/{program}_{test_gen_ind}_correct.log'
    os.system(f'timeout 30 pytest {test_file} > {test_log_file}')
    failed, passed, xfailed = extract_test_res(f'{test_log_file}')
    os.system(f'echo "{program},correct,{test_gen_ind},{failed},{passed},{xfailed}" >> {test_res_dir}/results.csv')

def main(argv):
    test_dir = argv[0]
    quixbugs_dir = argv[1]
    test_res_dir = argv[2]
    res = glob.glob(f'{test_dir}/*/*/test_transformed_*.py')
    for p in res:

        # if p != 'pynguin-res/lcs_length/0/test_transformed_lcs_length.py':
        #     continue

        program = p.split("/")[1]
        test_gen_ind = p.split("/")[2]
        
        log_test_res(quixbugs_dir, p, test_res_dir, program, test_gen_ind)

if __name__ == "__main__":
    main(sys.argv[1:])