def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	(c, d) = map(int, args[1].split())
	if (b == d):
	    ret_values.append(b)
	else:
	    s = set()
	    for i in range(0, 101):
	        s.add((b + (a * i)))
	    for i in range(0, 101):
	        temp = (d + (c * i))
	        if (temp in s):
	            ret_values.append(temp)
	            exit(0)
	    ret_values.append((- 1))

	return ret_values
