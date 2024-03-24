def func(*args):
	
	(x, y, l, r) = map(int, args[0].split())
	X = 1
	st = set()
	while (X <= r):
	    Y = 1
	    while ((X + Y) <= r):
	        if ((X + Y) >= l):
	            st.add((X + Y))
	        Y *= y
	    X *= x
	bad = sorted([x for x in st])
	prev = l
	ans = 0
	for x in bad:
	    ans = max(ans, (x - prev))
	    prev = (x + 1)
	ans = max(ans, ((r - prev) + 1))
	return(ans)
