def func(*args):
	ret_values = []
	
	al = 'abcdefghijklmnopqrstuvwxyz'
	(size, distinct) = map(int, args[0].split())
	ans = ''
	i = 0
	while (size > 0):
	    ans += al[i]
	    i += 1
	    if (i == distinct):
	        i = 0
	    size -= 1
	ret_values.append(ans)

	return ret_values
