import sys
import os
import glob
import pandas as pd
import ast
import multiprocessing as mp

def process(target_dir, module_name):
    if os.path.exists(f'{target_dir}/test_{module_name}.py'):
        return
    # print(f'Processing {target_dir}/test_{module_name}.py')
    os.system(f'PYNGUIN_DANGER_AWARE=TRUE pynguin --maximum-search-time 1500 --project-path {target_dir}/ --output-path {target_dir}/ --module-name {module_name} 1>> {target_dir}/pynguin.log 2>> {target_dir}/pynguin.err')

def main(argv):
    pool = mp.Pool(1)

    df_submissions = pd.read_csv(argv[0])
    output_dir = argv[1]

    use_ret_lst = bool(argv[3])

    existing_tests = {}
    if argv[2] is not None and os.path.exists(argv[2]):
        with open(argv[2], "r") as existing_tests_f:
            lines = existing_tests_f.readlines()
            for existing_test in lines:
                existing_test = existing_test.replace("\n", "")
                row_num = existing_test.split("_")[2].split("/")[0]
                round = existing_test.split("/")[2]
                target_dir, source_id = existing_test.replace('.py', '').split("/test_")
                existing_tests[f'{row_num}_{round}'] = {'target_dir': target_dir, 'source_id': source_id}

    df_submissions = df_submissions[(df_submissions['failed_tests_ratio'] < 0.9)
                                    & (df_submissions['verdicts_id'] == 1) & (df_submissions['has_print_in_loop'] == False)
                                    & ((use_ret_lst | df_submissions['func_sourceCode'].str.count("print") == 1))]

    for i, source in enumerate(df_submissions['func_sourceCode'].values.tolist()):
        if use_ret_lst:
            source = source.replace("def func(*args):\n", "def func(*args):\n\tret_values = []\n")
            source = source.replace("print(", "ret_values.append(")
            source = source + "\n\treturn ret_values\n"
        else:
            source = source.replace("print(", "return(")

        source_hash = hash(source)
        if source_hash < 0:
            source_hash = -source_hash
        source_id = f'src_{source_hash}_{i}'
        src_dir = f'{output_dir}/{source_id}'
        os.system(f'mkdir {src_dir}')
        for j in range(10):
            if f'{i}_{j}' in existing_tests:
                continue

            target_dir = f'{src_dir}/{j}'
            os.system(f'mkdir {target_dir}')
            with open(f'{target_dir}/{source_id}.py', 'w') as f:
                f.write(source)
                process(target_dir, source_id)
                # pool.apply_async(process, args = (target_dir, f"{source_id}", ))

    pool.close()
    pool.join()

if __name__ == "__main__":
    main(sys.argv[1:])