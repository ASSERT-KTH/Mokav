def func(*args):
	ret_values = []
	
	
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
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
