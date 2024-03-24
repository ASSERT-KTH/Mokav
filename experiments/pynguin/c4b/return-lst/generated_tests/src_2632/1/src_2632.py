def func(*args):
	ret_values = []
	
	(n, k) = map(int, args[0].split(' '))
	
	def factorize(n):
	    res = []
	    while (n > 1):
	        for i in range(2, 100000):
	            if ((n % i) == 0):
	                res.append(i)
	                n = (n / i)
	                break
	    return res
	l = factorize(n)
	if (len(l) < k):
	    ret_values.append('-1')
	elif (len(l) == k):
	    ret_values.append(' '.join(map(str, l)))
	else:
	    a = 1
	    for i in l[(k - 1):]:
	        a *= i
	    ret_values.append(' '.join(map(str, l[:(k - 1)])), a)

	return ret_values
