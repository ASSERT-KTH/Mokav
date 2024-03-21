def func(*args):
	ret_values = []
	
	(n, m) = list(map(int, args[0].split()))
	c = (n + 1)
	while (c <= m):
	    for i in range((c - 1), 1, (- 1)):
	        if ((c % i) == 0):
	            break
	    else:
	        if (c < m):
	            ret_values.append('NO')
	        elif (c == m):
	            ret_values.append('YES')
	        exit()
	    c += 1
	else:
	    ret_values.append('NO')

	return ret_values
