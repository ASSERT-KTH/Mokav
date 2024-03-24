def func(*args):
	ret_values = []
	
	(n, k) = list(map(int, args[0].split()))
	if (k > n):
	    ret_values.append((- 1))
	    exit()
	if ((k == 1) and (n > 1)):
	    ret_values.append((- 1))
	    exit()
	if ((k == 1) and (n == 1)):
	    ret_values.append('a')
	    exit()
	s = ''
	f = 1
	for i in range(((n + 2) - k)):
	    s += ('a' if f else 'b')
	    f = (1 - f)
	c = ord('c')
	for i in range(((n + 2) - k), n):
	    s += chr(c)
	    c += 1
	ret_values.append(s)

	return ret_values
