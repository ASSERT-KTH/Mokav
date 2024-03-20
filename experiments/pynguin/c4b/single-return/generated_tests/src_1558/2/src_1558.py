def func(*args):
	
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
	return(sum(d_list))
