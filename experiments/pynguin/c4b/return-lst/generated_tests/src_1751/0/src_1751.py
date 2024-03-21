def func(*args):
	ret_values = []
	
	(n, m) = map(int, args[0].split())
	prime = True
	if ((n == 2) and (m == 3)):
	    ret_values.append('YES')
	elif ((n == 2) and (m != 3)):
	    ret_values.append('NO')
	else:
	    while True:
	        n += 2
	        for i in range(3, (int((n ** 0.5)) + 1), 2):
	            if ((n % i) == 0):
	                prime = False
	                break
	            else:
	                prime = True
	        if prime:
	            break
	    if (n == m):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
