def func(*args):
	ret_values = []
	
	t = tuple(map(int, args[0].split('.')))
	dc = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
	
	def f(d, m, y):
	    if ((m not in range(13)) or (d > (dc[m] + ((m == 2) and ((y % 4) == 0))))):
	        return False
	    else:
	        return (((t[2] - y) > 18) or (((t[2] - y) == 18) and ((m, d) <= (t[1], t[0]))))
	(a, b, c) = map(int, args[1].split('.'))
	ret_values.append(('YES' if any((f(a, b, c), f(a, c, b), f(b, a, c), f(b, c, a), f(c, a, b), f(c, b, a))) else 'NO'))

	return ret_values
