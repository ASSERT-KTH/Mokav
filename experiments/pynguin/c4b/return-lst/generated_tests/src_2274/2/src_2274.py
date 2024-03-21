def func(*args):
	ret_values = []
	
	z = args[0]
	t = 1
	summ = 0
	k = 0
	for e in str(z):
	    if ((e == '4') or (e == '7')):
	        k += 1
	for e in str(k):
	    if ((e != '4') and (e != '7')):
	        ret_values.append('NO')
	        t = 0
	        break
	if t:
	    ret_values.append('YES')

	return ret_values
