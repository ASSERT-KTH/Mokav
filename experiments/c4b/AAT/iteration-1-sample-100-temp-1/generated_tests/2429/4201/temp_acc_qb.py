def patched_func(*args):
	global_list = []
	
	(x, y, z, k) = map(int, args[0].split())
	sides = sorted([x, y, z])
	cuts = (3 * [None])
	product = 1
	for i in range(3):
	    a = min((sides[i] - 1), (k // (3 - i)))
	    cuts[i] = a
	    k -= a
	    product *= (a + 1)
	global_list.append(product)
	return global_list