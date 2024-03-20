def func(*args):
	
	import fileinput, sys
	(n, k) = [int(x) for x in fileinput.input().readline().split()]
	min_lines = n
	steps = 2
	current_lines = (n // 2)
	seen = {n}
	
	def alg(lines):
	    global min_lines
	    global k
	    power = 0
	    running_total = 0
	    cur_val = (lines // (k ** power))
	    while cur_val:
	        running_total = (running_total + cur_val)
	        power = (power + 1)
	        cur_val = (lines // (k ** power))
	    if ((running_total >= n) and (lines < min_lines)):
	        min_lines = lines
	        return True
	    return False
	while (current_lines not in seen):
	    seen.add(current_lines)
	    if alg(current_lines):
	        current_lines = (current_lines - (n / (2 ** steps)))
	    else:
	        current_lines = (current_lines + (n / (2 ** steps)))
	    steps = (steps + 1)
	return(int(min_lines))
