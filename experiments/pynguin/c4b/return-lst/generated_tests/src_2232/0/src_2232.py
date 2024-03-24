def func(*args):
	ret_values = []
	
	a = args[0]
	b = []
	if (1000 <= int(a) <= 9000):
	    for k in range((int(a) + 1), 9013):
	        k = str(k)
	        for i in k:
	            b.append(i)
	        c = set(b)
	        g = len(c)
	        if (len(a) == g):
	            ret_values.append(k)
	            break
	        b = []

	return ret_values
