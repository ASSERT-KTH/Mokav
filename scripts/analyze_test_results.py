import sys
import json 
import pandas as pd
import glob

MAX_ITERATIONS = 10

def get_valid_pairs():
    valid_pairs = set()
    with open('./valid_pairs.txt', 'r') as file:
        lines = file.readlines()
        for l in lines:
            l = l.strip()
            valid_pairs.add(tuple(l.split(',')))
    return valid_pairs

def retrive_valid_src_ids_to_submission(dataset_v2_file, dataset_v3_filer):
    valid_pairs = get_valid_pairs()
    df_v2 = pd.read_csv(dataset_v2_file)
    df_v3 = pd.read_csv(dataset_v3_filer)

    df_v2 = df_v2[df_v2['verdicts_id'] == 1]
    df_v3 = df_v3[df_v3['verdicts_id'] == 1]

    valid_src_ids_to_submissions = {}

    for i, submission in enumerate(df_v2.to_dict('records')):
        problem_id = submission['problems_id']
        author = submission['author']

        if not (str(problem_id), str(author)) in valid_pairs:
            continue
        
        if df_v3[(df_v3['problems_id'] == problem_id) & (df_v3['author'] == author)].empty:
            continue
        
        valid_src_ids_to_submissions[f'src_{i}'] = (problem_id, author)

    return valid_src_ids_to_submissions

def get_valid_qb_programs():
    return [x.replace('.py', '') for x in 'powerset.py, knapsack.py, lis.py, longest_common_subsequence.py, breadth_first_search.py, to_base.py, next_palindrome.py, find_first_in_sorted.py, levenshtein.py, find_in_sorted.py, lcs_length.py, gcd.py, hanoi.py, quicksort.py, is_valid_parenthesization.py, rpn_eval.py, depth_first_search.py, kheapsort.py, get_factors.py, next_permutation.py, sieve.py, kth.py, pascal.py, subsequences.py, mergesort.py, max_sublist_sum.py, topological_ordering.py, bucketsort.py, possible_change.py, flatten.py, shunting_yard.py, detect_cycle.py'.split(', ')]

def extract_test_method_dets():
    valid_src_ids_to_submission = retrive_valid_src_ids_to_submission("cb_submission_res_2acc_alt.csv", "cb_submission_res_v_0_3.csv")
    valid_qb_programs = get_valid_qb_programs()

    test_res_dir = 'tmp/pynguin/test_results'

    is_qb = 'qb' in test_res_dir

    test_res_files = glob.glob(f'{test_res_dir}/*.log')

    test_method_results = {}

    for test_res_file in test_res_files:
        with open(test_res_file, "r") as f:
            lines = f.readlines()

            ## lines are like: ==============
            ##.....
            ##test_file F.F..... [ x%]
            ##.....F..F          [ y%]
            ## ==============
            test_method_res = ''
            is_test_finished = False
            for line in lines[1:]:
                if '=======' in line:
                    is_test_finished = True
                    break

                if line.strip().endswith('%]'):
                    test_method_res += line.split()[-3] if '[' in line.split()[-2] else line.split()[-2]

            filename_parts = test_res_file.split('/')[-1].split('.')[0].split('_')
            correctness = filename_parts[-1]
            iteration_id = filename_parts[-2]
            program = '_'.join(filename_parts[:-2])
            test_gen_ind = int(iteration_id)

            if test_gen_ind > MAX_ITERATIONS - 1:
                continue

            if ((not is_qb) and (not program in valid_src_ids_to_submission)) or (is_qb and (not program in valid_qb_programs)):
                continue

            if not is_test_finished:
                raise ValueError(f"Test not finished: {test_res_file}")

            for i, c in enumerate(test_method_res):
                test_method_id = f'{program}_{test_gen_ind}_{i}'
                if not test_method_id in test_method_results:
                    test_method_results[test_method_id] = {}

                if c == '.':
                    test_method_results[test_method_id][correctness] = 'passed'
                elif c == 'F':
                    test_method_results[test_method_id][correctness] = 'failed'
                else:
                    raise ValueError(f"Invalid test method result: {c}")
    
    det_test_methods = set()

    for k, v in test_method_results.items():
        if 'correct' in v and 'buggy' in v and v['correct'] == 'passed' and v['buggy'] == 'failed':
                det_test_methods.add(k)
    
    programs_with_det = set(['_'.join(x.split('_')[:-2]) for x in det_test_methods])
    programs_with_det_cnt = len(programs_with_det)
    print('Number of programs with DET', programs_with_det_cnt)
    print('Number of DET test methods', len(det_test_methods))

    report = {'test_method_results': test_method_results, 'det_test_methods': list(det_test_methods),
              'det_test_methods_cnt': len(det_test_methods), 'programs_with_det_cnt': programs_with_det_cnt}
    
    if not is_qb:
        problems_with_det = set([valid_src_ids_to_submission[x][0] for x in programs_with_det])
        report['problems_with_det'] = list(problems_with_det)
        report['problems_with_det_cnt'] = len(problems_with_det)
        print('Number of problems with DET', len(problems_with_det))

    with open('tmp/det_test_methods_info.json', 'w') as f:
        f.write(json.dumps(report, indent = 4))

