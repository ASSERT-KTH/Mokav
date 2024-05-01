def patched_func(*args):
	global_list = []
	
	(ax, bx) = map(str, args[0].split())
	d = (max(([(ord(c) - ord('0')) for c in ax] + [(ord(c) - ord('0')) for c in bx])) + 1)
	(ad, bd) = (0, 0)
	for dig in ax:
	    ad = ((ad * d) + ((ord(dig) - ord('0')) % 10))
	for dig in bx:
	    bd = ((bd * d) + ((ord(dig) - ord('0')) % 10))
	c = (ad + bd)
	ans = 0
	while (c > 0):
	    ans += 1
	    c //= d
	global_list.append(ans)
	return global_list