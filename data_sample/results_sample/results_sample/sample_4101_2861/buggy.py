def func(*args):
	
	
	def sol(x, y, a):
	    se = set()
	    for i in range(0, 100):
	        if ((x ** i) > a):
	            return se
	        tmp = (x ** i)
	        for j in range(0, 100):
	            if (((y ** j) + tmp) > a):
	                break
	            else:
	                se.add(((y ** j) + tmp))
	(x, y, l, r) = map(int, args[0].split())
	se = sol(x, y, r)
	e = f = (- 1)
	ans = 0
	se = sorted(se, reverse=True)
	while se:
	    e = se.pop()
	    if (e >= l):
	        yield(e)
	        if (f > (- 1)):
	            ans = max(ans, ((e - f) - 1))
	        else:
	            ans = max(ans, (e - l))
	        f = e
	if (f > 0):
	    ans = max(ans, (r - e))
	else:
	    ans = ((r - l) + 1)
	yield(ans)
