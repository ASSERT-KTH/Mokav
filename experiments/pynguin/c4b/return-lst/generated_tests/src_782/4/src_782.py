def func(*args):
	ret_values = []
	
	
	def calc(cur, start, interv):
	    if (cur < start):
	        return 0
	    return int((((cur - start) / interv) + 1))
	[a, ta] = list(map(int, args[0].split()))
	[b, tb] = list(map(int, args[1].split()))
	[hh, mm] = list(map(int, args[2].split(':')))
	bs = (5 * 60)
	be = ((23 * 60) + 59)
	s = ((hh * 60) + mm)
	e = (((hh * 60) + mm) + ta)
	a = calc(max((s - tb), (bs - 1)), bs, b)
	b = calc(min((e - 1), be), bs, b)
	ret_values.append((b - a))

	return ret_values
