def func(*args):
	ret_values = []
	
	n = int(args[0])
	l = list(map(int, args[1].split()))
	s = sum(l)
	if (n > s):
	    n = (n % s)
	if (n == 0):
	    for i in range(6, (- 1), (- 1)):
	        if (l[i] != 0):
	            ret_values.append((i + 1))
	            exit()
	c = 0
	for i in range(7):
	    c += l[i]
	    if (c >= n):
	        ret_values.append((i + 1))
	        exit()

	return ret_values
