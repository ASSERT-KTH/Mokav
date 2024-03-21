def func(*args):
	ret_values = []
	
	st = args[0]
	a = set()
	k = 0
	for e in st:
	    if (not (e in a)):
	        k += 1
	        a.add(e)
	if ((k % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
