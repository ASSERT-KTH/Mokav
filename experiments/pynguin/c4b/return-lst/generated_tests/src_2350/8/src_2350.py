def func(*args):
	ret_values = []
	
	a = str(args[0])
	b = list(a)
	v = 0
	s = ['Q', 'H', '9']
	for c in b:
	    for i in s:
	        if (c == i):
	            v += 1
	            ret_values.append('YES')
	            break
	    if (v != 0):
	        break
	if (v == 0):
	    ret_values.append('NO')

	return ret_values
