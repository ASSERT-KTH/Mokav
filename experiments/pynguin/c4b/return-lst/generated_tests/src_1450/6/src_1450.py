def func(*args):
	ret_values = []
	
	string = args[0]
	(n, a, b) = string.split()
	n = int(n)
	a = int(a)
	b = int(b)
	front = a
	back = b
	i = 0
	post = 0
	a = (n - 1)
	b = 0
	while (b <= back):
	    if ((a >= front) and (b <= back)):
	        post += 1
	    a -= 1
	    b += 1
	ret_values.append(post)

	return ret_values
