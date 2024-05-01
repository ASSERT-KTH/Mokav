def patched_func(*args):
	global_list = []
	
	m = '0fedabc'
	t = args[0]
	n = int(t[:(- 1)])
	s = t[(- 1)]
	n = (n - 1)
	k1 = m.find(s)
	k2 = (7 if (((n % 4) == 1) or ((n % 4) == 3)) else 0)
	k3 = (16 * (n // 4))
	global_list.append(((k1 + k2) + k3))
	return global_list