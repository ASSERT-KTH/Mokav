def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	r = (- 1)
	while (l > 1):
	    if ((l % k) != 0):
	        ret_values.append('NO')
	        break
	    else:
	        r += 1
	        l //= k
	else:
	    ret_values.append('YES')
	    ret_values.append(r)

	return ret_values
