def patched_func(*args):
	global_list = []
	
	(x, w) = map(int, args[0].split())
	m = max(x, w)
	A = (6 - (m - 1))
	if (A == 1):
	    answer = '1/6'
	if (A == 2):
	    answer = '1/3'
	if (A == 3):
	    answer = '1/2'
	if (A == 4):
	    answer = '2/3'
	if (A == 5):
	    answer = '5/6'
	if (A == 6):
	    answer = '1/1'
	global_list.append(answer)
	return global_list