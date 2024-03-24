def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split())
	pp = []
	l = 0
	while (k > 0):
	    if (n == 1):
	        l += 1
	        break
	    for i in range(2, (n + 1)):
	        if (k == 1):
	            pp.append(str(n))
	            k -= 1
	            break
	        elif ((n % i) == 0):
	            k -= 1
	            n = (n // i)
	            pp.append(str(i))
	            break
	ret_values.append((' '.join(pp) if (l == 0) else '-1'))

	return ret_values
