def original_func(*args):
	global_list = []
	
	s = args[0]
	row = int(s[:(len(s) - 1)])
	seat = s[(- 1)]
	dd = {'a': 4, 'b': 5, 'c': 6, 'd': 3, 'e': 2, 'f': 1}
	seat = dd[seat]
	ans = 0
	if ((row % 4) in [0, 3]):
	    row -= 2
	if ((row % 4) == 2):
	    ans += 6
	ans += (((row // 4) * 6) + (row - 1))
	global_list.append((ans + seat))
	return global_list