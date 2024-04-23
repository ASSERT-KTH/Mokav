def func(*args):
	
	s = [int(x) for x in args[0].split()]
	x = s[0]
	y = s[1]
	l = s[2]
	r = s[3]
	v = [(l - 1), (r + 1)]
	xx = 1
	yy = 1
	for i in range(64):
	    yy = 1
	    for j in range(64):
	        if (((xx + yy) <= r) and ((xx + yy) >= l)):
	            v.append((xx + yy))
	            yy = (y * yy)
	    xx = (xx * x)
	v = sorted(v)
	ans = 0
	for i in range(1, len(v)):
	    ans = max(ans, ((v[i] - v[(i - 1)]) - 1))
	yield(ans)
