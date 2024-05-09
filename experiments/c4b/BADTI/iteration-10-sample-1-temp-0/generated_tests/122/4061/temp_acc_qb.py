def patched_func(*args):
	global_list = []
	
	l = list(map(int, args[0].split()))
	w = list(map(int, args[1].split()))
	r = [500, 1000, 1500, 2000, 2500]
	(a, b) = map(int, args[2].split())
	k = 0
	for i in range(5):
	    k = (k + max((0.3 * r[i]), (((1 - (l[i] / 250)) * r[i]) - (50 * w[i]))))
	k = (k + (a * 100))
	k = (k - (b * 50))
	global_list.append(int(k))
	return global_list