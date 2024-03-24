def func(*args):
	ret_values = []
	
	a = args[0]
	b = 'hello'
	p = 0
	for i in range(len(a)):
	    if (a[i] == b[p]):
	        p += 1
	    if (p == 5):
	        ret_values.append('YES')
	        break
	if (p != 5):
	    ret_values.append('NO')

	return ret_values
