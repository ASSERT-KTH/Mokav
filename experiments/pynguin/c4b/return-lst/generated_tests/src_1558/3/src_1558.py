def func(*args):
	ret_values = []
	
	from sys import stdin
	(k, l, m, n, d) = [int(x.rstrip()) for x in stdin.readlines()]
	d_list = ([False] + [False for _ in range(d)])
	for x in [k, l, m, n]:
	    if (x > d):
	        continue
	    if (not d_list[x]):
	        i = x
	        while (i <= d):
	            d_list[i] = True
	            i += x
	ret_values.append(sum(d_list))

	return ret_values
