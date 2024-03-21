def func(*args):
	ret_values = []
	
	(lambda x, nx: ret_values.append((int(nx) if (sum(map(int, nx)) > sum(map(int, x))) else x)))(*(lambda x, p: (x, ((x[:p] + str((int(x[p]) - 1))) + (((len(x) - p) - 1) * '9'))))(*(lambda x: (x, (min(([(x[1:].find(str(i)) + 1) for i in range(9) if (x[1:].find(str(i)) != (- 1))] + [len(x)])) - 1)))(args[0])))

	return ret_values
