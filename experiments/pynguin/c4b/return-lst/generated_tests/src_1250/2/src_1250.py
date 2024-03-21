def func(*args):
	ret_values = []
	
	(a, b, n) = args[0].split()
	n = int(n)
	test = a
	for i in range(10):
	    a += str(i)
	    if ((int(a) % int(b)) == 0):
	        break
	    else:
	        a = a[:(- 1)]
	if (test == a):
	    ret_values.append((- 1))
	    exit()
	n -= 1
	while (n != 0):
	    a += '0'
	    n -= 1
	ret_values.append(int(a))

	return ret_values
