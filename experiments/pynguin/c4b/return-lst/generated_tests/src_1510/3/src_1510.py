def func(*args):
	ret_values = []
	
	s = list(args[0])
	h = list('hello')
	n = []
	j = 0
	for i in s:
	    if (i == h[j]):
	        n.append(i)
	        j += 1
	    if (j == 5):
	        break
	if (n == h):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
