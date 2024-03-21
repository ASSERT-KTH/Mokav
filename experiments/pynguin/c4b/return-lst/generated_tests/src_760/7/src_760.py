def func(*args):
	ret_values = []
	
	(l, r) = map(int, args[0].split())
	s = set()
	
	def f(st, res):
	    if (st > 10):
	        s.add(res)
	    else:
	        if (res == 0):
	            f((st + 1), res)
	        for i in (4, 7):
	            f((st + 1), ((res * 10) + i))
	f(0, 0)
	s = sorted(s)
	a = 1
	b = 1
	q = 0
	if (l in s):
	    q -= l
	    l -= 1
	while (l >= s[a]):
	    a += 1
	while (r >= s[(b + 1)]):
	    b += 1
	if (a >= b):
	    q += (((min(r, s[a]) - l) + 1) * s[a])
	    if (r > s[a]):
	        q += (s[(a + 1)] * (r - s[a]))
	else:
	    if (l < s[a]):
	        q += (s[a] * ((s[a] - l) + 1))
	    if (r > s[b]):
	        q += (s[(b + 1)] * (r - s[b]))
	    for i in range(a, b):
	        q += (s[(i + 1)] * (s[(i + 1)] - s[i]))
	ret_values.append(q)

	return ret_values
