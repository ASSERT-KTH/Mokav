def func(*args):
	ret_values = []
	
	args[0]
	inp = args[1]
	z = [(True if ((i == '4') or (i == '7')) else False) for i in inp]
	ans = list(map(int, inp))
	length = int((len(ans) / 2))
	if (all(z) and (sum(ans[0:length]) == sum(ans[length:]))):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
