def func(*args):
	ret_values = []
	
	(a, b, c, d) = map(int, args[0].split())
	l = [a, b, c, d]
	l = sorted(l)
	if (((l[0] + l[1]) > l[3]) or ((l[0] + l[2]) > l[3]) or ((l[1] + l[2]) > l[3]) or ((l[0] + l[1]) > l[2])):
	    ret_values.append('TRIANGLE')
	elif (((l[0] + l[1]) == l[3]) or ((l[0] + l[2]) == l[3]) or ((l[1] + l[2]) == l[3]) or ((l[0] + l[1]) == l[2])):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
