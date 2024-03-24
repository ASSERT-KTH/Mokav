def func(*args):
	
	from sys import stdin
	(x1, y1, x2, y2) = map(int, stdin.readline().split())
	dx = (x2 - x1)
	dy = (y2 - y1)
	result = ((((dx + 1) * (dy + 1)) + 1) // 2)
	return(result)
