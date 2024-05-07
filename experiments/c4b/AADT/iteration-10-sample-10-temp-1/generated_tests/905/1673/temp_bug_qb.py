def original_func(*args):
	global_list = []
	
	(n, m, k) = map(int, args[0].split())
	if ((k % 2) == 0):
	    l = 'R'
	if ((k % 2) != 0):
	    l = 'L'
	if ((k % (2 * m)) != 0):
	    p = ((k // (2 * m)) + 1)
	if ((k % (2 * m)) == 0):
	    p = (k // (2 * m))
	t = (((k - ((p - 1) * 6)) // 2) + ((k - ((p - 1) * 6)) % 2))
	global_list.append(((((str(p) + ' ') + str(t)) + ' ') + l))
	return global_list