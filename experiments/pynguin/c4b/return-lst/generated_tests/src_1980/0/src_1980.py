def func(*args):
	ret_values = []
	
	'\nDO NOT ASSUME THAT  K<=L\n'
	k = int(args[0])
	l = int(args[1])
	count = 0
	res = True
	if (k > l):
	    res = False
	while ((l >= k) and res):
	    if ((l % k) != 0):
	        res = False
	        break
	    l //= k
	    count += 1
	if (l > 1):
	    res = False
	if res:
	    ret_values.append('YES')
	    ret_values.append((count - 1))
	else:
	    ret_values.append('NO')

	return ret_values
