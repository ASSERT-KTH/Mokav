import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import scipy as sp
from Levenshtein import ratio
import gpt3_tokenizer
from statistics import median

PAIR_CNT = 1535

def get_valid_pairs():
    valid_pairs = set()
    with open('tmp/tmp/valid_pairs.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            l = l.strip()
            valid_pairs.add(tuple(l.split(',')))
    return valid_pairs

def extract_submissions_with_det(generated_tests_dir):
    submissions = set()

    for problem in os.scandir(generated_tests_dir):
        if not problem.is_dir():
            continue

        for author in os.scandir(problem):
            if not author.is_dir():
                continue

            if (problem.name, author.name) in get_valid_pairs():
                submissions.add((problem.name, author.name))
    
    return submissions

def compute_sdet_r_cor(submissions_df_file, tests_df_file, generated_tests_dir, subset_cnt, sorting_val_type):
    print(f"COMPUTING CORRELATION BETWEEN SDET_R AND {sorting_val_type} STARTED...")
    submissions_with_det = extract_submissions_with_det(generated_tests_dir)
    
    df = pd.read_csv(submissions_df_file)
    df = df[df.apply(lambda x: (str(x['problems_id']), str(x['author'])) in get_valid_pairs(), axis=1)]
    df_testcases = pd.read_csv(tests_df_file)
    longest_test = 0
    longest_src = 0
    for submission in df.to_dict('records'):
        problem_id = submission['problems_id']
        author = submission['author']

        tdf = df[(df['problems_id'] ==  problem_id) & (df['author'] == author)].to_dict('records')
        
        if sorting_val_type == 'diff_ratio':
            sorting_val = ratio(tdf[0]['sourceCode'], tdf[1]['sourceCode'])
        elif sorting_val_type == 'src_tokens':
            patched_tokens = gpt3_tokenizer.count_tokens(tdf[0]['sourceCode'])
            original_tokens = gpt3_tokenizer.count_tokens(tdf[1]['sourceCode'])
            if patched_tokens > longest_src:
                longest_src = patched_tokens
            if original_tokens > longest_src:
                longest_src = original_tokens
            sorting_val = gpt3_tokenizer.count_tokens(tdf[0]['sourceCode']) + gpt3_tokenizer.count_tokens(tdf[1]['sourceCode'])
        elif sorting_val_type == 'test_tokens':
            df_testcase = df_testcases[df_testcases["problems_id"] == problem_id]
            df_testcase = df_testcase.sort_values(by='inputdata', ascending=False, key=lambda x: x.apply(lambda y: gpt3_tokenizer.count_tokens(y)))
            test_case = df_testcase.to_dict("records")[0]["inputdata"]
            sorting_val = gpt3_tokenizer.count_tokens(test_case)
            if sorting_val > longest_test:
                longest_test = sorting_val
        else:
            raise ValueError(f'Invalid sorting_val_type: {sorting_val_type}')

        df.loc[(df.problems_id == problem_id) & (df.author == author),'sorting_val'] = sorting_val

    df = df[df['verdicts_id'] == 1]

    df = df.drop(df[df.sourceCode.str.len() > 10000].index) # problems_id = 2521, author = 2014

    df = df.sort_values(by=['sorting_val'])
        
    subset_to_detcnt = np.zeros(subset_cnt)

    subset_size = len(df) // subset_cnt

    subset_to_sorting_vals = [[] for _ in range(subset_cnt)]

    for i in range(1, subset_cnt + 1):
        for submission in df.to_dict('records')[(i-1)*subset_size:i*subset_size if i < subset_cnt else len(df)]:
            problem_id = submission['problems_id']
            author = submission['author']

            if not (str(problem_id), str(author)) in get_valid_pairs():
                continue

            subset_to_sorting_vals[i - 1].append(submission['sorting_val'])
            if (str(problem_id), str(author)) in submissions_with_det:
                subset_to_detcnt[i - 1] += 1

    subset_to_detcnt[:-1] = subset_to_detcnt[:-1] / subset_size
    subset_to_detcnt[-1] = subset_to_detcnt[-1] / (len(df) - (subset_cnt - 1) * subset_size)
    
    for i, sorting_vals in enumerate(subset_to_sorting_vals):
        print(f'S{i + 1} median value: {median(sorting_vals)}')

    xdata = range(1, 11)
    ydata = subset_to_detcnt
    print('S{i} sdet_r', subset_to_detcnt)
    print(sp.stats.spearmanr(xdata, ydata))

    print(f"COMPUTING CORRELATION BETWEEN SDET_R AND {sorting_val_type} FINISHED...")

def main(argv):
    submissions_df_file = 'DET-Gen/c4b_data/cb_submission_res_v_0_3.csv'
    tests_df_file = 'DET-Gen/c4b_data/cb_testcase_res_2acc.csv'
    generated_tests_dir = 'tmp/tmp/generated_tests'
    subset_cnt = 10

    # compute_sdet_r_cor(submissions_df_file, tests_df_file, generated_tests_dir, subset_cnt, 'src_tokens')
    # compute_sdet_r_cor(submissions_df_file, tests_df_file, generated_tests_dir, subset_cnt, 'test_tokens')
    compute_sdet_r_cor(submissions_df_file, tests_df_file, generated_tests_dir, subset_cnt, 'diff_ratio')

if __name__ == "__main__":
    main(sys.argv[1:])