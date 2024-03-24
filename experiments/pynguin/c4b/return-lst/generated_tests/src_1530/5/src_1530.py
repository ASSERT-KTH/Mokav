def func(*args):
	ret_values = []
	
	T = args[0]
	a = len(set(T))
	strq = ''
	for k in T:
	    if (not (k in T)):
	        strq += k
	if ((a % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
