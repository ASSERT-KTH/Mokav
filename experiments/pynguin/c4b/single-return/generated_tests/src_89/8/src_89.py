def func(*args):
	
	c = list(map(int, args[0].split()))
	s = sum(c)
	a = ([0] * 101)
	for i in range(5):
	    a[c[i]] += 1
	l = 0
	for i in range(100, 0, (- 1)):
	    if (a[i] > 1):
	        l = max((i * min(a[i], 3)), l)
	return((s - l))
