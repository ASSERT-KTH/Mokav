def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	res = k
	cnt = 0
	while (res < l):
	    res *= k
	    cnt += 1
	if (res == l):
	    ret_values.append('YES')
	    ret_values.append(cnt)
	else:
	    ret_values.append('NO')

	return ret_values
