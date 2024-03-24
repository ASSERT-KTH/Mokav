def func(*args):
	ret_values = []
	
	l = []
	for x in range(0, 26):
	    l.append(0)
	a = args[0]
	a = list(a)
	for x in a:
	    l[(ord(x.lower()) - 97)] = 1
	t = 0
	for x in l:
	    t = (t + x)
	if ((t % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
