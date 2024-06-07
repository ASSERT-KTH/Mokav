import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import scipy as sp
import glob
from Levenshtein import ratio

def get_valid_pairs():
    valid_pairs = set()
    with open('valid_pairs.csv', 'r') as file:
        lines = file.readlines()[1:]
        for l in lines:
            l = l.strip()
            valid_pairs.add(tuple(l.split(',')))
    return valid_pairs

def plot_iteration_success():
    det_per_iter = [905, 1068, 1137, 1173, 1203, 1225, 1234, 1245, 1251, 1255]
    f, ax = plt.subplots(1)
    xdata = range(1, 11)
    ydata = det_per_iter

    ax.set_xlabel("Iteration", weight='bold', fontsize=16)
    ax.set_ylabel("#Success_Pair", weight='bold', fontsize=16)
    ax.xaxis.set_tick_params(labelsize=14)
    ax.yaxis.set_tick_params(labelsize=14, labelrotation=45)

    ax.plot(xdata, ydata, linewidth=2, color='orange', marker='o', markersize=5)

    plt.savefig('iter_success.pdf', format='pdf', bbox_inches='tight')

def get_valid_qb_programs():
    return [x.replace('.py', '') for x in 'powerset.py, knapsack.py, lis.py, longest_common_subsequence.py, breadth_first_search.py, to_base.py, next_palindrome.py, find_first_in_sorted.py, levenshtein.py, find_in_sorted.py, lcs_length.py, gcd.py, hanoi.py, quicksort.py, is_valid_parenthesization.py, rpn_eval.py, depth_first_search.py, kheapsort.py, get_factors.py, next_permutation.py, sieve.py, kth.py, pascal.py, subsequences.py, mergesort.py, max_sublist_sum.py, topological_ordering.py, bucketsort.py, possible_change.py, flatten.py, shunting_yard.py, detect_cycle.py'.split(', ')]

def count_pynguin_tests():
    is_qb = True

    valid_qb_programs = get_valid_qb_programs()
    valid_pairs = get_valid_pairs()
    df_submissions = pd.read_csv('cb_submission_res_2acc_alt.csv')
    df_submissions = df_submissions[(df_submissions['failed_tests_ratio'] < 0.9)
                                    & (df_submissions['verdicts_id'] == 1)]
    submissions = df_submissions.to_dict('records')

    pynguin_qb_tests_dir = 'tmp/pynguin-qb/tests-for-correct-version/pynguin-qb-mutation-res'
    pyngun_transformed_tests = glob.glob(f'{pynguin_qb_tests_dir}/*/*/test_transformed*.py')

    all_tests_cnt = 0
    for x in pyngun_transformed_tests:
        iteration = int(x.split("/")[-2])
        if iteration > 9:
            continue

        if not is_qb:
            src_ind = int(x.split("/")[-3].split("_")[-1])
        if (not is_qb) and (not (str(submissions[src_ind]['problems_id']), str(submissions[src_ind]['author'])) in valid_pairs):
            continue

        if is_qb:
            program = x.split("/")[-3]
        if is_qb and not program in valid_qb_programs:
            continue

        with open(x, 'r') as file:
            test = file.read()
            all_tests_cnt += test.count("def test_")
    
    print(f'{pynguin_qb_tests_dir} test count: {all_tests_cnt}')

def count_total_pynguin_tests():
    count_pynguin_tests("pynguin-qb-mutation-res")

    count_pynguin_tests("tmp/pynguin-c4b-tests/generated_tests")

def count_iteration_dets():
    valid_pairs = get_valid_pairs()
    valid_pairs_cnt = len(valid_pairs)

    tests_dir = 'tmp/generated_tests'
    os.chdir(f'{tests_dir}')
    all_test_cnt = 0
    for i in range(10):
        generated_test_files = os.popen(f'find . -type f -name "temp_test_case_{i}*"').read().split('\n')[:-1]
        generated_test_files = [x for x in generated_test_files if tuple(x.split('/')[1:3]) in valid_pairs]

        all_test_cnt += len(generated_test_files)
        print(f'DETs at iteration {i}: {all_test_cnt / valid_pairs_cnt}%', all_test_cnt)

def get_c4b_pairs_with_det(tests_dir):
    valid_pairs = get_valid_pairs()
    generated_test_files = os.popen(f'find {tests_dir} -type f -name "temp_test_case*"').read().split('\n')[:-1]
    return set([tuple(tuple(x.split('/')[-3:-1])) for x in generated_test_files if tuple(x.split('/')[-3:-1]) in valid_pairs])

def count_mokav_tests():
    valid_pairs = get_valid_pairs()

    log_file = 'tmp/tmp/logs/logging_2024-05-16-22-10.log'

    iter_invocations = dict.fromkeys(range(10), 0)

    iter_ind = -1
    new_submission = False
    cur_problem, cur_author = None, None
    with open(log_file, 'r') as file:
        lines = file.readlines()
        for l in lines:
            l = l.strip()

            if '(PROBLEM_ID, AUTHOR)' in l:
                cur_problem, cur_author = l.split()[-2:]
                cur_problem, cur_author = cur_problem.replace('(', '').replace(',', ''), cur_author.replace(')', '')
                iter_ind = 0
                if new_submission:
                    print(l)
                new_submission = True
            if '#ITERATION#' in l:
                iter_ind = int(l.split(' ')[-1])
                if (cur_problem, cur_author) in get_valid_pairs():
                    iter_invocations[iter_ind] += 1

            if "CHATRES" in l:
                if new_submission:
                    if (cur_problem, cur_author) in get_valid_pairs():
                        iter_invocations[iter_ind] += 1
                new_submission = False

    for i in reversed(range(10)):
        iter_invocations[i] = sum([v for k, v in iter_invocations.items() if k <= i])
    print(iter_invocations)

