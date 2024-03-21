def func(*args):
	ret_values = []
	
	(a, b, c) = map(int, args[0].split())
	if ((c % 2) != 0):
	    p = 'L'
	else:
	    p = 'R'
	nes = ((c // (2 * b)) + 1)
	if ((c % (2 * b)) == 0):
	    nes -= 1
	ost = (b - (abs((c - ((2 * nes) * b))) // 2))
	ret_values.append(nes, ost, p)

	return ret_values
