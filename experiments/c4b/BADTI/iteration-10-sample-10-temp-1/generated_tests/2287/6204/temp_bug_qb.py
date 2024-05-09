def original_func(*args):
	global_list = []
	
	(ax, bx) = map(str, args[0].split())
	(a, b) = (int(ax), int(bx))
	d = (max(([(ord(c) - ord('0')) for c in ax] + [(ord(c) - ord('0')) for c in bx])) + 1)
	(ad, bd) = (0, 0)
	while (a > 0):
	    ad = ((ad * d) + (a % 10))
	    a //= 10
	while (b > 0):
	    bd = ((bd * d) + (b % 10))
	    b //= 10
	c = (ad + bd)
	ans = 0
	while (c > 0):
	    ans += 1
	    c //= d
	global_list.append(ans)
	return global_list