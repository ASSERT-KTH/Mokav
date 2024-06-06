import re

log_file = "logging_2024-05-30-17-11.log"

# Regular expression patterns for extracting relevant information
pattern_problem_id_author = r"###\(PROBLEM_ID, AUTHOR\)###: \((.*?), (.*?)\)"
pattern_iteration_count = r"###ITERATION###: (\d+)"
pattern_is_det = r"###IS_DET###: (.*?),CompletedProcess"
pattern_is_not_det = r"###IS_NOT_DET###: (.*?),CompletedProcess"

# Dictionary to store the counts for each PROBLEM_ID, AUTHOR, and iteration
counts = {}


with open(log_file, "r") as file:
    lines = file.readlines()

    problem_id = None
    iteration_count = None

    for line in lines:
        # Extract PROBLEM_ID and AUTHOR
        match_problem_id_author = re.search(pattern_problem_id_author, line)
        if match_problem_id_author:
            problem_id = match_problem_id_author.group(1)
            det_list = [0,0]
            


        # Extract iteration count
        match_iteration_count = re.search(pattern_iteration_count, line)
        # if match_iteration_count:
        #     iteration_count = match_iteration_count.group(1)
        #     print(iteration_count)
        # else:
        #     iteration_count = '0'
        
        # if iteration_count == '1':
        #     print('salam')

        # Count IS_DET
        match_is_det = re.search(pattern_is_det, line)
        match_is_not_det = re.search(pattern_is_not_det, line)

        if match_is_det:
            det_list[0] += 1
        if match_is_not_det:
            det_list[1] += 1


        if match_iteration_count:
            iteration_count = match_iteration_count.group(1)
            if problem_id not in counts:
                counts[problem_id] = {}
            if iteration_count not in counts[problem_id]:
                counts[problem_id][iteration_count] = [0,0]
            counts[problem_id][iteration_count] = det_list
            det_list = [0,0]


print(counts)

# Print the counts
for problem_id, iterations in counts.items():
    for iteration, count in iterations.items():
        print(f"PROBLEM_ID: {problem_id}, Iteration: {iteration}, IS_DET: {count[0]}, IS_NOT_DET: {count[1]}, Total: {count[0] + count[1]}")

# sum of all the IS_DET and IS_NOT_DET
total_det = 0
total_not_det = 0
for problem_id, iterations in counts.items():
    for iteration, count in iterations.items():
        total_det += count[0]
        total_not_det += count[1]

print(f"Total IS_DET: {total_det}, Total IS_NOT_DET: {total_not_det}")

# number of problems
print(f"Number of problems: {len(counts)}")

# perectage of program having is_det
print(f"Percentage of programs having IS_DET: {total_det / (total_det + total_not_det) * 100:.2f}%")


# percentage of programs having at least one det
problems_with_det = 0
for problem_id, iterations in counts.items():
    for iteration, count in iterations.items():
        if count[0] > 0:
            problems_with_det += 1
            break


print(problems_with_det)

print(f"Percentage of programs having at least one IS_DET: {problems_with_det / len(counts) * 100:.2f}%")