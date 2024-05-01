def patched_func(*args):
	global_list = []
	
	
	def e_gcd(a, b):
	    s = pt = 0
	    ps = t = 1
	    r = b
	    pr = a
	    while r:
	        q = (pr // r)
	        (pr, r) = (r, (pr - (q * r)))
	        (ps, s) = (s, (ps - (q * s)))
	        (pt, t) = (t, (pt - (q * t)))
	    return (pr, (ps, pt))
	(a, b) = [int(x) for x in args[0].split()]
	(c, d) = [int(x) for x in args[1].split()]
	(g, x) = e_gcd(a, c)
	num = (d - b)
	if (num % g):
	    global_list.append((- 1))
	else:
	    (u, v) = x
	    xp = ((num * u) // g)
	    hs = (c // g)
	    if (not u):
	        xp += (num // g)
	    while (xp > 0):
	        xp -= hs
	    while (xp < 0):
	        xp += hs
	    ans = ((xp * a) + b)
	    if (ans < d):
	        (o, p) = e_gcd(a, c)
	        while (ans < d):
	            ans += ((a * c) // o)
	    global_list.append(ans)
	return global_list