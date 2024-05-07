def patched_func(*args):
	global_list = []
	
	import itertools
	p = ([0] * 4)
	(p[0], p[1], p[2], p[3], a, b) = map(int, args[0].split())
	ans = 0
	for i in range(a, (b + 1)):
	    valid = 0
	    for perm in itertools.permutations(p):
	        if (i == ((((i % p[0]) % p[1]) % p[2]) % p[3])):
	            valid += 1
	    ans += (valid >= 7)
	global_list.append(ans)
	return global_list