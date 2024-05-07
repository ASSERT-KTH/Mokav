def original_func(*args):
	global_list = []
	
	(a, b, c) = map(int, args[0].split())
	s1 = (a * b)
	s2 = (b * c)
	s3 = (c * a)
	a = (((s1 * s3) // s2) ** 0.5)
	b = (((s1 * s2) // s3) ** 0.5)
	c = (((s2 * s3) // s1) ** 0.5)
	global_list.append(int((4 * ((a + b) + c))))
	return global_list