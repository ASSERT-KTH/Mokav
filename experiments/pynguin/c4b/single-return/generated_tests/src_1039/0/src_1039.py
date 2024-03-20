def func(*args):
	
	m = '0fedabc'
	t = args[0]
	n = int(t[:(- 1)])
	s = t[(- 1)]
	n = (n - 1)
	k1 = m.find(s)
	k2 = (7 if (((n % 4) == 1) or ((n % 4) == 3)) else 0)
	k3 = (16 * (n // 4))
	return(((k1 + k2) + k3))
