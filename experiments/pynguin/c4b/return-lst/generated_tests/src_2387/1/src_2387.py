def func(*args):
	ret_values = []
	
	d = args[0]
	p = True
	for i in range((len(d) - 1)):
	    m = i
	    j = 1
	    while (d[m] == d[(m + 1)]):
	        m += 1
	        j += 1
	        if ((m + 1) > (len(d) - 1)):
	            break
	    if (j >= 7):
	        ret_values.append('YES')
	        p = False
	        break
	if p:
	    ret_values.append('NO')

	return ret_values
