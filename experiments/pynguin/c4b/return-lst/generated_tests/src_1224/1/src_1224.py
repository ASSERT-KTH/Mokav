def func(*args):
	ret_values = []
	
	'\nCreated on Apr 27, 2016\nGmail : r.haque.249.rh@gmail.com\n@author: Md. Rezwanul Haque\n'
	'\nCreated on Apr 27, 2016\nGmail : r.haque.249.rh@gmail.com\n@author: Md. Rezwanul Haque\n'
	import sys
	f = sys.stdin
	(y, k, n) = map(int, f.readline().strip().split())
	if (y >= n):
	    first = (- 1)
	else:
	    t = k
	    while (t <= y):
	        t += k
	    first = (t - y)
	if (first == (- 1)):
	    ret_values.append((- 1))
	elif ((first + y) > n):
	    ret_values.append((- 1))
	else:
	    res = []
	    for i in range(first, ((n + 1) - y), k):
	        res.append(i)
	    ret_values.append(*res)

	return ret_values
