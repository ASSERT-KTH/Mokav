import sys
import os
import multiprocessing as mp

def process(pynguin_res_dir, correct_progs_dir, module_name, run_ind, timeout, assertion_generation):
    os.system(f'mkdir {pynguin_res_dir}/{module_name}/{run_ind}')
    os.system(f'cp {correct_progs_dir}/{module_name}.py {pynguin_res_dir}/{module_name}/{run_ind}/{module_name}.py')
    os.system(f'cp {correct_progs_dir}/node.py {pynguin_res_dir}/{module_name}/{run_ind}/node.py')
    os.system(f'PYNGUIN_DANGER_AWARE=TRUE pynguin --maximum-search-time {timeout} --project-path {pynguin_res_dir}/{module_name}/{run_ind}/' + 
              f' --output-path {pynguin_res_dir}/{module_name}/{run_ind}/ --module-name {module_name} --assertion-generation {assertion_generation}')

def main(argv):
    pynguin_res_dir = argv[0]
    correct_progs_dir = argv[1]
    modules_lst_file = argv[2]
    round_cnt = int(argv[3])
    timeout = int(argv[4])
    assertion_generation = argv[5]
    pool = mp.Pool(int(mp.cpu_count() / 4))

    with open(modules_lst_file) as file:
        lines = file.readlines()

        os.system(f'mkdir {pynguin_res_dir}')

        for i in range(len(lines)):
            line = lines[i].replace("\n", "")
            module_name = line.split(".")[0]
            os.system(f'mkdir {pynguin_res_dir}/{module_name}')
            for j in range(round_cnt):
                pool.apply_async(process, args = (pynguin_res_dir, correct_progs_dir, module_name, j, timeout, assertion_generation, ))

    pool.close()
    pool.join()

if __name__ == "__main__":
    main(sys.argv[1:])