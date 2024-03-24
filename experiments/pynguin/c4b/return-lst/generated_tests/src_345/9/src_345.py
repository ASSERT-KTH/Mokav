def func(*args):
	ret_values = []
	
	k = int(args[0])
	l = int(args[1])
	n = 0
	while ((k ** n) <= l):
	    if ((k ** n) == l):
	        ret_values.append('YES')
	        ret_values.append((n - 1))
	        exit()
	    n += 1
	ret_values.append('NO')

	return ret_values
