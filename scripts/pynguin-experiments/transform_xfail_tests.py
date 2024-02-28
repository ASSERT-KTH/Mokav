import sys
import os
import glob

def main(argv):
    dir = argv[0]
    res = glob.glob(f'{dir}/*/*/test_*.py')
    for p in res:
        # if p != 'pynguin-res/lcs_length/0/test_lcs_length.py':
        #     continue

        with(open(p, "r")) as input_file:
            transformed_path = p.replace("/test_", "/test_transformed_")
            with(open(transformed_path, "w")) as f:
                is_xfail = False
                lines = input_file.readlines()
                for i, line in enumerate(lines):
                    if "xfail" in line:
                        is_xfail = True
                        f.write('#' + line)
                    else:
                        if is_xfail:
                            if i == len(lines) - 1 or lines[i + 1] == "\n":
                                f.write('#' + line)
                                is_xfail = False
                            else:
                                f.write(line)
                        else:
                            f.write(line)

if __name__ == "__main__":
    main(sys.argv[1:])