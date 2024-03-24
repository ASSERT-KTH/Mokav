def func(*args):
	ret_values = []
	
	from sys import stdin
	(t, s, x) = map(int, stdin.readline().split())
	res = ((t + s) + 1)
	if ((t == x) or ((t + s) == x) or (((t + s) + 1) == x)):
	    ret_values.append('YES')
	elif ((t == 0) and (s == 0) and (x == 2)):
	    ret_values.append('NO')
	elif (x < ((t + s) + 1)):
	    ret_values.append('NO')
	elif (((x - ((t + s) + 1)) % s) == 0):
	    ret_values.append('YES')
	else:
	    a = ((x - ((t + s) + 1)) % s)
	    if ((s - a) == 1):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