def analyze_results_csv_file(argv):
    valid_src_ids_to_submission = retrive_valid_src_ids_to_submission("cb_submission_res_2acc_alt.csv", "cb_submission_res_v_0_3.csv")

    test_res = argv[0]
    test_res_analysis_path = argv[1]
    test_res_analysis = {}
    programs_with_buggy_fail = set()
    programs_with_correct_fail = set()
    with open(test_res) as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            program, correctness, test_gen_ind, failed, passed, xfailed  = line.split(',')
            test_gen_ind = int(test_gen_ind)
            
            if test_gen_ind > MAX_ITERATIONS - 1:
                continue

            if not program in valid_src_ids_to_submission:
                continue

            if program not in test_res_analysis:
                test_res_analysis[program] = {'buggy_fail': False, 'correct_fail': False, '(problem, author)': valid_src_ids_to_submission[program]}

            if failed != 'None' and int(failed) > 0 or ((xfailed == 'None' or int(xfailed) == 0) and (passed == 'None' or int(passed) == 0)):
                if correctness == 'buggy':
                    test_res_analysis[program]['buggy_fail'] = True
                    programs_with_buggy_fail.add(program)
                else:
                    test_res_analysis[program]['correct_fail'] = True
                    programs_with_correct_fail.add(program)
    
    test_res_analysis['programs_cnt'] = len(test_res_analysis.keys())
    test_res_analysis['programs_with_buggy_fail_cnt'] = len(programs_with_buggy_fail)
    test_res_analysis['programs_with_correct_fail_cnt'] = len(programs_with_correct_fail)
    test_res_analysis['programs_with_diff_detected_cnt'] = len(programs_with_buggy_fail.difference(programs_with_correct_fail))
    test_res_analysis['programs_with_buggy_fail'] = list(programs_with_buggy_fail)
    test_res_analysis['programs_with_correct_fail'] = list(programs_with_correct_fail)
    test_res_analysis['programs_with_diff_detected'] = list(programs_with_buggy_fail.difference(programs_with_correct_fail))

    test_res_analysis['problems_with_diff_detected'] = list(set([test_res_analysis[x]['(problem, author)'][0] for x in test_res_analysis['programs_with_diff_detected']]))
    test_res_analysis['submissions_with_diff_detected'] = list(set([f"{test_res_analysis[x]['(problem, author)'][0]}_{test_res_analysis[x]['(problem, author)'][1]}" for x in test_res_analysis['programs_with_diff_detected']]))
    
    with open(test_res_analysis_path, 'w') as convert_file:
        convert_file.write(json.dumps(test_res_analysis, indent = 4))

def main(argv):
    extract_test_method_dets()


if __name__ == "__main__":
    main(sys.argv[1:])