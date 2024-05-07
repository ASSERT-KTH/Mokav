def patched_func(*args):
	global_list = []
	
	(a, b) = [int(x) for x in args[0].split()]
	answer = 0
	while (a <= b):
	    a *= 3
	    b *= 2
	    answer += 1
	global_list.append(answer)
	return global_list