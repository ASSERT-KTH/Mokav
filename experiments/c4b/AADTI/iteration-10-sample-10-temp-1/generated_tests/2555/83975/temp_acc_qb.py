def patched_func(*args):
	global_list = []
	
	
	def it(nach, s, ind):
	    i = nach
	    while ((len(s) > i) and (s[i] == s[nach])):
	        i = (i + 1)
	    if ((i - nach) > 6):
	        ind = (ind + 1)
	    if ((len(s) - 1) > i):
	        ind = it(i, s, ind)
	    return ind
	s = args[0]
	ind = 0
	if (it(0, s, ind) > 0):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list