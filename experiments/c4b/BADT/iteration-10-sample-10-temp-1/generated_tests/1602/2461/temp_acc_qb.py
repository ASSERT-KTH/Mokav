def patched_func(*args):
	global_list = []
	
	(x, t, a, b, da, db) = map(int, args[0].split())
	la = ([0] + list(range(a, (a - (t * da)), (- da))))
	lb = ([0] + list(range(b, (b - (t * db)), (- db))))
	global_list.append(('YES' if any((((pa + pb) == x) for pa in la for pb in lb)) else 'NO'))
	return global_list