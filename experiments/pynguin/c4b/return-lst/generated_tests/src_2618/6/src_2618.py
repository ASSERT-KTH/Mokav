def func(*args):
	ret_values = []
	
	import math
	(x, y, l, r) = (int(i) for i in args[0].split())
	vvrs = []
	for i in range(60):
	    for j in range(60):
	        cur = ((x ** i) + (y ** j))
	        if (cur > r):
	            break
	        if (cur >= l):
	            vvrs.append(cur)
	vvrs.sort()
	maxcnt = 0
	for i in range((len(vvrs) - 1)):
	    rzn = (vvrs[(i + 1)] - vvrs[i])
	    if (rzn > maxcnt):
	        maxcnt = rzn
	if (len(vvrs) == 0):
	    ret_values.append(((r - l) + 1))
	else:
	    ret_values.append(max((maxcnt - 1), (vvrs[0] - l), (r - vvrs[(- 1)])))

	return ret_values
