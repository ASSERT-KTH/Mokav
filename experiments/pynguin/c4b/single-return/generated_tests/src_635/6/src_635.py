def func(*args):
	
	from itertools import permutations
	from math import ceil, log
	(n, m) = t = list(map(int, args[0].split()))
	(l, _) = t = [(ceil(log(x, 7.0)) if (x > 1) else 1) for x in t]
	return(sum((((int(s[:l], 7) < n) and (int(s[l:], 7) < m)) for s in map(''.join, permutations('0123456', sum(t))))))
