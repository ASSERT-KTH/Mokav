def func(*args):
	ret_values = []
	
	a = args[0]
	b = ['h', 'e', 'l', 'l', 'o']
	c = 0
	d = 0
	for i in a:
	    if (b[c] == i):
	        c = (c + 1)
	        if (c == 5):
	            break
	if (c == 5):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