def count_iter_det_problems():
    valid_pairs = get_valid_pairs()

    valid_problems = set([x[0] for x in valid_pairs])
    print(f'Valid problems: {len(valid_problems)}')

    tests_dir = 'tmp/tmp/generated_tests'
    os.chdir(f'{tests_dir}')
    all_det_prs = set()
    for i in range(10):
        test_files = os.popen(f'find . -type f -name "temp_test_case_{i}*"').read().split('\n')[:-1]
        all_det_prs = all_det_prs.union(set([x.split('/')[1] for x in test_files if tuple(x.split('/')[1:3]) in valid_pairs]))
        print(f'DET_PR for {i}: {len(all_det_prs) / len(valid_problems)} {len(all_det_prs)}')

def count_test_method_dets():
    valid_pairs = get_valid_pairs()
    assertion_err_log_file = 'tmp/tmp/assertion_error.log'
    df_submissions = pd.read_csv('DET-Gen/c4b_data/cb_submission_res_v_0_3.csv')
    submissions = df_submissions[df_submissions['verdicts_id'] == 1].to_dict('records')
    
    iter_det_count = {}

    with open(assertion_err_log_file, 'r') as file:
        lines = file.readlines()

        pair_cnt = 0
        cur_problem, cur_author = None, None
        for l in lines:
            if 'Iteration' in l:
                iter_ind = int(l.split(' ')[-1])
                if iter_ind == 0:
                    cur_problem, cur_author = str(submissions[pair_cnt]['problems_id']), str(submissions[pair_cnt]['author'])
                    pair_cnt += 1
                if iter_ind not in iter_det_count:
                    iter_det_count[iter_ind] = 0
            elif 'AssertionError' in l:
                if (cur_problem, cur_author) in valid_pairs:
                    iter_det_count[iter_ind] += 1
    
    for i in reversed(range(10)):
        iter_det_count[i] = sum([v for k, v in iter_det_count.items() if k <= i])
    
    print(iter_det_count)

def get_diff_between_configs():
    valid_pairs = get_valid_pairs()

    main_tests_dir = 'tmp/main/generated_tests'
    we_tests_dir = 'tmp/we/generated_tests'
    gpt4_tests_dir = 'tmp/gpt4/generated_tests'
    main_generated_test_files = os.popen(f'find {main_tests_dir} -type f -name "temp_test_case_*"').read().split('\n')[:-1]
    main_generated_tests = set([tuple(x.split('/')[3:5]) for x in main_generated_test_files if tuple(x.split('/')[3:5]) in valid_pairs])

    we_generated_test_files = os.popen(f'find {we_tests_dir} -type f -name "temp_test_case_*"').read().split('\n')[:-1]
    we_generated_tests = set([tuple(x.split('/')[3:5]) for x in we_generated_test_files if tuple(x.split('/')[3:5]) in valid_pairs])

    gpt4_generated_test_files = os.popen(f'find {gpt4_tests_dir} -type f -name "temp_test_case_*"').read().split('\n')[:-1]
    gpt4_generated_tests = set([tuple(x.split('/')[3:5]) for x in gpt4_generated_test_files if tuple(x.split('/')[3:5]) in valid_pairs])

    print(f'{len(main_generated_tests.difference(we_generated_tests))}')
    print(f'{len(main_generated_tests.difference(we_generated_tests).difference(gpt4_generated_tests))}')
    print(f'{main_generated_tests.difference(we_generated_tests).difference(gpt4_generated_tests)}')

def main(argv):
    codellama = get_c4b_pairs_with_det('tmp/codellama')
    temp0 = get_c4b_pairs_with_det('tmp/temp0')
    no_ex = get_c4b_pairs_with_det('tmp/no-ex')
    no_ed = get_c4b_pairs_with_det('tmp/no-ed')
    no_desc = get_c4b_pairs_with_det('tmp/no-desc')
    mokav = get_c4b_pairs_with_det('tmp/mokav')
    gpt_4_temp_0 = get_c4b_pairs_with_det('tmp/gpt-4-temp-0')
    gpt_4 = get_c4b_pairs_with_det('tmp/gpt-4')
    dpp = get_c4b_pairs_with_det('tmp/dpp')
    mokav2 = get_c4b_pairs_with_det('tmp/mokav2')
    mokav3 = get_c4b_pairs_with_det('tmp/mokav3')
    mokav4 = get_c4b_pairs_with_det('tmp/mokav4')
    mokav5 = get_c4b_pairs_with_det('tmp/mokav5')

    valid_pairs = get_valid_pairs()
    pairs_without_det = valid_pairs - codellama - temp0 - no_ex - no_ed - no_desc - mokav - gpt_4_temp_0 - gpt_4 - dpp - mokav2 - mokav3 - mokav4 - mokav5
    print(len(pairs_without_det))
    
    submissions = pd.read_csv('DET-Gen/c4b_data/cb_submission_res_v_0_3.csv')

    for pair in pairs_without_det:
        pair_submissions = submissions[(submissions['problems_id'] == int(pair[0])) & (submissions['author'] == int(pair[1]))].to_dict('records')
        acc_src = pair_submissions[0]['sourceCode']
        if acc_src.count('\n') > 7:
            continue

        print("ACCEPTED:")
        print(pair_submissions[0]['sourceCode'])
        print("REJECTED:")
        print(pair_submissions[1]['sourceCode'])

if __name__ == "__main__":
    main(sys.argv[1:])  