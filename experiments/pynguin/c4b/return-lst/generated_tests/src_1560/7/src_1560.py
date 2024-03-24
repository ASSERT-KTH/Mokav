def func(*args):
	ret_values = []
	
	from sys import stdin
	r = [x.rstrip().find('1') for (i, x) in enumerate(stdin.readlines())]
	for (i, x) in enumerate(r):
	    if (x >= 0):
	        ret_values.append((abs((2 - i)) + (abs((x - 4)) // 2)))
	        break

	return ret_values
