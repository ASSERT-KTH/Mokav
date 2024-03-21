def func(*args):
	ret_values = []
	
	from sys import stdin
	(a, b, c) = map(int, stdin.readline().split())
	if (((a != b) and (c == 0)) or ((b > a) and (c < 0))):
	    ret_values.append('NO')
	elif ((a == b) or ((b > a) and (c > 0) and (((b - a) % c) == 0)) or ((a > b) and (c < 0) and (((a - b) % c) == 0))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
