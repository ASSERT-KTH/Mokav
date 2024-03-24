def func(*args):
	ret_values = []
	
	(x, t, a, b, da, db) = map(int, args[0].split())
	la = ([0] + list(range(a, (a - (t * da)), (- da))))
	lb = ([0] + list(range(b, (b - (t * db)), (- db))))
	ret_values.append(('YES' if any((((pa + pb) == x) for pa in la for pb in lb)) else 'NO'))

	return ret_values
