def func(*args):
	ret_values = []
	
	n = list(map(int, args[0].split()))
	p = 0
	for a in range(max((n[0] + 1), (n[1] + 1))):
	    for b in range(max((n[0] + 1), (n[1] + 1))):
	        if ((((a * a) + b) == n[0]) and (((b * b) + a) == n[1])):
	            p += 1
	ret_values.append(p)

	return ret_values
