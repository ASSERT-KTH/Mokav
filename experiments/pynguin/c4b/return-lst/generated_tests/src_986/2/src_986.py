def func(*args):
	ret_values = []
	
	
	def swap(t1, t2):
	    return (t2, t1)
	c = int(args[0])
	lim = 64
	ans = 1
	now = 2
	pre = 1
	while (now < c):
	    pre += (now + 1)
	    (pre, now) = swap(pre, now)
	    ans += 1
	if (c <= 2):
	    ret_values.append((c - 1))
	else:
	    ret_values.append(ans)

	return ret_values
