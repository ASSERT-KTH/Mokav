def func(*args):
	
	dc = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	(m, d) = map(int, args[0].split())
	return((((dc[m] + d) + 5) // 7))
