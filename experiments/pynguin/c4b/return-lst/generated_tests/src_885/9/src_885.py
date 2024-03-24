def func(*args):
	ret_values = []
	
	(l, r, k) = map(int, args[0].split())
	i = 0
	flag = 0
	temp = pow(k, i)
	while (temp <= r):
	    if (temp >= l):
	        ret_values.append('{} '.format(temp), end='')
	        flag = 1
	    i += 1
	    temp = pow(k, i)
	if (flag == 0):
	    ret_values.append((- 1))

	return ret_values
