def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (n, m) = list(map(int, args[0].split()))
	    if (n <= m):
	        ret_values.append(n)
	        exit()
	    l = 0
	    r = (10 ** 19)
	    while (r > (l + 1)):
	        k = ((l + r) // 2)
	        if (((n - (((k - 1) * k) // 2)) - (m + k)) > 0):
	            l = k
	        else:
	            r = k
	    ret_values.append((m + r))

	return ret_values
