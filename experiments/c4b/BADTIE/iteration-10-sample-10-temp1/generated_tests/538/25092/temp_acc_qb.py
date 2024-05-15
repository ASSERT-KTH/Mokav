def patched_func(*args):
	global_list = []
	
	from collections import Counter
	t = list(map(int, args[0].split(' ')))
	cnt = Counter()
	for tt in t:
	    cnt[tt] += 1
	ans = sum(t)
	for (tt, n) in cnt.items():
	    if (n >= 2):
	        ans = min(ans, (sum(t) - (min(n, 3) * tt)))
	global_list.append(ans)
	return global_list