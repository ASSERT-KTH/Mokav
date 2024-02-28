import sys
import os
import multiprocessing as mp

def process(module_name, run_ind):
    os.system(f'mkdir pynguin-res/{module_name}/{run_ind}')
    os.system(f'cp correct_python_programs_bak/{module_name}.py pynguin-res/{module_name}/{run_ind}/{module_name}.py')
    os.system(f'cp correct_python_programs_bak/node.py pynguin-res/{module_name}/{run_ind}/node.py')
    os.system(f'PYNGUIN_DANGER_AWARE=TRUE pynguin --project-path pynguin-res/{module_name}/{run_ind}/ --output-path pynguin-res/{module_name}/{run_ind}/' + 
            f' --module-name {module_name}')

def main(argv):
    pool = mp.Pool()

    with open(argv[0]) as file:
        lines = file.readlines()
        for i in range(1, len(lines)):
            line = lines[i].replace("\n", "")
            module_name = line.split(".")[0]
            os.system(f'mkdir pynguin-res/{module_name}')
            for j in range(10):
                pool.apply_async(process, args = (module_name, j, ))

    pool.close()
    pool.join()

if __name__ == "__main__":
    main(sys.argv[1:])