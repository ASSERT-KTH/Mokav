import sys
import json 

def main(argv):
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
            if program not in test_res_analysis:
                test_res_analysis[program] = {'buggy_fail': False, 'correct_fail': False}
            if failed != 'None' and int(failed) > 0:
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
    
    with open(test_res_analysis_path, 'w') as convert_file:
        convert_file.write(json.dumps(test_res_analysis, indent = 4))


if __name__ == "__main__":
    main(sys.argv[1:])