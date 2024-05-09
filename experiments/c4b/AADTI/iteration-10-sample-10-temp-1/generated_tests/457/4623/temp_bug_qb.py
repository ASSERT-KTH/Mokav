def original_func(*args):
	global_list = []
	
	
	def calc(x, y):
	    return int(((x / y) + 1))
	[a, ta] = list(map(int, args[0].split()))
	[b, tb] = list(map(int, args[1].split()))
	[hh, mm] = list(map(int, args[2].split(':')))
	bs = (5 * 60)
	be = ((23 * 60) + 59)
	s = ((hh * 60) + mm)
	e = (((hh * 60) + mm) + ta)
	a = (calc(max((s - tb), (bs - 1)), b) - calc((bs - 1), b))
	b = (calc(min((e - 1), be), b) - calc((bs - 1), b))
	global_list.append((b - a))
	return global_list